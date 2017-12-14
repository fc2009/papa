# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time
import re

class BookspiderSpider(CrawlSpider):
    name = 'bookSpider'
    allowed_domains = ['quanwenyuedu.io']
    start_urls = ['http://www.quanwenyuedu.io/']

    rules = (
        Rule(LinkExtractor(allow=r'aoshidanshen.quanwenyuedu.io$', deny='big5'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/\d+.html$', deny='big5'), callback='ajax_info', follow=True)
    )

    def parse_item(self, response):
        print("url========", response.url)
        global book_name
        book_name = response.xpath('//div[@class="top"]/p[@class="title"]/span/text()').extract()[0]
        print(book_name)
        # print('=================================================')
        book_info = response.xpath('//div[@class="top"]')
        info = book_info.xpath('string(.)').extract()[0].strip().replace('\n',' ')
        print(info)
        with open("C:\\Users\\Administrator\\Desktop\\papa\\bookspider\\file\\"+book_name+'.txt','a') as f:
            f.write(info+"\n\n\n")
            time.sleep(1)
        # # i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
    def ajax_info(self,response):
        form_data={
            'c': 'book',
            'a': 'ajax',
        }
        zz = re.compile(r'setTimeout.*')
        js = zz.search(response.text)
        js_list = js.group().split("','")

        form_data['id'] = js_list[3]
        form_data['sky'] =js_list[5]
        form_data['t'] =js_list[7].split("'")[0]
        form_data['rndval'] =str(int(time.time() * 1000))
        print(form_data)
        url_str = ''.join(response.url.split('io/')[:-1]) + 'io/index.php?c=book&a=ajax'
        yield scrapy.FormRequest(url=url_str,
                             formdata=form_data,
                             callback=self.info_parse
                                 )
    def info_parse(self,response):
        print('get_text =====', response.url)
        # 这样不行因为我们处理的是ajax的内容，而不是加载过后的页面，我们可以
        # 把response.text打印出来看看，请求过来的结构。
        print(response.text)
        # text = '\n'.join(response.xpath('//div[@class="articlebody"]/text()').extract())
        text = '\n'.join(response.xpath("//text()").extract())
        # print(text)
        time.sleep(1)
        with open("C:\\Users\\Administrator\\Desktop\\papa\\bookspider\\file\\"+book_name+'.txt', 'a') as f:
            f.write(text+ '\n\n=====================================\n')





