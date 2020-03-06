'''
This server is for automating the 
generation of up to date reports for the readme

'''

import os 
import sys
from flask import (Flask, request, g, redirect, url_for, abort, Response, jsonify, send_from_directory)
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, date, time 

basedir = os.path.abspath(os.path.dirname(__file__))

sched = BlockingScheduler()
app = Flask(__name__)
app.config['FOLDER'] = 'static'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'output')
os.makedirs(app.config['UPLOADED_PHOTOS_DEST'])

# called by the scheduler every hour
def run_covidify():
    print('Running covidify at :', datetime.date(datetime.now()))
    os.system('covidify run --output=' + app.config['UPLOADED_PHOTOS_DEST'])
    # os.system('mv ./reports/images/*.jpg ./static')
    # os.system('rm -rf ' + app.config['UPLOADED_PHOTOS_DEST'] + '/data')
    # os.system('rm -rf ' + app.config['UPLOADED_PHOTOS_DEST'] + '/reports/*.xlsx')


@app.route('/images/<filename>') 
def send_file(filename): 
    '''
    Return the requested images back to the github readme
    '''
    print(os.system('ls ' + str(os.getcwd())))
    print(os.system('ls ' + str(app.config['UPLOADED_PHOTOS_DEST'])))
    return os.path.join(app.config['UPLOADED_PHOTOS_DEST'],'reports', 'images', filename)

@app.route('/') 
def index(): 
    '''
    Return the requested images back to the github readme
    '''
    return jsonify({'results': 'example'})

# Load the model and run the server
if __name__ == "__main__":
    # app.debug = True
    # port = int(os.environ.get("PORT", 7654))
    app.run(debug=True)