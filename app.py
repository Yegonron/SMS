from flask import Flask, render_template, redirect, request

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///root.db'

db = SQLAlchemy(app)

class Player(db.Model):
    playerID = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    gender = db.Column(db.String(120), unique=True, nullable=False)
    phoneno = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.String(120), unique=True, nullable=False)
    sport = db.Column(db.String(120), unique=True, nullable=False)
    position = db.Column(db.String(120), unique=True, nullable=False)
    bootsize = db.Column(db.String(120), unique=True, nullable=False)
    kitsize = db.Column(db.String(120), unique=True, nullable=False)
    photo = db.Column(db.String(120), unique=True, nullable=False)

    def __tsl__ (self):
        return '<Player %r>' % self.playerID

@app.route('/', methods =['POST','GET'])
def home():
    if request.method == 'POST':
        surname = request.form['surName']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        gender = request.form['gender']
        phoneno = request.form['phoneNo']
        age = request.form['age']
        sport = request.form['sport']
        position = request.form['position']
        bootsize = request.form['bootSize']
        kitsize = request.form['kitSize']
        photo = request.form['photo']

        new_entry = Player(surname=surname, firstname=firstname, lastname=lastname, gender=gender, phoneno=phoneno,
                            age=age, sport=sport, position=position, bootsize=bootsize, kitsize=kitsize, photo=photo)

        try:
             db.session.add(new_entry)
             db.session.commit()
             return redirect('/')

        except:
            return "Error"
    else:
        return render_template('player.html')

class Clinic(db.Model):
    medicalReportNo = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    medicalReport = db.Column(db.String(1000), unique=True, nullable=False)

    def __tsl__ (self):
        return '<Clinic %r>' % self.medicalReportNo


@app.route('/', methods =['POST','GET'])
def clinic():
    if request.method == 'POST':
        surname = request.form['surName']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        medicalReport = request.form['medicalReport']
        
        new_entry = Clinic(surname=surname, firstname=firstname, lastname=lastname, medicalReport= medicalReport)

        try:
             db.session.add(new_entry)
             db.session.commit()
             return redirect('/')

        except:
            return "Error"
    else:
        return render_template('clinic.html')


class Coach(db.Model):
    coachID = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    def __tsl__ (self):
        return '<Clinic %r>' % self.coachID

    
@app.route('/', methods =['POST','GET'])
def coach():
    if request.method == 'POST':
        surname = request.form['surName']
        firstname = request.form['firstName']
        lastname = request.form['lastName']
        email = request.form['email']
        
        new_entry = Clinic(surname=surname, firstname=firstname, lastname=lastname, email= email)

        try:
             db.session.add(new_entry)
             db.session.commit()
             return redirect('/')

        except:
            return "Error"
    else:
        return render_template('coach.html')


if __name__ == "__main__":
    app.run(debug=True)

