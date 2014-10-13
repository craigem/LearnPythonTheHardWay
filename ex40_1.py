# 1. Write some more songs using this and make sure you understand that you're 
# passing a list of strings as the lyrics.

class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

five_yards = Song(["Be there no-one left on Earth but you",
					"One thing shall remain true."])

dc = Song(["D.C. you raised some backs up by the things you said, and",
			"You stood your ground while weaker ones just turned and fled, but",
			"When it came time to count your foes amongst your friends, well",
			"There was respect and so much love that never ends, 'cos",
			"D.C. you gave them happiness and hobnob days and they will",
			"Cherish them forever and when they get the blues and greys"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

five_yards.sing_me_a_song()

dc.sing_me_a_song()
