# import libs
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import mysql.connector
from mysql.connector import errorcode
from scrapy.crawler import CrawlerProcess


