from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/FlaskProject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("Alveena")
db = SQLAlchemy(app)

class employee(db.Model):
    e_id=db.Column(db.Integer,primary_key=True)
    e_name=db.Column(db.String(20),nullable=True)
    email=db.Column(db.String(20),nullable=True)
    phone_no=db.Column(db.String(12),nullable=True)
    e_company=db.Column(db.String(30),nullable=True)

with app.app_context():
    db.create_all()

if __name__=='__main__':
    app.run(debug=True)