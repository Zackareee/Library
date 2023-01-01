import os
import sqlite3
from src.forms import BookForm, EditForm
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
    edit_book_form = EditForm()
    conn = get_db_connection()
     
     
    if request.method == "POST": #Submitting a form
        print("wow")
        if edit_book_form.validate_on_submit():
            id = (edit_book_form.Eid.data) #TODO MUST CHECK AGAINST ID'S LINKED TO CURRENT USER TO AVOID MALICIOUS DATA EDITS. 
            title = (edit_book_form.Ename.data)
            volume = (edit_book_form.Evolume.data)
            #if user has book id edit_book_form.Eid.data:
            conn.execute(f"UPDATE books SET title = \"{title}\", volume = {volume} WHERE id = {id}")
    booksvar = conn.execute('SELECT * FROM books').fetchall()
    conn.close()      
    return render_template('index.html', booksvar=booksvar, BookForm=create_book_form, EditForm=edit_book_form)

