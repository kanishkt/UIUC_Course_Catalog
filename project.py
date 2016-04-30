from flask import Flask, render_template
from reddit_scrape import RedditData as re
import coursesScrape as cs
from mainScraper import koofers as koof

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<query>')
def getClass(query="CS+225"):
    data = re(query)
    dict = cs.coursesDict
    for x in dict:
        if x == query:
            str = x[3:]
            str2 = dict[x].replace(" ","-")
            str3 = str+"-"+str2
            profs, stats = koof(str3)
            print profs
            print stats
            break
    return render_template("class.html", query=query,data=data, profs=profs, stats=stats)


if __name__ == '__main__':
    app.run()
