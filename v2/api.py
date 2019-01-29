from flask import *
from collector import *

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    job_query = request.args.get('q')
    job_location = request.args.get('l')
    job_page = request.args.get('page')
    return jsonify(str(get_job_dataset(job_query, job_location,job_page)[0]))

app.run(host='127.0.0.1',port='80')

