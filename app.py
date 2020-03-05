'''
This server is for automating the 
generation of up to date reports for the readme

'''

import os 
import sys
from flask import (Flask, request, g, redirect, url_for, abort, Response, jsonify, send_from_directory)
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, date, time 

sched = BlockingScheduler()
app = Flask(__name__)
app.config['FOLDER'] = os.path.join(os.getcwd(),'reports', 'images')

# called by the scheduler every hour
def run_covidify():
    print('Running covidify at :', datetime.date(datetime.now()))
    os.system('covidify run --output=./')
    os.system('mv ./reports/images/*.jpg ./static')
    os.system('rm -rf ./data')
    os.system('rm -rf ./reports/*.xlsx')


@app.route('/<path:filename>') 
def send_file(filename): 
    '''
    Return the requested images back to the github readme
    '''
    return os.path.join(app.config['FOLDER'], filename)

# Load the model and run the server
if __name__ == "__main__":
    app.debug = False
    port = int(os.environ.get("PORT", 8888))
    app.run(port=port)