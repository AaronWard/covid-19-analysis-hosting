'''
This server is for automating the 
generation of up to date reports for the readme

'''

import os 
import sys
from flask import (Flask, send_file, request, jsonify, send_from_directory)

app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(),'static')

# Make directory if it does not already exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# function for running covidify
def run_covidify():
    os.system('cd ' + app.config['UPLOAD_FOLDER'] + ' && covidify run --output=./')
    os.system('rm -rf ' + os.path.join(app.config['UPLOAD_FOLDER'], 'data'))
    os.system('rm -rf ' + os.path.join(app.config['UPLOAD_FOLDER'], 'reports', '*.xlsx'))

@app.route('/static/<path:filename>')
def send_img(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except:
        return jsonify({'unable to get image'})


# Load the model and run the server
if __name__ == "__main__":
    # app.debug = True
    # port = int(os.environ.get("PORT", 7654))
    app.run(debug=True)