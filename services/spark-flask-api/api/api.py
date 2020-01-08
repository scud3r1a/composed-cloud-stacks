# Import libraries
import json
import requests
from flask import Flask, jsonify, request
from subprocess import call
import time, datetime
import hashlib
import sys
import pandas as pd

# Constants
SPARK_VERSION = '2.3.1'
SPARK_HOME = '/usr/spark-' + SPARK_VERSION
SPARK_SUBMIT = SPARK_HOME + '/bin/spark-submit'
PYTHON_VERSION = str(sys.version).split(' ')[0]

# Init
app = Flask(__name__)
print('')

# GET version
@app.route('/get/version', methods=['GET'])
def get_version():

    # Return Python and Spark version
    return jsonify({
        'python_version': str(PYTHON_VERSION),
        'spark_version': str(SPARK_VERSION)
    }), 201


# POST task (script)
@app.route('/post/task', methods=['POST'])
def post_task():

    # Extract script and flags
    processed_content = []
    content = str(request.get_json()).replace('{', '').replace('}', '')
    content = content.replace('\' ', '\'').replace('\" ', '\"').replace(', ', ',').split(',')
    for line in content:
        line = line.replace('\'', '').replace('\"', '').replace(': ', ':')
        line = line.split(':')
        processed_content.append(line)
    content = processed_content

    # Crawl through content lines
    for line in content:
        arg = line[0].strip()
        if arg == 'script':
            script = line[1]
        elif arg == 'flags':
            flags = line[1]

    # Execute task
    task = ['bash', SPARK_SUBMIT, script] + flags.split(' ')
    print(task)
    call(task)
    print("Done.\n")

    # Return response
    return jsonify({
        'status': 'success'
    }), 201
