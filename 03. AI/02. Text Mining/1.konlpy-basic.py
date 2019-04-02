# from konlpy.tag import  Twitter
# twitter = Twitter()
# malist = twitter.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
# print(malist)
# malist = twitter.pos("아버지가 방에 들어가신다.", norm=True, stem=True)
# print(malist)

from konlpy.tag import Okt
okt = Okt()
malist = okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True)
print(malist)
