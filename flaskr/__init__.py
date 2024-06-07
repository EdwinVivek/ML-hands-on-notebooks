import os
from flask import Flask, abort, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy();


class TestModel():
    __tablename__ = 'test'
    
    name = db.Column(db.String(), primary_key=True)
    
    def __init__(self):
        global db
        self.db = db.Model    
       # self.name = name
    

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
        #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    ) 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sa@1234@localhost:5432/learning'
    global db
    db = SQLAlchemy(app)

    @app.route('/')
    def home():
        return 'Welcome - My Flask App'
    
    @app.route('/hello')
    def hello():
        #users = db.session.execute(db.select('sales').order_by('sales.country')).scalars()
        #testModel  = TestModel(db)
        data  = TestModel().db.query.all()
        return data
        #return 'Hello world'
    
    
    #dynamic routes
    @app.route('/dynamic/<int:a>/<int:b>')
    def add(a, b):
        try:
            return '<h1>Adding {} and {} = {}</h1>'.format(a,b, a+b)
        except:
            abort(404)
    
    @app.route('/query')
    def query():
        return jsonify(db.query)
    
    
    return app



        