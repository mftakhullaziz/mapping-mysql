# import libs
from msilib.schema import Error
from traceback import print_tb
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import mysql.connector as connections
from mysql.connector import errorcode
from scrapy.crawler import CrawlerProcess

# create connection to mysql  db
try:

    mysql_db = connections.connect(
        host="localhost",
        user="root",
        password="",
        database="scrapping_py"
    )
    cursor = mysql_db.cursor(buffered=True)
    print("Connected Success")

except connections.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Username or Password is wrong!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not found")
    else:
        print(err)

class Scrap_(CrawlSpider):

	name = 'test1'	
	allowed_domains = ['books.toscrape.com']
	start_urls = ['http://books.toscrape.com/']
	headers = {
                'user-agent' : "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"
				}
	rules = (Rule(LinkExtractor(allow=()), callback='parse_item', follow=True),)
		
	def parse_item(self, response): 
		wsearch = ['travel','music','art','history']
		lstitle = []
		x = response.url
		
		booktitle = str(x)	
		booktitle = booktitle.split("/")[4]
		booktitle = booktitle.split("_")[0]
		
		[lstitle.append(i) for i in booktitle.split("-")]
		
		check =  any(item in wsearch for item in lstitle)
		
		if check is True:

			myquery = """INSERT INTO books (urls,books)
			values(%s,%s)
			"""
			val=(x,booktitle)
			cursor.execute(myquery,val)
			mysql_db.commit()
			
		else:
			pass	

if __name__ == "__main__":
	process = CrawlerProcess()
	process.crawl(Scrap_)
	process.start()
	cursor.close()
	mysql_db.close()

