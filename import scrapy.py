import scrapy
class MasukSpider(scrapy.Spider):
    name = "masuk"
    start_urls = ['https://academy.babastudio.com/login']
    username = 'email'
    sandi = 'passwrod'
    url_stars = 'https://academy.babastudio.com/social-learning-my-course'
    def parse(self, response):
        formdataanda = {
            'login': self.username,
            'password': self.sandi
        }
        return scrapy.http.FormRequest.from_response(response, formdata = formdataanda, callback = self.scrape_page)
    def scrape_page(self, response):
        yield scrapy.Request(url = self.url_stars, callback = self.stars)        
    def stars(self, response):
        for repo in response.xpath('//div[contains(@class, "d-inline-block mb-1")]/h3/a/text()'):
            print(repo.get())