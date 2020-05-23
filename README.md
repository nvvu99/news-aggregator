# News Aggregator web app
-------------------
* This project used Django and Scrapy to create a News Aggregator web app
* Database used: MySQL

### Screenshot
[![alt text](https://github.com/nvvu99/news-aggregator/blob/master/screenshot.png "screenshot")]

### Features
* User authentication features
* Add news topic for following
* Organize follwoing topic
* Save article for read later
* News web scraping (in folder NewsScraper)

### Run this project
* Clone this project: `git clone https://github.com/nvvu99/news-aggregator.git`
* Create a database in MySQL using command: `create database news character set utf8`
* Open the file my.cnf an change the user, password respectively to your database
> [client]
> #protocol = tcp
> host = localhost
> database = news
> user = prod
> password = 0000
> default-character-set = utf8
* `cd` into `NewsAggregator`: `cd news-aggregator`
* (Optional)Install python virtual environment:
```
virtualenv venv
source ./venv/bin/activate
```
* Install required libraries: `pip install -r requirements.txt`
* Initial the database:
```
python manage.py migrate
python manage.py loaddata initial_data.json
```
* `cd` into `NewsSraper`: `cd NewsScraper`
* Scrape the articles data: `scrapy crawl`
* `cd ..`
* Run webserver: `python manage.py runserver`
* Open your browser and go to [http://localhost:8000](http://localhost:8000)

### The NewsScraper module
The articles scraped from following source:
* [baotintuc.vn](https://baotintuc.vn)
* [thoidai.com.vn](https://thoidai.vom.vn)
* [phapluatxahoi.vn](https://phapluatxahoi.vn)
* [tapchimattran.vn](https://tapchimattran.vn)
* [vov.vn](https://vpv.vn)
* [tienphong.vn](https://tienphong.vn)
* [vanhien.vn](http://vanhien.vn)
* [nhandan.com.vn](https://nhandan.com.vn)
* [laodongthudo.vn](https://laodongthudo.vn)
* [nghenhinvietnam.vn](https://nghenhinvietnam.vn)
* [vietnamnet.vn](https://vietnamnet.vn)
* [doanhnghiepvn.vn](https://doanhnghiepvn.vn)
* [kienthuc.net.vn](https://kienthuc.net.vn)
* [vietnamplus.vn](https://vietnamplus.vn)
* [plo.vn](https://plo.vn)