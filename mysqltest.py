from flask import Flask, render_template
from flask_moment import Moment
import sqlalchemy as db
from sqlalchemy import func
import cryptography

app = Flask(__name__)
moment = Moment(app)

# sql setting
engine = db.create_engine("mysql+pymysql://root:passw0rd!@localhost/Mydatabase")
metadata = db.MetaData()
connection = engine.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/option')
def option():
    return render_template('optiontest.html')


def get_latlng_list(proxy):
    latlng = []
    mylist = []
    
    for i in proxy.fetchall():
        latlng.append(i[0])
        latlng.append(i[1])
        
    mylist.extend(latlng)
    return mylist

@app.route('/location_show')
def location_show():
    table_taipei2018 = db.Table('taipei_2018' , metadata , autoload=True , autoload_with=engine)
    query = db.select(table_taipei2018)
    proxy = connection.execute(query)
    
    return get_latlng_list(proxy)

@app.route('/newtaipei_2018')
def newtaipei_2018():
    table_newtaipei_2018 = db.Table('newtaipei_2018', metadata , autoload=True , autoload_with=engine)
    query = db.select(table_newtaipei_2018)
    proxy = connection.execute(query)

    return get_latlng_list(proxy)


@app.route('/model')
def model():
    return render_template('model.html')

@app.route('/indextest')
def indexTest():
    return render_template('leaflet.html')

@app.route('/forivanfangyu')
def ivanfangyu():
    return render_template('ivanfangyu.html')

    connection.close()
    engine.dispose()

if __name__== "__main__":
    app.run(
        host='0.0.0.0',
        debug=True,
        port=5000
    )
