import media
import fresh_tomatoes

# Initiate instances of movie class

the_departed = media.Movie(
	"The Departed",
	"tagline",
	"https://www.youtube.com/watch?v=iojhqm0JTW4",
	"94",
	"https://www.rottentomatoes.com/m/departed/"
	"https://resizing.flixster.com/C3KwdGYuUGFuBcsJ8WaPCqvw-oQ=/206x305/v1.bTsxMTE2NjcyMTtqOzE3MDk0OzEyMDA7ODAwOzEyMDA"
	)

the_town = media.Movie(
	"The Town",
	"Critics Consensus: Tense, smartly written, and wonderfully cast, The Town proves that Ben Affleck has rediscovered his muse -- and that he's a director to be reckoned with.",
	"https://www.youtube.com/watch?v=WcXt9aUMbBk",
	"94",
	"https://www.rottentomatoes.com/m/the_town/"
	"https://resizing.flixster.com/eGDf5HoDpMlpgs8fre8RgZzOvU8=/206x305/v1.bTsxMTE2NjczMjtqOzE3MDk0OzEyMDA7ODAwOzEyMDA"
	)

mystic_river = media.Movie(
	"Mystic River",
	"Critics Consensus: Anchored by the exceptional acting of its strong cast, Mystic River is a somber drama that unfolds in layers and conveys the tragedy of its story with visceral power",
	"https://www.youtube.com/watch?v=W7NktJhrRYQ",
	"87",
	"https://www.rottentomatoes.com/m/mystic_river"
	"https://resizing.flixster.com/eGDf5HoDpMlpgs8fre8RgZzOvU8=/206x305/v1.bTsxMTE2NjczMjtqOzE3MDk0OzEyMDA7ODAwOzEyMDA"
	)

gone_baby_gone = media.Movie(
	"Gone Baby Gone",
	"Critics Consensus: Ben Affleck proves his directing credentials in this gripping dramatic thriller, drawing strong performances from the excellent cast and bringing working-class Boston to the screen.",
	"https://www.youtube.com/watch?v=vAhPH8Qa_os",
	"94",
	"https://www.rottentomatoes.com/m/gone_baby_gone"
	"https://resizing.flixster.com/VDQeC8Tdx6ktxADjC5p-aSCat8I=/206x305/v1.bTsxMTE3NjE5ODtqOzE3MDk0OzEyMDA7ODAwOzEyMDA"
	)

ted = media.Movie(
	"Ted",
	"Critics Consensus: Ted's romance versus bromance plot is familiar, but the film's held aloft by the high-concept central premise and a very funny (albeit inconsistent) script.",
	"https://www.youtube.com/watch?v=9fbo_pQvU7M",
	"67",
	"https://www.rottentomatoes.com/m/ted_2012"
	"https://resizing.flixster.com/mjT6cQ9oRB_EFajO5lThVVfOgnc=/206x305/v1.bTsxMTE2NzQyODtqOzE3MDk0OzEyMDA7ODAwOzEyMDA"
	)

the_boondock_saints = media.Movie(
	"The Boondock Saints",
	"Critics Consensus: A juvenile, ugly movie that represents the worst tendencies of directors channeling Tarantino.",
	"https://www.youtube.com/watch?v=ydXojYfCF3I",
	"20",
	"https://www.rottentomatoes.com/m/boondock_saints"
	"https://resizing.flixster.com/bLDds8lCNnzUyyBVM9CDz2-yx-w=/206x305/v1.bTsxMTIwODQ4NTtqOzE3MDk0OzEyMDA7MTMwNTsxNzQw"
	)

the_fighter = media.Movie(
	"The Fighter",
	"Critics Consensus: Led by a trio of captivating performances from Mark Wahlberg, Christian Bale, and Amy Adams, The Fighter is a solidly entertaining, albeit predictable, entry in the boxing drama genre.",
	"https://www.youtube.com/watch?v=71l-kIhJ5j8",
	"90",
	"https://www.rottentomatoes.com/m/the-fighter"
	"https://resizing.flixster.com/30HO5Y9YHJpyJxKEw26LZUZahaU=/206x305/v1.bTsxMTE2ODkzOTtqOzE3MDk0OzEyMDA7ODAwOzEyMDA"
	)

good_will_hunting = media.Movie(
	"Good Will Hunting",
	"Critics Consensus: It follows a predictable narrative arc, but Good Will Hunting adds enough quirks to the journey -- and is loaded with enough powerful performances -- that it remains an entertaining, emotionally rich drama.",
	"https://www.youtube.com/watch?v=nH9LZOXBMUE",
	"97",
	"https://www.rottentomatoes.com/m/good_will_hunting/"
	"https://resizing.flixster.com/vDSTX05Ie8kZHC2prKm-3ahl-bU=/206x305/v1.bTsxMTYxNDc1NjtqOzE3MTQ0OzEyMDA7Nzk4OzEwNjQ"
	)

movie_list = [the_departed, the_town, mystic_river, gone_baby_gone, ted, the_boondock_saints, the_fighter, good_will_hunting]

fresh_tomatoes.open_movies_page(movie_list)
