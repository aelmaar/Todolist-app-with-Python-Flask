from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)

#class Task(db.Model):
#    id = db.Column(db.Integer, primary_key=True)


@app.route('/')
def index():
    return render_template('index.html')
