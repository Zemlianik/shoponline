from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from cloudipsp import Api, Checkout

api = Api(merchant_id=1396424,
          secret_key='test')
checkout = Checkout(api=api)
data = {
    "currency": "USD",
    "amount": 100000
}
url = checkout.url(data).get('checkout_url')


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Item(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(150), nullable=False)
    price=db.Column(db.Integer,nullable=False)
    isActive=db.Column(db.Boolean,default=True)
    image=0
    grade=db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return 'Запись'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    items=Item.query.order_by(Item.price).all()
    return render_template('about.html',data=items)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create',methods=['POST','SET'])
def creates():
    if request.method=='POST':
        title=request.form['title']
        price = request.form['price']
        grade = request.form['grade']

        item=Item(title=title, price=price,grade=grade)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/about')
        except:
            return 'Произошла ошибка'
    else:
        return render_template('create.html')

@app.route('/gold')
def gold():
    return render_template('gold.html')

if __name__=='__main__':
    app.run(debug=True)