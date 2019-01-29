# neuvoo_test2.py
# test script for testing neuvoo scraper class
# author Aniket Chaudhari

from souper import *  # souper module
from neuvoo_job import *  # neuvoo job field
import re  # regular expressions
from urllib.parse import urlparse  # urlparser
'''
global vars
'''

# target url
url = 'http://www.neuvoo.co.in/jobs/?'

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
        payload = {
            "k":query,
            "l":location,
            "p":str(page+1)+'0'
        }
    else:
        payload = {
            "k":query,
            "l":location
        }

'''
end global vars
'''

# payload setter
# if page_no != 1:
#     start_offset = (page_no + 1)
#     payload["start"] = str(start_offset)+'0'



class neuvooScraper():
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
        
        scraped = self.get_jobcount()
        # instanciate
        self.jobj = neuvoo_Job(scraped, title, link, employer, address,
                               desc, posted)

    # method get_job
    # returns neuvoo_Job object
    def get_job(self):
        return self.jobj

    # method get_title
    # returns title string
    def get_title(self, jobcard):
        jobtitle = jobcard.findAll("div", {"class": "j-title"})
        link = jobcard.findAll("a", {"class": "gojob"})
        global redirected_url
        if len(jobtitle) != 0:
            return jobtitle[0].text, redirected_url+''+ link[0]["href"]
        else:
            return ''

    # method get_employer
    # returns employer string
    def get_employer(self, jobcard):
        job_employer = jobcard.findAll("div", {"class": "j-empname"})
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
        job_address_div = jobcard.findAll("div", {"class": "j-location"})
        if len(job_address_div) != 0:
            return job_address_div[0].text
        else:
            return ''

    # method get_desc
    # returns description string
    def get_desc(self, jobcard):
        job_desc = jobcard.findAll("div", {"class": "j-snippet"})

        if len(job_desc) != 0:
            return job_desc[0].text.lstrip()
        else:
            return ''

    # method get_posted
    # returns date string
    def get_posted(self, jobcard):
        job_posted = jobcard.findAll("div", {"class": "j-date"})
        if len(job_posted) != 0:
            return job_posted[0].text
        else:
            return ''
    

    # method get_jobcount
    # returns count of scraped jobs int
    def get_jobcount(self):
        global soup
        job_count = soup.findAll("span", {"class": "total-job"})
        if len(job_count) != 0:
            num = re.findall(r'\d+', job_count[0].text)
            if len(num) > 2:
                return str(num[1] + num[2])
            else:
                return str(num[1])
        else:
            return ''
    # end neuvooScraper class

#main scrape method neuvoo.com
def scrape_neuvoo(j_query, j_location, j_page):
    global url,payload,soup,jobCards,redirected_url


    set_payload(j_query, j_location, j_page)

    soup,neuvoo_last_url = Souper(url, payload).get_soup()  # setting initial soup

    set_last_url(neuvoo_last_url)  # setting initial l_url


    # parsing the redirected url

    # jobcard
    jobCards = soup.findAll("div", {"class": "job"})


    # check for an international job
    #url = 'https://www.neuvoo.co.in/jobs?'
    if len(jobCards) == 0:
        # check for international domain link
        other_job = soup.findAll("p", {"class": "oocs"})

        if len(other_job) != 0:
            other_job_link = soup.findAll("p", {"class": "oocs"})[0].find('a')['href']
            url = other_job_link
            soup = Souper(url, payload).get_soup()  # setting initial soup
            # setting initial l_url
            set_last_url(neuvoo_last_url)
            jobCards = soup.findAll("div", {"class": "job"})


    #iteration on jobCards
    job_arr = []
    # json job array; containing json job objects
    json_arr = []

    neuvoo_job_count = 0

    for i in jobCards:
        # populating the job and json arrays
        job_arr.append(neuvooScraper(i).get_job())
        neuvoo_job_count = neuvooScraper(i).get_jobcount()
        json_arr.append(neuvooScraper(i).get_job().get_json())

    #def ret_json_arr():
    return neuvoo_job_count,json_arr

# #calling the main method
#j_count, j_data = scrape_neuvoo("software engineer","delhi india","1")