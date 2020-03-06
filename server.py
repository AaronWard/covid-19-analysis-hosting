'''
This server is for automating the 
generation of up to date reports for the readme

'''

import os 
import sys
from flask import (Flask, request, g, redirect, url_for, abort, Response, jsonify, send_from_directory)
from datetime import datetime, date, time 

basedir = os.path.abspath(os.path.dirname(__file__))

# sched = BlockingScheduler()
app = Flask(__name__, static_folder='static')
app.config['FOLDER'] = './static'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'output')

if not os.path.exists(app.config['FOLDER']):
    os.makedirs(app.config['FOLDER'])

# called by the scheduler every hour
def run_covidify():
    print('Running covidify at :', datetime.date(datetime.now()))
    os.system('cd ' + app.config['FOLDER'] + ' && covidify run --output=./')
    os.system('rm -rf ' + os.path.join(app.config['FOLDER'], 'data'))
    os.system('rm -rf ' + os.path.join(app.config['FOLDER'], 'reports', '*.xlsx'))

@app.route('/<path:filename>') 
def send_file(filename): 
    '''
    Return the requested images back to the github readme
    '''
    print(os.system('ls ' + str(os.getcwd())))
    print(os.system('ls ' + str(app.config['FOLDER'])))
    return (app.config['FOLDER'],'reports', 'images', filename)

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