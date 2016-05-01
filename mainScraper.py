__author__ = 'Navya'
#rate my prof

from bs4 import BeautifulSoup
import urllib
import requests

import mechanize
from bs4 import BeautifulSoup
#import urllib2
#import json
#import re

#---login

import cookielib

def koofers(college, className):
    cj = cookielib.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    br.addheaders = [('User-agent', 'Chrome')]

    br.open("https://www.koofers.com/login")

    br.select_form(nr=0)
    br.form['email'] = 'sheivingoyal@gmail.com'
    br.form['password'] = 'abhisucks'
    br.submit()

    #print br.response().read()

    #---

    professors = {}
    stats = {}
    grades = {}

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

        data = c.find_all("div", style = "margin-left:4px;margin-bottom:4px;")
        for d in data:
            script = d.find_all("script", type = "text/javascript")
            script = str(script)
            script = [i.strip() for i in script.split("\\n")]

            numGrades = 5
            letters = []
            dataIndex = 0
            for i in range(len(script)):
                if(script[i].find("categories")!=-1):
                    letters = eval(script[i].split(":")[1][1:-1])
                    numGrades = len(letters)

                if(script[i].find("data:")!=-1):
                    script[i] = script[i].split(":")[1]

                    dataIndex = i
                    break

            gradeDict = ""
            for i in xrange(dataIndex+1, dataIndex+numGrades+1):
                gradeDict += script[i].replace("{", "[").replace("}", "]").replace("y:", "").replace("color:", "")
            gradeDict = eval(gradeDict)
            for i in range(len(gradeDict)):
                grades[letters[i]] = gradeDict[i][0]

            #print(script)

    #print(stats)
    #print ""
    #print(grades)
    #print ""

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
            professors[name[0]] = [gpa[0]]

        for n in nameTag:
            links = n.find_all('a', href=True)
            for l in links:
                professors[name[0]].append('https://www.koofers.com'+l['href'])
                #link = 'https://www.koofers.com'+l['href']
                #linkSoup = BeautifulSoup(urllib.urlopen(link).read(), "html.parser")
                #reviewData = soup.find_all("div", class_ = "right")
                #print(linkSoup.prettify())

    #print(professors)
    #for i in professors:
     #   print professors[i][0]

    return stats, grades, professors

def main():
    college = 'cs'
    className = '225-data-structures'
    #className = '466-introduction-to-bioinformatics'
    #className = "241-system-programming"

    stats, grades, professors = koofers(college, className)
    print(stats)
    print(grades)
    print(professors)


if __name__ == "__main__":
    main()