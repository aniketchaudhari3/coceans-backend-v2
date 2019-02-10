# indeed_test2.py
# test script for testing indeed scraper class
# author Aniket Chaudhari

from souper import *  # souper module
from indeed_job import *  # indeed job field
import re  # regular expressions
from urllib.parse import urlparse  # urlparser
'''
global vars
'''

# target url
url = 'https://www.indeed.co.in/jobs?'

payload = {}
# page offset no
page_no = 1
# redirected_url
redirected_url = ''
# soup
soup = None
#jobcards
jobCards = []

def set_last_url(lurl):
    parsed_uri = urlparse(lurl)
    global redirected_url
    redirected_url = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)[:-1]

def set_payload(query,location,page):
    global payload
    if page != '1':
        page_offset = int(page) - 1
        payload = {
            "q":query,
            "l":location,
            "start":str(page_offset)+'0'
        }

    else:
        payload = {
            "q":query,
            "l":location
        }

'''
end global vars
'''

# payload setter
# if page_no != 1:
#     start_offset = (page_no + 1)
#     payload["start"] = str(start_offset)+'0'



class IndeedScraper():
    jobj = None
    scraped_jobs = 0

    def __init__(self, jobcard):
        # set attrs
        # set attrs
        title, link = self.get_title(jobcard)
        employer = self.get_employer(jobcard)
        address = self.get_address(jobcard)
        desc = self.get_desc(jobcard)
        posted = self.get_posted(jobcard)
        sponsored = self.get_sponsored(jobcard)
        trusted = self.get_trusted_employer(jobcard)
        rating = self.get_rating(jobcard)
        salary = self.get_salary(jobcard)
        scraped = self.get_jobcount()
        # instanciate
        self.jobj = Indeed_Job(scraped, title, link, employer, address,
                               desc, sponsored, posted, trusted, rating, salary)

    # method get_job
    # returns Indeed_Job object
    def get_job(self):
        return self.jobj

    # method get_title
    # returns title string
    def get_title(self, jobcard):
        jobtitle = jobcard.findAll("a", {"class": "jobtitle"})
        turns = jobcard.findAll("a", {"class": "turnstileLink"})
        global redirected_url
        if len(jobtitle) != 0:
            return jobtitle[0].text, redirected_url+''+jobtitle[0]["href"]

        elif len(turns) != 0:

            return turns[0].text, redirected_url+''+turns[0]["href"]

        else:
            return ''

    # method get_employer
    # returns employer string
    def get_employer(self, jobcard):
        job_employer = jobcard.findAll("span", {"class": "company"})
        if len(job_employer) != 0:
            if '\n' in job_employer:
                return job_employer[0].text.lstrip()
            else:
                return job_employer[0].text.replace('\n', '').lstrip()
        else:
            return ''

    # method get_address
    # returns address string
    def get_address(self, jobcard):
        job_address_div = jobcard.findAll("div", {"class": "location"})
        job_address_span = jobcard.findAll("span", {"class": "location"})
        if len(job_address_div) != 0:
            return job_address_div[0].text
        elif len(job_address_span) != 0:
            return job_address_span[0].text
        else:
            return ''

    # method get_desc
    # returns description string
    def get_desc(self, jobcard):
        job_desc = jobcard.findAll("span", {"class": "summary"})

        if len(job_desc) != 0:
            return job_desc[0].text.lstrip()
        else:
            return ''

    # method get_posted
    # returns date string
    def get_posted(self, jobcard):
        job_posted = jobcard.findAll("span", {"class": "date"})
        if len(job_posted) != 0:
            return job_posted[0].text
        else:
            return ''

    # method get_sponsored
    # returns sponsored bool
    def get_sponsored(self, jobcard):
        job_sponsored = jobcard.findAll("span", {"class": "sponsoredGray"})
        if len(job_sponsored) != 0:
            if 'Sponsored' in job_sponsored[0].text:
                return True
            else:
                return False
        else:
            return False
    # method get_trusted_employer
    # returns trusted employer tick bool

    def get_trusted_employer(self, jobcard):
        job_trust = jobcard.findAll(
            "div", {"class": "serp-ResponsiveEmployer-icon"})
        if len(job_trust) != 0:
            return True
        else:
            return False

    # method get_rating
    # returns ratings float
    def get_rating(self, jobcard):
        job_rating = jobcard.findAll("span", {"class": "rating"})
        if len(job_rating) != 0:
            pxstring = job_rating[0]["style"]
            px = int(re.findall(r'\d+', pxstring)[0])
            return "{:.3f}".format(px / 12) if (px != 0) or (px > 60) else 0
        else:
            return ''

    # method get_salary
    # returns salary int
    def get_salary(self, jobcard):
        job_salary = jobcard.findAll("span", {"class": "salary"})
        if len(job_salary) != 0:
            return job_salary[0].text.lstrip()
        else:
            return ''

    # method get_jobcount
    # returns count of scraped jobs int
    def get_jobcount(self):
        global soup
        job_count = soup.findAll("div", {"id": "searchCount"})
        if len(job_count) != 0:
            num = re.findall(r'\d+', job_count[0].text)
            if len(num) > 2:
                return str(num[1] + num[2])
            else:
                return str(num[1])
        else:
            return ''
    # end IndeedScraper class

#main scrape method Indeed.com
def scrape_indeed(j_query, j_location, j_page):
    global url,payload,soup,jobCards,redirected_url


    set_payload(j_query, j_location, j_page)

    soup,indeed_last_url = Souper(url, payload).get_soup()  # setting initial soup

    set_last_url(indeed_last_url)  # setting initial l_url


    # parsing the redirected url

    # jobcard
    jobCards = soup.findAll("div", {"class": "jobsearch-SerpJobCard"})


    # check for an international job
    #url = 'https://www.indeed.co.in/jobs?'
    if len(jobCards) == 0:
        # check for international domain link
        other_job = soup.findAll("p", {"class": "oocs"})

        if len(other_job) != 0:
            other_job_link = soup.findAll("p", {"class": "oocs"})[0].find('a')['href']
            url = other_job_link
            soup = Souper(url, payload).get_soup()  # setting initial soup
            # setting initial l_url
            set_last_url(indeed_last_url)
            jobCards = soup.findAll("div", {"class": "jobsearch-SerpJobCard"})


    #iteration on jobCards
    job_arr = []
    # json job array; containing json job objects
    json_arr = []

    indeed_job_count = 0

    for i in jobCards:
        # populating the job and json arrays
        job_obj = IndeedScraper(i)
        job_arr.append(job_obj.get_job())
        indeed_job_count = job_obj.get_jobcount()
        json_arr.append(job_obj.get_job().get_json())

    #def ret_json_arr():
    return indeed_job_count,json_arr

# #calling the main method
# j_count, j_data = scrape_indeed("software engineer","delhi india","1")

