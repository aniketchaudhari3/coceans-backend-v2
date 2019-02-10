from indeed_test3 import *
from neuvoo_test1 import *

#query = input("Enter job title: ")
#location = input("Enter job location: ")
#page_offset = input("Enter page no: ")

#indeed_dataset
total_job_count = 0
#temp_job_dataset = []

job_dataset = []

def get_job_dataset(c_query, c_location, c_page_offset):
    global total_job_count,job_dataset
    total_job_count = 0
    job_dataset.clear()
    #indeed.com collector
    indeed_j_count, indeed_job_dataset  = scrape_indeed(c_query, c_location, c_page_offset)
    job_dataset.append(indeed_job_dataset)
    total_job_count = total_job_count + int(indeed_j_count)
    

    #neuvoo.co.in collector
    neuvoo_j_count, neuvoo_job_dataset = scrape_neuvoo(c_query, c_location, c_page_offset)
    job_dataset.append(neuvoo_job_dataset)
    total_job_count = total_job_count + int(neuvoo_j_count)
    
    print("Total jobs: ",len(neuvoo_job_dataset)+len(indeed_job_dataset))
    return job_dataset


#get_job_dataset(query, location, page_offset)
print(total_job_count)
#print(job_dataset)

