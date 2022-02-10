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

