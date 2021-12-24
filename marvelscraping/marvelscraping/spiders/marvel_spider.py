import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# We use CrawlSpider instead of Spider so that we can make use of Rules and Link Extractors.
class CharacterSpider(CrawlSpider):
    name = "characters"
    start_urls = ["https://marvel.fandom.com/wiki/Category:Characters"]

    # The first rule extracts the link for the next page. Everything that will be done with the first url will then be done
    # with this next link, including finding the link for the next page, essentially allowing us to crawl through all pages.
    # The second rule extracts the links for all characters (obtained through CSS selector). All of these links will then
    # be subjected to the function parse_item. Think of parse_item as the "regular parse" whose start_urls list equals
    # all the links extracted from the second rule.

    rules = (
            Rule(LinkExtractor(restrict_css=(".category-page__pagination-next", ))),
            Rule(LinkExtractor(restrict_css=(".category-page__first-char+ .category-page__members-for-char .category-page__member", ), deny=("Category:")), 
                callback="parse_item") 
            )

    def parse_item(self, response):
        name = response.css("#firstHeading::text").get().replace("\n\t\t\t\t\t","").replace("\t\t\t\t","")
        gender = response.css("[data-source=Gender]").css("a::text").get()
        marital_status = response.css("[data-source=MaritalStatus]").css("a::text").get()
        try:
            height_in_meters = float(response.css("[data-source=Height]").css("a::text").get().split("(")[-1][:-3])
        except:
            height_in_meters = None
        try:
            weight_in_kg = float(response.css("[data-source=Weight]").css("a::text").get().split("(")[-1][:-4])
        except: 
            weight_in_kg = None
        eye_color = response.css("[data-source=Eyes]").css("a::text").get()
        try:
            hair_color = response.css("[data-source=Hair]").css("a::text").getall()[-1]
        except:
            hair_color = None
        living_status = response.css("[data-source=Status]").css("a::text").get()
        reality = response.css("[data-source=Reality]").css("a::text").get()
        birth_place = response.css("[data-source=PlaceOfBirth]").css("a::text").get()
        identity = response.css("[data-source=Identity]").css("a::text").get()
        citizenship = response.css("[data-source=Citizenship]").css("a::text").get()
        try:
            first_appearance = response.css("[data-source=First]").css("a::text").getall()[-1]
        except:
            first_appearance = None
        try:
            num_appearances = int(response.css("[href*=Appearances]::text").get().split()[0])
        except:
            num_appearances = None
        
        yield {
            "Name" : name,
            "Gender" : gender,
            "Marital_Status" : marital_status,
            "Height" : height_in_meters,
            "Weight" : weight_in_kg,
            "Eye_Color" : eye_color,
            "Hair_Color" : hair_color,
            "Living_Status" : living_status,
            "Reality" : reality,
            "Birthplace" : birth_place,
            "Identity" : identity,
            "Citizenship" : citizenship,
            "First_Appearance" : first_appearance,
            "Appearances" : num_appearances
        }

        # run scrapy crawl characters -o characters.csv on the marvelscraping folder