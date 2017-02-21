google-speedtest-chart
======================

Simple Python script to push speedtest results (using `speedtest-cli`) to a Google Docs spreadsheet. I use this to measure and track my upload and download bandwith:

![](http://up.frd.mn/xRiew.png)

You can find an interactive demo (actually productive) version of the chart here: https://docs.google.com/spreadsheets/d/1QvV6POBVBXuq5iXSOLNd5bwgd5To8FMuvsrSfvY7Nuk/pubchart?oid=1973311741&format=interactive

### Requirements

* Python 3.6
* [`speedtest-cli`](https://github.com/sivel/speedtest-cli)
* Google account

### Installation and usage

**NOTE**
I edited this to fit a friends request

1. Clone and open repository:  
  `git clone https://github.com/Beachman4/google-speedtest-chart && cd google-speedtest-chart`
1. Install dependencies:  
  `pip install speedtest-cli cymysql sqlalchemy`
1. Insert the SQL in the file table.sql

1. Symlink it into your $PATH:
   `ln -s speedtest.py /usr/local/bin/speedtest`
1. Copy default config and adjust it:  
  `cp default.config.json config.json`
1. Run the script:  
  `$ speedtest`

### License

[MIT](LICENSE)

### Version

1.3.1
