# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

db_init_statement = '''
create table if not exits movie_info(
url_in_douban nchar(128),
name_in_douban nchar(64),
year int,
length nchar(32),
url_in_imdb nchar(128),
score float,
scored_num int,
tags nchar(128),
primary key(url_in_douban))
'''
class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        smt = '''insert into movie_info values ('''
        smt += ''')'''
        return item

#class DoubanMovieItem(Item):
#    # define the fields for your item here like:
#    url_in_douban = Field()
#    name_in_douban = Field() # name in douban page, Chinese/Foreign language
#    year = Field() # release time
#    length = Field() # how long this movie lasts
#    url_in_imdb = Field()
#    score = Field() # its score, a number like 9.5
#    scored_num = Field() # how many people scored thi movie
#    tags = Field() # it's a dict, maps from tagname to tagtimes
