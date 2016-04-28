__author__ = 'Navya'
#rate my prof

from bs4 import BeautifulSoup
import urllib
import requests

def koofers(class_):
    college = 'cs'
    className = class_#'225-data-structures'

    professors = {}
    stats = {}
    url = 'https://www.koofers.com/university-of-illinois-urbana-champaign-uiuc/' + college + '/' + className
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    #print(soup.prettify())
    content = soup.find_all("div", class_="blue_container")

    for c in content:
        data = c.find_all("div", style = "margin-bottom:10px;")
        piece = [piece.text for piece in data]

        i = 0
        for p in piece:
            if i == 3: break

            p = p.strip()
            p = p.replace("\n                \n\n\n                    ", " : ")
            p = p.split(":")
            stats[p[0]] = p[1]

            i+=1

    print(stats)
    print ""

    url = 'https://www.koofers.com/university-of-illinois-urbana-champaign-uiuc/' + college + '/' + className + '/professors'
    r = urllib.urlopen(url).read()
    soup = BeautifulSoup(r, "html.parser")
    #print(soup.prettify())
    content = soup.find_all("div", class_="content")

    for c in content:
        nameTag = c.find_all("div", class_="title")
        name = [name.text for name in nameTag]
        #if(len(name) > 0):
        #    print(name[0])

        gpaTag = c.find_all("span", class_="value")
        gpa = [gpa.text for gpa in gpaTag]
        if(len(gpa) > 0) and (len(name) > 0):
            professors[name[0]] = gpa[0]

    print professors
    return professors, stats
