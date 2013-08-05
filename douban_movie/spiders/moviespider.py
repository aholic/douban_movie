#coding=utf-8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from douban_movie.items import DoubanMovieItem

class MovieSpider(BaseSpider):
    name = "movie.douban"
    start_urls = ["http://movie.douban.com/tag/喜剧?start=0&type=T"]

    def parse(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        ret = []
        hxs = HtmlXPathSelector(response)
        movies = hxs.select("//div[@class='pl2']/a/@href").extract()
        ret.extend([Request(url, callback=self.parse_movie) for url in movies])
        next_page = "".join(hxs.select("//span[@class='next']/a/@href").extract()).strip()
        ret.append(Request(next_page, callback=self.parse_page))
        return ret

    def parse_movie(self, response):
        hxs = HtmlXPathSelector(response)
        movie = DoubanMovieItem()
        movie['url_in_douban'] = unicode(response.url)
        movie['name_in_douban'] = "".join(hxs.select("//span[@property='v:itemreviewed']/text()").extract()).strip()
        movie['year'] = int(("".join(hxs.select("//span[@class='year']/text()").extract()).strip())[1:-1])
        movie['length'] = "".join(hxs.select("//span[@property='v:runtime']/@content").extract()).strip()
        movie['url_in_imdb'] = "".join(hxs.select("//div[@id='info']/a[last()]/@href").extract()).strip()
        movie['score'] = "".join(hxs.select("//strong[@class='ll rating_num'][@property='v:average']/text()").extract()).strip()
        movie['scored_num'] = "".join(hxs.select("//span[@property='v:votes']/text()").extract()).strip()

        tag_names = hxs.select("//div[@class='tags-body']/a/text()").extract()
        tag_times = hxs.select("//div[@class='tags-body']/a/span/text()").extract()
        tag_num = len(tag_names)
        tags = dict()
        for i in range(tag_num):
            tags[tag_names[i]] = int(tag_times[i][1:-1])
        movie['tags'] = tags
        return [movie]
