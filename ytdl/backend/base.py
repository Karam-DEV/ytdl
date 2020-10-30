from __future__ import unicode_literals
import time
from ytdl.util import (
		extract_video_id,
		get_stream_size
	)


class BaseVideo:
	def __init__(self,url:str,basic=True):
		self._video_id = extract_video_id(url)
		self._title = None
		self._author = None
		self._likes = None
		self._dislikes = None
		self._views = None
		self._length = None
		self._description = None
		self._duration = None
		self._rating = None
		self._tags = None
		self._category = None
		self._upload_date = None
		
		self._streams = []
		self._video_streams = []
		self._audio_streams = []
		self._all_streams = []
		
		self._have_basic = False
		self._have_gdata = False
		
		if basic:
			self._fetch_basic()
	
	def _fetch_basic(self):
		"""Extract basic video information"""
		raise NotImplementedError("The Method must be implemented")
	def _fetch_gdata(self):
		"""Extract description and  """
		raise NotImplementedError("The Method must be implemented")
	@property
	def video_id(self):
		return self._video_id
	@property
	def title(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._title
	@property
	def author(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._author
	@property
	def likes(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._likes
	@property
	def dislikes(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._dislikes
	@property
	def views(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._views
	@property
	def length(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._length
	@property
	def duration(self):
		if not self._have_basic:
			self._fetch_basic()
		self._duration = time.strftime('%H:%M:%S', time.gmtime(self._length))
		return self._duration
	@property
	def description(self):
		if not self._have_gdata:
			self._fetch_gdata()
		return self._length
	@property
	def rating(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._rating
	@property
	def tags(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._tags
	@property
	def category(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._category
	@property
	def upload_date(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._upload_date
	
	@property
	def all_streams(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._all_streams
	@property
	def streams(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._streams
	@property
	def video_streams(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._video_streams
	@property
	def audio_streams(self):
		if not self._have_basic:
			self._fetch_basic()
		return self._audio_streams


class BaseStream:
	def __init__(self,parent):
		self._itag = None
		self._mediatype = None
		self._raw_bitrate = None
		self._bitrate = None
		self._resolution = None
		self._quality = None
		self._extension = None
		self._notes = None
		self._url = None
		self._filename = None
		self._file_size = None
		self._threed = None
		self._parent = parent
	
	@property
	def itag(self):
		return self._itag
	@property
	def mediatype(self):
		return self._mediatype
	@property
	def raw_bitrate(self):
		return self._raw_bitrate
	@property
	def bitrate(self):
		return self._bitrate
	@property
	def resolution(self):
		return self._resolution
	@property
	def quality(self):
		return self._quality
	@property
	def ext(self):
		return self._extension
	@property
	def notes(self):
		return self._notes
	@property
	def url(self):
		return self._url
	@property
	def filename(self):
		return self._filename
	@property
	def file_size(self):
		if not self._file_size:
			self._file_size = get_stream_size(self.url)
		return self._file_size
	@property
	def parent(self):
		return self._parent
		
		
		

class Author:
	def __init__(self,name:str,id:str):
		self.name = name
		self.id = id
	
	@property
	def url(self):
		return f"http://www.youtube.com/channel/{self.id}"
