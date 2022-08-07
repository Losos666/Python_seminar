import pytube
link = "https://www.youtube.com/watch?v=M27MkCUMxj8"
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download()



# from progress.bar import Bar

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     bar.next()
# bar.finish()

# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=M27MkCUMxj8")
# yt = yt.get('mp4', '720p')
# yt.download('/path/to/download/directory')
