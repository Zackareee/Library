import os
import sqlite3

from flask import Blueprint, render_template

mainbp = Blueprint('main', __name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"  # !! Only in development environment.

discord = []

if os.name == 'nt':
    s = "#"
else:
    s = "-"


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@mainbp.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response


@mainbp.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    booksvar = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('index.html', booksvar=booksvar)

