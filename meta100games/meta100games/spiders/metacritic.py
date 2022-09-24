import scrapy


class MetacriticSpider(scrapy.Spider):
    name = 'metacritic'
    start_urls = ['https://www.metacritic.com/browse/games/score/metascore/all/all/filtered']

    def parse(self, response):
        for game in response.css('.clamp-summary-wrap'):
            yield{
                'Title':game.css('.title h3::text').get(),
                'Platform': game.css('.platform .data::text').get(),
                'Metascore': game.css('.clamp-metascore .positive::text').get(),
                'User Score': game.css('.user::text').get()
            }
            
