from __future__ import unicode_literals
import re
from urllib.parse import parse_qs, urlparse
import requests as req
def extract_video_id(url:str):
	idregx = re.compile(r'[\w-]{11}$')
	url = url.strip()
	if idregx.match(url):
		return url # ID of video
	if '://' not in url:
		url = '//' + url
	parsedurl = urlparse(url)
	if parsedurl.netloc in ('youtube.com', 'www.youtube.com', 'm.youtube.com', 'gaming.youtube.com'):
		query = parse_qs(parsedurl.query)
		if 'v' in query and idregx.match(query['v'][0]):
			return query['v'][0]
	elif parsedurl.netloc in ('youtu.be', 'www.youtu.be'):
		vidid = parsedurl.path.split('/')[-1] if parsedurl.path else ''
		if idregx.match(vidid):
			return vidid
	
	err = f"Need 11 character video id or the URL of the video. Got {url}"
	raise ValueError(err)

def get_stream_size(url):
	return req.get(url, stream=True).headers['Content-length']