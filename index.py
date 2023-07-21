from flask import Flask, render_template, request, redirect, url_for, session
from tik import *
from influencers_to_notion import *



app = Flask(__name__)
app.secret_key = 'nacho'

@app.route("/home")
def index():
    return render_template('index.html')

@app.route('/loading', methods=['GET', 'POST'])
def loading():
    if request.method == 'POST':
        session['hashtags'] = request.form.get('hashtags').split(',')
        session['keywords'] = request.form.get('keywords').split(',')
        session['num'] = request.form.get('num')
    return render_template('loading.html')

@app.route('/process')
def process():
    creators = []
    creators = find_creators(session.get('hashtags'), creators, session.get('keywords'), session.get('num'))
    session['creators'] = creators
    return render_template('results.html', creators=creators)

@app.route('/add', methods=['GET', 'POST'])
def add():
    data = request.get_json()
    username = data['username']
    email = data['email']
    size = data['size']
    links = data['links']
    create_item('daf8b9db57984a1c9ade779c345f28d3', username, email, size, links)
    return f'Creator Added'



if __name__ == "__main__":
    app.run()