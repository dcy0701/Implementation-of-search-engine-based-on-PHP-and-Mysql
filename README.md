# Implementation-of-search-engine-based-on-PHP-and-Mysql
基于PHP和Mysql的站内搜索引擎实现
基于PHP和Mysql的站内搜索引擎实现，
现在的互联网上，很多网站都提供了全文搜索的功能
，通常的做法是通过select查询的like语句来进行搜索，这一办法在搜索时不够准确，以及效率非常低下的缺点。
比如对一个有十几万条记录数据表的TEXT字段进行LIKE操作，可能会花费上近10秒钟左右，
这对网站的浏览者来说是一个非常糟糕的使用体验。
我们使用了MySQL的fulltext功能，
配合中文分词以及词性标注进行索引，同时结合TF-IDF算法进行关键词排序。
