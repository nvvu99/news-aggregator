# News Aggregator web app

- This project used Django and Scrapy to create a News Aggregator web app
- Database used: MySQL

### Screenshot

![alt text](https://github.com/nvvu99/news-aggregator/blob/master/screenshot.png "screenshot")

### Features

- User authentication features
- Add news topic for following
- Organize following topic
- Save article for read later
- News web scraping (in folder NewsScraper)

### Run this project

- Clone this project:

```console
[niar@niar niar] git clone https://github.com/nvvu99/news-aggregator.git
```

- Create a database in MySQL using command: `create database news character set utf8`
- Open the file `my.cnf` an change the user, password respectively to your database
```
[client]
#protocol = tcp
host = localhost
database = news
user = prod
password = 0000
default-character-set = utf8
```

- Run the following commands

```
[niar@niar niar] cd news-aggregator
[niar@niar news-aggregator]
[niar@niar news-aggregator] virtualenv venv
[niar@niar news-aggregator] source ./venv/bin/activate
(venv) [niar@niar news-aggregator] pip install -r requirements.txt
(venv) [niar@niar news-aggregator] python manage.py migrate
(venv) [niar@niar news-aggregator] python manage.py loaddata initial_data.json
(venv) [niar@niar news-aggregator] cd NewsScraper
(venv) [niar@niar NewsScraper] scrapy crawl
(venv) [niar@niar NewsScraper] cd ..
(venv) [niar@niar news-aggregator] python manage.py runserver
```

- Open your browser and go to [http://localhost:8000/news](http://localhost:8000/news)

### The NewsScraper module

The articles scraped from following source:

- [baotintuc.vn](https://baotintuc.vn)
- [thoidai.com.vn](https://thoidai.com.vn)
- [phapluatxahoi.vn](https://phapluatxahoi.vn)
- [tapchimattran.vn](http://tapchimattran.vn)
- [vov.vn](https://vov.vn)
- [tienphong.vn](https://tienphong.vn)
- [vanhien.vn](http://vanhien.vn)
- [nhandan.com.vn](https://nhandan.com.vn)
- [laodongthudo.vn](http://laodongthudo.vn)
- [nghenhinvietnam.vn](https://nghenhinvietnam.vn)
- [vietnamnet.vn](https://vietnamnet.vn)
- [doanhnghiepvn.vn](https://doanhnghiepvn.vn)
- [kienthuc.net.vn](https://kienthuc.net.vn)
- [vietnamplus.vn](https://vietnamplus.vn)
- [plo.vn](https://plo.vn)
