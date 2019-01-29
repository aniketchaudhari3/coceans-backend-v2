import json
#job class
class neuvoo_Job():
    title = ''
    link = ''
    employer = ''
    address = ''
    description = ''
    dateposted = ''
    scraped_job = ''

    def __init__(self, scraped='',title='',link='', employer='', address='', description='', dateposted=''):
        self.scraped_job = scraped
        self.title = title
        self.link = link
        self.employer = employer
        self.address = address
        self.description = description
        self.dateposted = dateposted

    def print_job(self):
        print("title: ",self.title)
        print("employer: ",self.employer)
        print("address: ",self.address)
        print("description: ",self.description)
        print("date posted: ",self.dateposted)
        print("-------------------------------")
    
    def get_json(self):
        return json.dumps({
        "title" : self.title,
        "link":self.link,
        "employer" : self.employer,
        "address" : self.address,
        "description" : self.description,
        "dateposted" : self.dateposted
    })



#--------------------------------------------------------------------------------
#temp functions