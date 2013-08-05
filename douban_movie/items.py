# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class DoubanMovieItem(Item):
    # define the fields for your item here like:
    url_in_douban = Field()
    name_in_douban = Field() # name in douban page, Chinese/Foreign language
    year = Field() # release time
    length = Field() # how long this movie lasts
    url_in_imdb = Field()
    score = Field() # its score, a number like 9.5
    scored_num = Field() # how many people scored thi movie
    tags = Field() # it's a dict, maps from tagname to tagtimes
