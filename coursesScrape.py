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
coursesSoup = BeautifulSoup(coursesPage)

print coursesSoup.prettify()
print coursesSoup.title
print coursesSoup.title.string

coursesTable = coursesSoup.find('table', {"class":"table table-striped table-bordered table-condensed"})
print coursesTable
coursesNumList = []
coursesNameList = []
for coursesRow in coursesTable.findAll("tr"):
	coursesCells = coursesRow.findAll("td")
	coursesStates = coursesRow.findAll("a")
	if(len(coursesCells) == 2):
		coursesNumList.append(str(coursesCells[0].find(text = True).strip()))
		coursesNameList.append(str(coursesStates[0].find(text = True).strip()))

print coursesNumList
print coursesNameList


# coursesAllLinks = coursesSoup.find_all("a")
# for coursesLink in coursesAllLinks:
# 	print coursesLink.get("href")
# counter = 0
# extCourseRubric
# extCourseTitle
# externalCourseRubric = coursesSoup.find_all("div", class_="extCourseData")
# print externalCourseRubric
# for courseNames in externalCourseRubric:
# 	print "HERE"
# 	print courseNames

# coursesURL = urllib2.open('http://cs.illinois.edu/courses/full-curriculum').read()
# coursesSoup = BeautifulSoup(coursesURL)
# print type(coursesSoup)


# def make_soup(url):
# 	html = urlopen(url).read()
# 	return BeautifulSoup(html, "lxml")

# def get_category_links(section_url):
# 	soup = make_soup(section_url)
# 	boccat = soup.find("dl", "boccat")
# 	category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
# 	return category_links

# rawCourseURL = raw_input(coursesURL)
# print rawCourseURL
# courseRequest = requests.get("http://" + rawCourseURL)
# coursesData = courseRequest.text()
# coursesSoup = BeautifulSoup(data)
# for link in coursesSoup.findAll('u'):
# 	print(link.get('href'))
