'''
This server is for automating the 
generation of up to date reports for the readme

'''

import os 
import sys
from flask import (Flask,send_file, request, g, redirect, url_for, abort, Response, jsonify, send_from_directory)
from datetime import datetime, date, time 

app = Flask(__name__)

def list_paths(startpath='/'):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

# function for running covidify
# Load the model and run the server
if __name__ == "__main__":
    # app.debug = True
    # port = int(os.environ.get("PORT", 7654))
    app.run(debug=True)