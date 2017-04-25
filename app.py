from flask import Flask, render_template
from bs4 import BeautifulSoup as bs
from urllib import request as req

app = Flask(__name__)
app.secret_key = 'bdkhfbkjafasdfnjkashdf'

@app.route('/')
@app.route('/englishnews')
def englishnews():
	r = req.urlopen('http://timesofindia.indiatimes.com/rssfeedstopstories.cms')
	soup = bs(r, 'xml')

	news = soup.find_all('description')
	headlines = soup.find_all('title')
	return render_template('englishnews.html', news=news, headlines=headlines)

@app.route('/hindinews')
def hindinews():
	r = req.urlopen('http://rss.jagran.com/rss/news/national.xml')
	soup = bs(r, 'xml')

	news = soup.find_all('description')
	headlines = soup.find_all('title')
	# news.img.decompose()
	return render_template('hindinews.html', news=news, headlines=headlines)


if __name__ == "__main__":
	app.run(debug=True)
