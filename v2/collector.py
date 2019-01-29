from indeed_test3 import *
from neuvoo_test1 import *

query = input("Enter job title: ")
location = input("Enter job location: ")
page_offset = input("Enter page no: ")

#indeed_dataset
total_job_count = 0
job_dataset = []




def get_job_dataset(c_query, c_location, c_page_offset):
    global total_job_count,job_dataset

    #indeed.com collector
    indeed_j_count, indeed_job_dataset  = scrape_indeed(c_query, c_location, c_page_offset)
    job_dataset.append(indeed_job_dataset)
    total_job_count = total_job_count + int(indeed_j_count)

    #neuvoo.co.in collector
    neuvoo_j_count, neuvoo_job_dataset = scrape_neuvoo(c_query, c_location, c_page_offset)
    job_dataset.append(neuvoo_job_dataset)
    total_job_count = total_job_count + int(neuvoo_j_count)

    return job_dataset

get_job_dataset(query, location, page_offset)

print(job_dataset)