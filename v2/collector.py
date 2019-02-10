
from indeed_test3 import *
from neuvoo_test2 import *
import threading
import time

#query = input("Enter job title: ")
#location = input("Enter job location: ")
#page_offset = input("Enter page no: ")

#indeed_dataset
total_job_count = 0
#temp_job_dataset = []

job_dataset = []

def get_job_dataset(c_query, c_location, c_page_offset):
    global total_job_count,job_dataset
    start_time = time.time()
    total_job_count = 0
    job_dataset.clear()
    #indeed.com collector
    def thread_indeed():
        global total_job_count, job_dataset
        indeed_j_count, indeed_job_dataset  = scrape_indeed(c_query, c_location, c_page_offset)
        job_dataset = job_dataset + indeed_job_dataset
        total_job_count = total_job_count + int(indeed_j_count)
    

    #neuvoo.co.in collector
    def thread_neuvoo():
        global total_job_count, job_dataset
        neuvoo_j_count, neuvoo_job_dataset = scrape_neuvoo(c_query, c_location, c_page_offset)
        job_dataset = job_dataset + neuvoo_job_dataset
        total_job_count = total_job_count + int(neuvoo_j_count)
    
    t1 = threading.Thread(target = thread_indeed )
    t2 = threading.Thread(target = thread_neuvoo )
   
    t1.start()
    t2.start()
    t1.join()
    t2.join()

 
    end_time = time.time()
    print("Time: ", (end_time - start_time))
    #print("Total jobs: ",len(neuvoo_job_dataset)+len(indeed_job_dataset))
    return job_dataset


#get_job_dataset(query, location, page_offset)
#print(job_dataset)

