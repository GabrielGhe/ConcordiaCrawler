import requests, json
from bs4 import BeautifulSoup

# --------------------------------------------------------
# Go get all the course information
def crawl():
    url = "http://aits.encs.concordia.ca/oldsite/resources/schedules/courses/?y=2014&s=2"
    source = requests.get(url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text)

    # get all the links
    for link in soup.findAll('a'):
        link_href = link.get('href')

        # only if the link is for a class do we display it
        if link_href.startswith('details'):
            link_href = "http://aits.encs.concordia.ca/oldsite/resources/schedules/courses/" + link_href
            crawl_class(link_href)


# --------------------------------------------------------
# Go get info for 1 course
def crawl_class(class_url):
    # init
    source = requests.get(class_url)
    plain_text = source.text
    soup = BeautifulSoup(plain_text)

    # title
    course_title = soup.findAll('h1')[0].text
    print course_title

    # sections with teachers
    rows = soup.findAll('table', { 'class': 'table_1'})[1].find('tbody').findAll('tr')
    for row in rows:
        for column in row.find_all('td'):
            print column.text
    print ""
    


# --------------------------------------------------------
# Get information about a professor from rate my professor
def ratemyprof(prof = ""):
    # used to find the professors at concordia with the prefix
    professor_url = ("http://search.mtvnservices.com/typeahead/suggest/?solrformat=true"
                       "&rows=10&callback=noCB&prefix=")
    professor_url += prof
    professor_url += ("&qf=teacherfullname_t%5E1000+teacherfullname_autosuggest"
                        "&bf=pow(total_number_of_ratings_i%2C2.1)&defType=edismax&siteName=rmp"
                        "&group=off&group.field=content_type_s&group.limit=20"
                        "&fq=content_type_s%3ATEACHER&fq=schoolid_s%3A1422"
                        "&fq=schoolname_t%3A%22Concordia+University%22&fq=schoolid_s%3A1422")

    # go to the professor's page
    prof_page = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid="
    resp = requests.get(professor_url)
    data = json.loads(resp.text[5:-2])
    first_match = data["response"]["docs"][0]["pk_id"]


#crawl()
ratemyprof("aiman+hanna")