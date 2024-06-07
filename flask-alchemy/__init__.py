from flask_sqlalchemy import SQLAlchemy
from flask import Flask, abort, jsonify, request, render_template, Response, redirect, url_for
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:sa%401234@localhost:5432/learning"
db = SQLAlchemy(app)


class TestModel(db.Model):
    __tablename__ = 'test'

    name = db.Column(db.String(), primary_key=True)


    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<TestTable {self.name}>"
    

@app.route('/')
def index():
    return render_template('index.html', name = "Edwin", time= datetime.datetime.utcnow() )
    
@app.route('/test', methods=['POST', 'GET'])
def handle_cars():
    if request.method == 'GET':
        test = TestModel.query.all()
        results = [{"name": t.name} for t in test]
        return {"count": len(results), "cars": results}
    
    elif request.method == "POST":
        output = {'msg': 'posted'}
        response = Response(
            mimetype="application/json",
            response=json.dumps(output),
            status=201
        )
        return response
    
    elif request.method == "PUT":
        #data = request.get_json()
        new_test = TestModel(name = "max")
        db.session.add(new_test)
        db.session.commit()
        return {"message": f"car {new_test.name} has been created successfully."}
    
    
@app.route('/delete/<string:name>')
def delete_car(name):
    car  = TestModel.query.get_or_404(name)
    db.session.delete(car)
    db.session.commit()
    return {"message": f"car {car.name} has been deleted successfully."}


@app.route('/home')
def home():
    return redirect(url_for('index'))


@app.route('/about')
def about():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]
    return render_template('about.html', comments=comments)