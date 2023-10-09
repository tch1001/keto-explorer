from flask import render_template, request, redirect, url_for
import requests
from requests import Response
import os
import json

KETO_READ_URL = os.environ.get('KETO_READ_URL')
KETO_WRITE_URL = os.environ.get('KETO_WRITE_URL')

def get_all():
    ret : Response = requests.get(f"{KETO_READ_URL}/relation-tuples")
    return json.loads(ret.text)

def list_relations():
    return render_template('admin.html', ret = get_all())

def check_relation():
    try:
        check : Response = requests.get(f"{KETO_READ_URL}/relation-tuples/check", params = request.args)
        return check.text
    except Exception as e:
        return str(e), 404

def expand():
    try:
        expand : Response = requests.get(f"{KETO_READ_URL}/relation-tuples/expand", params = request.args)
        return expand.text
    except Exception as e:
        return str(e), 404

def add_relation():
    try:
        jsonData = (json.loads(request.data))
        # app.logger.info(jsonData)
        print("HI")
        if('subject_set' in jsonData):
            jsonData['subject_set'] = json.loads(jsonData['subject_set'])
        print("HI")
        add : Response = requests.put(f"{KETO_WRITE_URL}/relation-tuples", 
                data = json.dumps(jsonData))
        print("HI")
    except Exception as e:
        return str(e), 404
    if(add.status_code == 201):
        return 'ok', 200
    else:
        return add.text, 404
