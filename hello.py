from flask import Flask, url_for, request, render_template, redirect
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# Add page
@app.route('/hello')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('hello.html', name=name)

# Escape HTML
@app.route('/user/<username>')
def show_user_profile(username):
    return f"User {escape(username)}"

# Enforce variable rules
@app.route('/path/<path:subpath>') # specify "path" type
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

# There are different canonical conventions for using trailing slashes.
# E.g. The projects endpoint usually has a trailing slash but not the 
# about page
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# To build a URL to a specific function, use the url_for() function.
with app.test_request_context():
    print(url_for('show_user_profile', username='John Doe'))
    
# By default, route only answers to GET requests, but this can be changed
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "answering to POST"
    else:
        return "answering to GET"
    
# This can also be achieved with specific methods; also see redirect function
@app.get('/login-get')
def login_get():
    return redirect(url_for('login'))

@app.post('/login-post')
def login_post():
    return redirect(url_for('login'))
