import scrapy
import json
class WeiboSpider(scrapy.Spider):
    name = "weibo"

    headers_base = {
        'Host': ' passport.weibo.cn',
        'Connection': ' keep-alive',
        # 'Content-Length': ' 347',
        'Origin': ' https://passport.weibo.cn',
        'User-Agent': ' Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        'Content-Type': ' application/x-www-form-urlencoded',
        'Accept': ' */*',
        'Referer': ' https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F%3Fjumpfrom%3Dwapv4%26tip%3D1',
        'Accept-Encoding': ' gzip, deflate, br',
        'Accept-Language': ' zh-CN,zh;q=0.8',
    }
    header_2 = {
        'Host': ' m.weibo.cn',
        'Connection': ' keep-alive',
        'Accept':' application/json, text/javascript, */*; q=0.01',
        # 'X-Requested-With': ' XMLHttpRequest',
        'User-Agent': ' Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        'Referer': ' https://m.weibo.cn/?jumpfrom=wapv4&tip=1',
        'Accept-Encoding': ' gzip, deflate, br',
        'Accept-Language': ' zh-CN,zh;q=0.8',
    }
    login_data ={
        'username': '13087052960',
        'password': 'qwert12345',
        'savestate': '1',
        'r': 'http://weibo.cn/',
        'ec': '0',
        'pagerefer': '',
        'entry': 'mweibo',
        'wentry': '',
        'loginfrom': '',
        'client_id':'',
        'code': '',
        'qq': '',
        'mainpageflag': '1',
        'hff': '',
        'hfp': '',
    }
    def start_requests(self):
        yield scrapy.FormRequest(
        url= 'https://passport.weibo.cn/sso/login',
        formdata=self.login_data,
        headers=self.headers_base,
        callback=self.parse,
        )

    def parse(self, response):
        # print(response.text)
        yield scrapy.Request(
            "https://m.weibo.cn/feed/friends?version=v4",
            headers=self.header_2,
            callback=self.download_json
        )

    wenjian_name = 0
    def download_json(self,response):
        print(response.url)
        print(response.text)
        # 其实response.text就是json对象，
        # json对象在Python中print，都是<class 'str'>
        print(type(response.text))
        # 我们将json文件loads下来，发现是列表型的，因为该text在
        # dumps的时候是以一个列表的形式转成json文件的。
        # 但我们把它loads python类型时,它又变成列表了，
        # 列表里是一个字典，字典里有一个next_cursor的key,
        # 我们按照python的数据类型取出来即可。
        print(type(json.loads(response.text)))
        print(type(json.loads(response.text)[0]))
        content = json.loads(response.text)[0]
        con = json.dumps(dict(content), ensure_ascii=False) + "\n"
        with open("C:\\Users\\Administrator\\Desktop\\papa\\xinlang\\jiazai\\"+str(self.wenjian_name)+".json", 'w', encoding="utf-8") as f:
            f.write(con)
            self.wenjian_name += 1
        next_consor = content['next_cursor']
        url_ajax = "https://m.weibo.cn/feed/friends?version=v4&next_cursor="+str(next_consor)+"&page=1"
        yield scrapy.Request(
            url_ajax,
            headers=self.header_2,
            callback=self.download_json
        )








