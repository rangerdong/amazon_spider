# Amazon Product Review & Ranking Spider
---

亚马逊商品抓取程序，目前主要包含四个主要spider，在spider目录下.

*	`profile_spider.py`	- 	商品评价主要信息抓取spider， 主要抓取商品评价总数，各分级评论占比，商品名称，图片等信息

* `detail_spider.py` - 商品评价列表抓取spider， 抓取 *三星以下* 并且 *在近期40天内* 的评价

* `sales_ranking.py` - 商品大目录排名抓取spider，抓取商品在某个大目录下的排名

* `keyword_spider.py` - 商品关键字信息排名抓取spider， 抓取某个商品在特定关键字搜索下的排名

操作数据库的信息放在sql.py下，主要对抓取的信息进入写库操作

项目环境：

 * `python3.6.2`
 * `scrapy 1.4.0`
 * `pymysql`
 * `mysql5.7.18`

启动爬虫

	cd amazon_spider
	scrapy crawl profile -a asin=***  # 爬取评价主要信息
	scrapy crawl detail -a asin=*** {-a daily=1}  # 爬取商品近40天内三星以下的评论列表，其中daily参数表示每日更新
	scrapy crawl sales_ranking  # 爬取 salesrankings表中所有的商品 大目录排名变动并记录 
	scrapy crawl keyword_ranking  # 爬取 salesranking_keywords 表中所有的关键字排名变动并记录 其中关键字列表页数最大20页，每页16条数据，总的排名在320以内，若无数据，则为321 
	
数据表文件在tablesqls文件夹中

### ！注意
	使用本项目进行商品大目录与关键字排名，需要自行将sales_rankings与keyword_rankings表中写入数据
	其中sales_ranking 中的sid健 可随意填写，可结合自身项目的用户表作关联



