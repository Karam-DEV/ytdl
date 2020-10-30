from __future__ import unicode_literals
import datetime
from .base import (
		BaseVideo,
		BaseStream,
		Author
	)
import youtube_dl

class Video(BaseVideo):
	def __init__(self, *args, **kwargs):
		self._ydl_info = None
		self._ydl_opts = {'quiet': True, 'prefer_insecure': False, 'no_warnings': True}
		ydl_opts = kwargs.get("ydl_opts")
		if ydl_opts:
			self._ydl_opts.update(ydl_opts)
		super(Video, self).__init__(*args, **kwargs)
	
	def _fetch_basic(self):
		""" Fetch basic data and streams. """
		if self._have_basic:
			return
		with youtube_dl.YoutubeDL(self._ydl_opts) as ydl:
			info = ydl.extract_info(self.video_id, download=False)
			self._title = info['title']
			self._author = Author(info['uploader'], info['uploader_id'])
			self._views = info['view_count']
			self._likes = info['like_count']
			self._dislikes = info['dislike_count']
			self._length = info['duration']
			upload_date = info['upload_date']
			upload_date = int(upload_date[:4]), int(upload_date[4:6]), int(upload_date[6:])
			self._upload_date = datetime.datetime(*upload_date)
			self._rating = info['average_rating']
			self._category = info['categories'][0] if info['categories'] else ''
			allstreams = [Stream(s, self) for s in info['formats']]
			self._streams = [i for i in allstreams if i.mediatype == 'normal']
			self._audio_streams = [i for i in allstreams if i.mediatype == 'audio']
			self._video_streams = [i for i in allstreams if i.mediatype == 'video']
			self._all_streams = allstreams
		self._have_basic = True
			
class Stream(BaseStream):
	def __init__(self, info, parent):
		super(Stream, self).__init__(parent)
		self._itag = info['format_id']
		
		#  _mediatype detected
		if (info.get('acodec') != 'none' and info.get('vcodec') == 'none'):self._mediatype = 'audio'
		elif (info.get('acodec') == 'none' and info.get('vcodec') != 'none'):self._mediatype = 'video'
		else:self._mediatype = 'normal'
		
		self._threed = info.get('format_note') == '3D'
		self._rawbitrate = info.get('abr', 0) * 1024
		self._bitrate = f"{info.get('abr', 0)}K"
		height = info.get('height') or 0
		width = info.get('width') or 0
		self._resolution = f'{height}x{width}'
		self._quality = self._bitrate if self._mediatype == 'audio' else self._resolution
		self._extension = info['ext']
		self._notes = info.get('format_note') or ''
		self._url = info.get('url')
		if self._url.startswith("https://manifest.googlevideo.com"):
			self._url = info.get('fragment_base_url', self._url)
		self._file_size = info.get('filesize')

