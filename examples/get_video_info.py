import ytdl

video = ytdl.Video("https://youtu.be/Wf2PCX2cTzc")
print(video.title)
print(video.author.name)
print(video.likes)
print(video.dislikes)
print(video.views)
for s in video.streams:
	msg = f"{s.ext} {s.quality} {s.file_size/1024/1024}MB\nDownload Link:\n{s.url}\n"
	print(msg)
