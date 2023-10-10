from flask import Flask, current_app

import os
from dotenv import load_dotenv

load_dotenv(os.environ.get("ENV_FILE",".env"), override=True)
print(os.environ)
import keto

app = Flask(__name__)

app.add_url_rule('/', methods=["GET"], view_func=keto.list_relations)
app.add_url_rule('/check', methods=["GET"], view_func=keto.check_relation)
app.add_url_rule('/expand', methods=["GET"], view_func=keto.expand)
app.add_url_rule('/add', methods=["POST"], view_func=keto.add_relation)
app.add_url_rule('/delete', methods=["POST"], view_func=keto.delete_relation)

def create_app(test_config=None):
    if test_config is not None:
        app.config.update(test_config)
    return app
