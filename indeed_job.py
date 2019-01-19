import json
#job class
class Indeed_Job():
    title = ''
    link = ''
    employer = ''
    address = ''
    description = ''
    sponsored = False
    dateposted = ''
    trusted = False
    salary = ''
    rating = ''
    scraped_job = ''

    def __init__(self, scraped='',title='',link='', employer='', address='', description='', sponsored=False, dateposted='', trusted=False,rating='',salary=''):
        self.scraped_job = scraped
        self.title = title
        self.link = link
        self.employer = employer
        self.address = address
        self.description = description
        self.sponsored = sponsored
        self.dateposted = dateposted
        self.trusted = trusted
        self.rating = rating
        self.salary = salary

    def print_job(self):
        print("title: ",self.title)
        print("employer: ",self.employer)
        print("address: ",self.address)
        print("description: ",self.description)
        print("sponsored: ",self.sponsored)
        print("date posted: ",self.dateposted)
        print("trusted: ",self.trusted)
        print("rating: ",self.rating)
        print("salary: ",self.salary)
        print("-------------------------------")
    
    def get_json(self):
        return json.dumps({
        "title" : self.title,
        "link":self.link,
        "employer" : self.employer,
        "address" : self.address,
        "description" : self.description,
        "sponsored" : self.sponsored,
        "dateposted" : self.dateposted,
        "trusted" : self.trusted,
        "rating":self.rating,
        "salary":self.salary
    })



#--------------------------------------------------------------------------------
#temp functions