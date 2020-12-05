from flask import Flask, jsonify, render_template, request
import pymongo
import markdown
import markdown.extensions.fenced_code
from pygments.formatters import HtmlFormatter
from datetime import datetime,timedelta
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    return "123"
if __name__ == '__main__':
    app.run(debug=True)