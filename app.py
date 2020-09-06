from flask import Flask, redirect, render_template, request
import psycopg2
import json
import os
app = Flask(__name__,template_folder='template',static_folder='static')

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods = ['GET','POST'])
def survey():
    if request.method == 'GET':
        return render_template('survey.html')
    elif request.method == 'POST':
        print('hello')
        form = request.form
        # print(form)
        # answer1 = form['question1_1']
        # answer1,answer2,answer3 = form['selectionBox1'],form['selectionBox2'],form['selectionBox3']
        f = open('static/js/answers.json','r')
        answer = json.load(f);
        genre_test = [
            {
                "name" : "edm",
                "status" : False
            },
            {
                "name" : "pop",
                "status" : False
            },
            {
                "name" : "soul",
                "status" : False
            },
        ]
        country_test = [
            {
                "name" : "vn",
                "status" : False
            },
            {
                "name" : "us",
                "status" : False
            },
            {
                "name" : "hq",
                "status" : False
            }
        ]
        
        res = []
        res_temp = []
        country = []
        genre = []
        
        for i in form:
            if i == 'vn' or i == 'us' or i == 'hq':
                for j in country_test:
                    if i == j['name']:
                        country.append(i)
            elif i == 'pop' or i == 'soul' or i == 'edm':
                for j in genre_test:
                    if i == j['name']:
                        genre.append(i)
        print(country)
        print(genre)
        for i in country:
            for j in answer:
                if j['country'] == i:
                    res_temp.append(j)
        for i in genre:
            for j in res_temp:
                if j['genre'] == i:
                    res.append(j)          
        print(res)
        return render_template('result.html',items = res)


app.run()