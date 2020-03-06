'''
This server is for automating the 
generation of up to date reports for the readme

'''

import os 
import sys
from flask import (Flask,send_file, request, g, redirect, url_for, abort, Response, jsonify, send_from_directory)
from datetime import datetime, date, time 

basedir = os.path.abspath(os.path.dirname(__file__))

# sched = BlockingScheduler()
app = Flask(__name__, static_folder='static')
app.config['FOLDER'] = os.path.join(os.getcwd(),'static')

if not os.path.exists(app.config['FOLDER']):
    os.makedirs(app.config['FOLDER'])

# called by the scheduler every hour
def run_covidify():
    print('Running covidify at :', datetime.date(datetime.now()))
    os.system('cd ' + app.config['FOLDER'] + ' && covidify run --output=./')
    os.system('rm -rf ' + os.path.join(app.config['FOLDER'], 'data'))
    os.system('rm -rf ' + os.path.join(app.config['FOLDER'], 'reports', '*.xlsx'))

@app.route('/<path:filename>') 
def send_graph(filename): 
    '''
    Return the requested images back to the github readme
    '''
    print('FILE NAME: ', filename)

    print('CWD ...')
    print('...', os.system('ls ' + str(os.getcwd())))

    print('FOLDER ...')
    print('...', os.system('ls ' + str(app.config['FOLDER'])))

    image = os.path.join(app.config['FOLDER'],'reports', 'images', filename)         
    return send_file(image)

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