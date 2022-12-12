from flask import Blueprint, render_template, flash, Flask, redirect, url_for, current_app
from datetime import timedelta
from os import getcwd
import base64
import time
import os
import cProfile
import pstats

mainbp = Blueprint('main', __name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"    # !! Only in development environment.

discord = []


if os.name == 'nt':
    s = "#"
else:
    s = "-"

@mainbp.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

@mainbp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



