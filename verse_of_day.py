from json import loads as json_loads
from requests import get as req_get

from html import unescape
from icecream import ic


class DailyVerse():
	@classmethod
	def supports_search(self):
		return True

	@staticmethod
	def get_verse(version):
		response = json_loads(req_get('https://www.biblegateway.com/votd/get/?format=json&version=' + version).content)
		return [{'quote': unescape(response['votd']['text']), 'author': response['votd']['display_ref'], 'sourceName': None, 'link': None}]

	def get_random(self):
		return self.get_verse('ESV')

	def get_for_author(self, author):
		return self.get_verse(author)

	def get_for_keyword(self, keyword):
	    return self.get_verse(keyword)
	
def get_bible_quote_of_day():
    my_verse = DailyVerse.get_verse('ESV')[0]
    chapter_and_verse = my_verse['author']
    verse_string = my_verse['quote']

    try:
        verse_string = verse_string.split('[')[1]
        verse_string = verse_string.split(']  ')[1]
    except:
        pass

    book_and_chapter, verses = chapter_and_verse.split(':')
    book_and_chapter = book_and_chapter + ':'
    chapter = book_and_chapter.split(' ')[-1]
    last_part = chapter
    book = (book_and_chapter.split(last_part)[0]).strip()
    book = book.split(':')[0].strip()
    if '-' in verses:
        num_verses = 'Verses ' 
    else:
        num_verses = 'Verse '
    chapter = chapter.split(':')[0].strip()
    verse_string = verse_string.replace('“','')
    verse_string = verse_string.replace('”','')
    verse_string = verse_string.replace('  ', ' ')
    verse_string = verse_string.replace('  ', ' ')
    verse_string = verse_string.strip()
	
    speaking_part_of_chapter_verse = book + ' Chapter ' + chapter + ', ' + num_verses +  verses + '. '
    speaking_part = speaking_part_of_chapter_verse + verse_string
    print_statement = chapter_and_verse + ' - ' + verse_string
    return [print_statement, speaking_part]


#ic(get_bible_quote_of_day())