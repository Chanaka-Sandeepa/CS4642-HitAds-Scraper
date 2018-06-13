import scrapy
# from scrapy.selector import HtmlXPathSelector


class QuotesSpider(scrapy.Spider):
    name = "HitAds_Spyder"

    def start_requests(self):
        urls = [
            # 'http://www.trc.gov.lk/2014-05-13-13-23-17/events/755-15th-apt-telecommunication-ict-development-forum.html',
            # 'http://www.trc.gov.lk/world-telecommunication-information-society-day-2018.html',
            # 'http://www.trc.gov.lk/notice-to-cable-tv-and-direct-to-home-satellite-tv-service-providers.html',
            # 'http://www.trc.gov.lk/mr-p-r-s-p-jayathilake-is-the-new-director-general-of-trcsl.html',
            # 'http://www.trc.gov.lk/2014-05-13-13-23-17/events/662-his-excellency-the-president-of-sri-lanka-graced-the-17th-apt-policy-and-regulatory-forum.html',
            # 'http://www.trc.gov.lk/nisadiya.html',
            # 'http://www.trc.gov.lk/2014-05-13-03-46-49/right-to-information.html',
            # 'http://www.trc.gov.lk/spectrum-management/spectrum-management-in-sri-lanka.html',
            # 'http://www.trc.gov.lk/2014-08-13-11-31-28/numbering.html',
            # 'http://www.trc.gov.lk/2014-08-13-11-31-28/network-equipment/import-clearance.html',
            # 'http://www.trc.gov.lk/2014-08-13-11-31-28/guidelines.html',
            # 'http://www.trc.gov.lk/2014-05-12-12-36-13/system-licence/licensing-procedure-issuance-renewal.html',
            # 'http://www.trc.gov.lk/2014-05-12-12-36-13/system-licence/licenced-operator-list.html',
            # 'http://www.trc.gov.lk/2014-05-12-12-36-13/system-licence/public-notice-on-issuence-renewal-modification-of-licences.html',
            # 'http://www.trc.gov.lk/2014-05-12-12-36-13/system-licence/public-consultation.html',
            # 'http://www.trc.gov.lk/2014-05-12-12-36-13/frequency-licence.html',
            # 'http://www.trc.gov.lk/2014-05-12-12-36-13/2014-05-12-13-18-07/list-of-licenced-vendors.html',
            # 'http://www.trc.gov.lk/2014-05-12-12-36-13/2014-05-12-13-18-07/vendor-licence-procedure.html',
            # 'http://www.trc.gov.lk/2014-05-12-13-20-23/tariff-regulation.html',
            # 'http://www.trc.gov.lk/2014-05-12-13-20-23/telco-levies.html',
            'http://www.hitad.lk/EN/cars',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {

            'title': response.css('h4.fw_b::text').extract(),
            'location': response.css('div.item-facets2 > font.hidden-xs::text').extract(),
            'price': response.css('span.list-price-value::text').extract(),
        }