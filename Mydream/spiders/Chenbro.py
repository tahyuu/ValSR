# -*- coding: utf-8 -*-
import scrapy
from Mydream.items import MydreamItem 
from scrapy.linkextractors import LinkExtractor


class ChenbroSpider(scrapy.Spider):
    name = 'Chenbro'
    allowed_domains = ['http://www.chenbro.com/zh-CN']
    start_urls = ['http://www.chenbro.com/en-US/products/BareboneServer/1U_BBServer/1',
		  'http://www.chenbro.com/en-US/products/BareboneServer/2U_Bbserver/1',]
    pagelink = LinkExtractor(allow=("start=\d+"))
    response.xpath('//a[contains(@href, "product")]/@href').extract()


    def parse(self, response):
	p_dic= dict()
	p_item_names=response.xpath('//table[re:test(@id, "spec_table")]//td[1]//text()').extract()
	p_item_contents=response.xpath('//table[re:test(@id, "spec_table")]//td[2]').re("\>[\s\S]+\<")
	i=0
	for p_item_name in p_item_names:
		p_dic[p_item_name.strip().replace(" ","_").replace("/","_").replace("(","").replace(")","")]=p_item_contents[i].replace(">","").replace("<","").strip()
		i=i+1
	#for (k,v) in p_dic.items():
	#	print "%s:%s" %(k.rjust(30),v.ljust(30))
	
	product=MydreamItem(p_dic)
	print product
	
        #for sel in response.xpath('//ul/li'):
        #    title = sel.xpath('a/text()').extract()
        #    link = sel.xpath('a/@href').extract()
        #    desc = sel.xpath('text()').extract()
        #    print title, link, desc
	return product
