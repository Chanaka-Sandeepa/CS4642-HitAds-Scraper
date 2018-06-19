import scrapy
# from scrapy.selector import HtmlXPathSelector


class QuotesSpider(scrapy.Spider):
    name = "HitAds_Spyder"

    def process_text(text):
        text = text.replace('\r', '')
        text = text.replace('\t', '')
        text = text.replace("\n", "")
        text = text.replace("-", "")
        return text

    def process_date(text):
        text = text.replace('Date : ', '')
        return text

    def start_requests(self):

        urls = [
            # 'http://www.hitad.lk/EN/cars',
            'http://www.hitad.lk/EN/vehicle'
        ]
        for i in range (25, 10000, 25):
            domain_url = 'http://www.hitad.lk/EN/vehicle?page='
            new_url = domain_url +str(i)
            urls.append(new_url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for ads in response.css('ul.cat-ads'):
            yield {

                'title': QuotesSpider.process_text(ads.css('h4.fw_b::text').extract_first()),
                'location': QuotesSpider.process_text(ads.css('div.item-facets2 > font.hidden-xs::text').extract_first()),
                'price': ads.css('span.list-price-value::text').extract_first(),
                'date': QuotesSpider.process_date(ads.css('div.ad-info-2::text').extract_first()),
                'type': ads.css('div.item-facets::text')[0].extract(),
                'category': ads.css('div.item-facets::text')[1].extract(),
                'sub category': ads.css('div.item-facets::text')[2].extract(),
                'condition': ads.css('div.item-facets::text')[3].extract(),
                'brand': ads.css('div.item-facets::text')[4].extract(),
                'model': ads.css('div.item-facets::text')[5].extract(),
                'year': ads.css('div.item-facets::text')[6].extract(),
                # for data in ads.css('div.item-facets'):
                #     'type': ads.css('span.list-price-value::text').extract_first(),
            #

            }