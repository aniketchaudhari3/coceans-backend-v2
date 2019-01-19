#Indeed_Scraper class
#contains all the scraping methods for indeed.com
#Author: Aniket Chaudhari

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
            return jobtitle[0].text, redirected_url[:-1]+''+jobtitle[0]["href"]

        elif len(turns) != 0:

            return turns[0].text, redirected_url[:-1]+''+turns[0]["href"]

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
