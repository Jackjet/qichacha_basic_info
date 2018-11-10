# qichacha_basic_info
使用scrapy框架爬取企企网站上公司的基本信息 ** https://www.qichacha.com/ **       
本次通过cookie登录的方式爬取企查查各公司的基本信息，后继还会介绍爬取企查查上各公司的裁判文书信息。     
## 网页链接分析     
 &ensp;&ensp;&ensp;&ensp; 打开企查查的首页，输入要查询的公司名字点击即可看到网页匹配出的相关公司列表，因为查询时给出的是公司的全名，所以一般是在列表中的第一个，程序中通过xpath匹配第一个公司。    
 &ensp;&ensp;&ensp;&ensp; 具体网页链接可通过浏览器或F12中的NETWORK看到。如下图所示：    
![查询页](https://github.com/wei523712/qichacha_basic_info/blob/master/image/%E6%9F%A5%E8%AF%A2%E6%9F%90%E5%85%AC%E5%8F%B8.png)      
           
 &ensp;&ensp;&ensp;&ensp; 查看网页源代码即可看到进入详情页的链接通过xpath提取出来，点击进入要查询的公司即可看到该公司的基本信息，如下图所示：      
![详情1](https://github.com/wei523712/qichacha_basic_info/blob/master/image/%E8%AF%A6%E6%83%85%E9%A1%B51.png)
![详情2](https://github.com/wei523712/qichacha_basic_info/blob/master/image/%E8%AF%A6%E6%83%85%E9%A1%B52.png)             
 &ensp;&ensp;&ensp;&ensp; 点击公司的基本信息，公司的详情主要集中在表格中。该网页链接后会加上“#base”,当然要是不加也可以。     
 ![详情页链接](https://github.com/wei523712/qichacha_basic_info/blob/master/image/%E8%AF%A6%E6%83%85%E9%A1%B5%E9%93%BE%E6%8E%A5.png)
