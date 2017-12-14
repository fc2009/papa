# -*- coding: utf-8 -*-
import scrapy

class GupiaoSpider(scrapy.Spider):
    name = 'gupiao'
    start_urls = ['http://stock.10jqka.com.cn/']

    def parse(self, response):
        # print(response.text)
        base = response.xpath('//div[@id="rzrq"]/table/tbody/tr/td[2]/a')
        for gu in base:
            gu_name = gu.xpath('./text()').extract()[0]
            gu_url = gu.xpath('./@href').extract()[0]
            gu_hao = gu_url.split('/')[-2]
            # print(gu_name)
            # print(gu_url)
            yield scrapy.Request(
                gu_url,
                callback=self.down_gu,
                meta={
                    "gu_name":gu_name,
                    "gu_hao":gu_hao,
                    "index":1
                }
            )
    def down_gu(self,response):
        table = []
        print(response.url)
        tr_list = response.xpath('//table[@class="m-table"]/tbody/tr')
        for td in tr_list:
            content_list = td.xpath('./td/text()').extract()
            content_list[1] = content_list[1].strip()
            # print('】，【'.join(content_list))
            table.append('|，|'.join(content_list))
            print(response.url)
            print(table)
        with open('C:\\Users\\Administrator\\Desktop\\papa\\stock\\gupiao\\'+response.meta["gu_name"]+'.txt', 'a') as f:
            f.write('\n'.join(table)+'\n')
            f.close()
                # f.write('\n'.join(table)+'\n')
        # 还有很多页，是动态加载的，这里我们只取前三页。
        if response.meta['index'] > 3:
            return

        response.meta['index'] += 1
# http://data.10jqka.com.cn/market/rzrqgg/code/000725/order/desc/page/2/ajax/ 1 /
        page_url = 'http://data.10jqka.com.cn/market/rzrqgg/3/ajax/code/'+str(response.meta['gu_hao'])+'/desc/page/order/desc/page/' + str(response.meta['index'])+'/ajax/1/'
        yield scrapy.Request(
            url=page_url,
            callback=self.down_gu,
            meta={
                "gu_name":response.meta['gu_name'],
                "gu_hao":response.meta['gu_hao'],
                "index": response.meta['index'],
            }
        )
