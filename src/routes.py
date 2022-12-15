import os
import sqlite3
from src.forms import BookForm
from flask import Blueprint, render_template,request

mainbp = Blueprint('main', __name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "true"  # !! Only in development environment.

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
    
    create_book_form = BookForm()
    conn = get_db_connection()
    booksvar = conn.execute('SELECT * FROM books').fetchall()
    conn.close()       
    
    if request.method == "POST": #Submitting a form
        print("wow")
        return render_template('index.html', BookForm=create_book_form)

    return render_template('index.html', booksvar=booksvar, BookForm=create_book_form)

