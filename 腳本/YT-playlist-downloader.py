url=input('輸入播放清單網址:')
from pytube import Playlist
pl = Playlist(url)
pl.download_all('G:/')