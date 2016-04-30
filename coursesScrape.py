import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import requests

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


# coursesURL = "http://cs.illinois.edu/courses/full-curriculum"
coursesURL = "https://courses.illinois.edu/schedule/2016/fall/CS"
coursesPage = urllib2.urlopen(coursesURL)
coursesSoup = BeautifulSoup(coursesPage, "html.parser")

# print coursesSoup.prettify()
# print coursesSoup.title
# print coursesSoup.title.string

coursesTable = coursesSoup.find('table', {"class":"table table-striped table-bordered table-condensed"})
# print coursesTable
coursesNumList = []
coursesNameList = []
for coursesRow in coursesTable.findAll("tr"):
	coursesCells = coursesRow.findAll("td")
	coursesStates = coursesRow.findAll("a")
	if(len(coursesCells) == 2):
		coursesNumList.append(str(coursesCells[0].find(text = True).strip()))
		coursesNameList.append(str(coursesStates[0].find(text = True).strip()))

# print coursesNumList
# print coursesNameList
coursesDict = dict(zip(coursesNumList, coursesNameList))
# print coursesDict


