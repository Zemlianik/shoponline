from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class item(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(150), nullable=False)
    price=db.Column(db.Integer)
    isActive=db.Column(db.Boolean,default=True)
    image=0
    grade=db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return self.title



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/gold')
def gold():
    return render_template('gold.html')

if __name__=='__main__':
    app.run(debug=True)