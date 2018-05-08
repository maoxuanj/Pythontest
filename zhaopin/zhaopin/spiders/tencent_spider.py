# -*- coding: utf-8 -*-
import  re
import  json
from  scrapy.selector  import  Selector
try:
        from  scrapy.spider  import  Spider
except:
        from  scrapy.spider  import  BaseSpider  as  Spider
from  scrapy.utils.response  import  get_base_url
from  scrapy.utils.url  import  urljoin_rfc
from  scrapy.contrib.spiders  import  CrawlSpider,  Rule
from  scrapy.contrib.linkextractors.sgml  import  SgmlLinkExtractor  as  sle
from  zhaopin.items  import  *
class  TencentSpider(CrawlSpider):
        name  =  "zhaopin"
        allowed_domains  =  ["zhaopin.com"]
        start_urls  =  [
                "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%AE%81%E6%B3%A2&kw=python&sm=0"
        ]
        rules  =  [  #  定义爬取URL的规则
                Rule(sle(allow="/zhaopin.com\?&start=\d{,4}#a"), follow=True, callback='parse_item')
        ]
        def  parse_item(self,  response):  #  提取数据到Items里面，主要用到XPath和CSS选择器提取网页数据
                items  =  []
                sel  =  Selector(response)
                base_url  =  get_base_url(response)
                sites_even  =  sel.css('table.tablelist  tr.even')
                for  site  in  sites_even:
                        item  =  ZhaopinItem()
                        item['name']  =  site.css('.l.square  a').xpath('text()').extract()
                        relative_url  =  site.css('.l.square  a').xpath('@href').extract()[0]
                        item['detailLink']  =  urljoin_rfc(base_url,  relative_url)
                        item['catalog']  =  site.css('tr  >  td:nth-child(2)::text').extract()
                        item['workLocation']  =  site.css('tr  >  td:nth-child(4)::text').extract()
                        item['recruitNumber']  =  site.css('tr  >  td:nth-child(3)::text').extract()
                        item['publishTime']  =  site.css('tr  >  td:nth-child(5)::text').extract()
                        items.append(item)
                        #print  repr(item).decode("unicode-escape")  +  '\n'
                sites_odd  =  sel.css('table.tablelist  tr.odd')
                for  site  in  sites_odd:
                        item  =  ZhaopinItem()
                        item['name']  =  site.css('.l.square  a').xpath('text()').extract()
                        relative_url  =  site.css('.l.square  a').xpath('@href').extract()[0]
                        item['detailLink']  =  urljoin_rfc(base_url,  relative_url)
                        item['catalog']  =  site.css('tr  >  td:nth-child(2)::text').extract()
                        item['workLocation']  =  site.css('tr  >  td:nth-child(4)::text').extract()
                        item['recruitNumber']  =  site.css('tr  >  td:nth-child(3)::text').extract()
                        item['publishTime']  =  site.css('tr  >  td:nth-child(5)::text').extract()
                        items.append(item)
                        #print  repr(item).decode("unicode-escape")  +  '\n'
                print('parsed  '  +  str(response))

        def  _process_request(self,  request):
                print('process  '  +  str(request))
                