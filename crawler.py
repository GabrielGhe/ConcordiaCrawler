import requests
from bs4 import BeautifulSoup

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
            print( "{} {}".format(link.text, link_href) )
crawl()


def ratemyprof():
    # used to find the professors at concordia with the prefix
    ratemyprofessor = ("http://search.mtvnservices.com/typeahead/suggest/?solrformat=true"
                       "&rows=10&callback=noCB&prefix=")
    ratemyprofessor += "aiman"
    ratemyprofessor += ("&qf=teacherfullname_t%5E1000+teacherfullname_autosuggest"
                        "&bf=pow(total_number_of_ratings_i%2C2.1)&defType=edismax&siteName=rmp"
                        "&group=off&group.field=content_type_s&group.limit=20"
                        "&fq=content_type_s%3ATEACHER&fq=schoolid_s%3A1422"
                        "&fq=schoolname_t%3A%22Concordia+University%22&fq=schoolid_s%3A1422")

    # go to the professor's page
    prof_page = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid="