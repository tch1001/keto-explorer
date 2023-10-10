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
        if('subject_set' in jsonData):
            jsonData['subject_set'] = json.loads(jsonData['subject_set'])
        add : Response = requests.put(f"{KETO_WRITE_URL}/admin/relation-tuples", 
                data = json.dumps(jsonData))
    except Exception as e:
        return str(e), 404
    if(add.status_code == 201):
        return 'ok', 200
    else:
        return add.text, 404

def formatParams(jsonData):
    return "?" + "&".join([f"{key}={value}" for key, value in jsonData.items()])

def delete_relation():
    try:
        jsonData = json.loads(request.data)
        if('subject_set' in jsonData):
            jsonData['subject_set'] = json.loads(jsonData['subject_set'])
        delete : Response = requests.delete(f"{KETO_WRITE_URL}/admin/relation-tuples" + formatParams(jsonData), 
                data = json.dumps(jsonData))
    except Exception as e:
        return str(e), 404
    if(delete.status_code == 204):
        return 'ok', 200
    else:
        return delete.text, 404
