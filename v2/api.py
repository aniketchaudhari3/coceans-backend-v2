from flask import *
from collector import *

app = Flask(__name__)

#index
@app.route('/')
def index():
    return 'Access Restriced! '


#api endpoint
@app.route('/api', methods=['GET'])
def api():
    job_query = request.args.get('q')
    job_location = request.args.get('l')
    job_page = request.args.get('page')
    return jsonify(get_job_dataset(job_query, job_location,job_page))


#honeypot
@app.route('/phpmyadmin')
def pma():
    with open('honeylog.txt','a') as honeylog:
        data = 'IP: '+ request.remote_addr+'\n'
        honeylog.write(data)
    return 'Redirecting to PhpMyAdmin'

app.run(host='0.0.0.0',port='80')

