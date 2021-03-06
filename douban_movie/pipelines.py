#coding=utf-8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sqlite3 as sq3
db_init_statement = '''
create table if not exists movie_info(
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
db = sq3.connect('movie.db')
db.execute(db_init_statement)
db.commit()

class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        smt = "insert into movie_info values ("
        url_in_douban = "".join(['"', item['url_in_douban'], '"'])
        name_in_douban = "".join(['"', item['name_in_douban'], '"'])
        year = item['year']
        length = "".join(['"', item['length'], '"'])
        url_in_imdb = "".join(['"', item['url_in_imdb'], '"'])
        score = item['score']
        scored_num = item['scored_num']
        tags = '"'
        for tag in item['tags']:
            tags += tag
            tags += ','
            tags += item['tags'][tag]
            tags += '|'
        tags = tags[0:-1]
        tags += '"'
        smt += (','.join([url_in_douban, name_in_douban, year, length, url_in_imdb, score, scored_num, tags]))
        smt += ')'
        db.execute(smt)
        db.commit()
        return item

#class DoubanMovieItem(Item):
#    # define the fields for your item here like:
#    url_in_douban = Field()
#    name_in_douban = Field() # name in douban page, Chinese/Foreign language
#    year = Field() # release time
#    length = Field() # how long this movie lasts
#    url_in_imdb = Field()
#    score = Field() # its score, a number like 9.5
#    scored_num = Field() # how many people scored this movie
#    tags = Field() # it's a dict, maps from tagname to tagtimes
