from flask import Flask, render_template
from reddit_scrape import RedditData as re

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<query>')
def getClass(query="CS+225"):
    data = re(query)
    return render_template("class.html", query=query,data=data)


if __name__ == '__main__':
    app.run()
