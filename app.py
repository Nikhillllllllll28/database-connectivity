from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/loginpage'
db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False,  nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    sex = db.Column(db.String(10), unique=False, nullable=False)

@app.route("/contact", methods=['GET', 'POST'])
def Contact():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        sex = request.form.get('sex')
        entry = Contacts(name=name, age=age, sex=sex)
        db.session.add(entry)
        db.session.commit()

    return render_template('index.html')

app.run(debug=True)
