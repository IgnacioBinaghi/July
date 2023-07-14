from flask import Flask, render_template, request, session
import random
from getNotion import read_database, update_item
from influencers_to_notion import accept_creator, deny_creator
from main import *

app = Flask(__name__)
app.secret_key = 'july'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forReview')
def forReview():
    db_link = request.args.get('db_link')[22:54]
    session['db_link'] = db_link
    creators = read_database(db_link)
    return render_template('review.html', creators=creators)


@app.route('/generate', methods=['GET', 'POST'])
def generate():
    businesses = get_businesses()
    return render_template('generate.html', businesses=businesses)

@app.route('/submitGenerate', methods=['POST'])
def submitGenerate():
    data = request.get_json()
    business = data['selectedKey']
    dbLink = data['dbLink']
    main(dbLink, business)
    return ''


@app.route('/accept', methods=['POST'])
def accept():
    db_link = session.get('db_link')
    id = request.form.get('id')
    print(db_link, id)
    
    accept_creator(db_link, id)

    return f'Creator Accepted'


@app.route('/denied', methods=['POST'])
def denied():
    db_link = session.get('db_link')
    id = request.form.get('id')
    
    deny_creator(db_link, id)

    return f'Creator Denied'




if __name__ == '__main__':
    app.run()
