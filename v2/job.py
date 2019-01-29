#job class
class Job():
    title = ''
    employer = ''
    address = ''
    description = ''
    sponsored = False
    dateposted = ''
    trusted = False

    def __init__(self, title='', employer='', address='', description='', sponsored=False, dateposted='', trusted=False):
        self.title = title
        self.employer = employer
        self.address = address
        self.description = description
        self.sponsored = sponsored
        self.dateposted = dateposted
        self.trusted = trusted
    
    def print_job(self):
        print("title: ",self.title)
        print("employer: ",self.employer)
        print("address: ",self.address)
        print("description: ",self.description)
        print("sponsored: ",self.sponsored)
        print("date posted: ",self.dateposted)
        print("trusted: ",self.trusted)
        print("-------------------------------")