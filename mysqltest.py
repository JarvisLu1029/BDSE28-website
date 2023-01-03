from flask import Flask, render_template
from flask_moment import Moment
import sqlalchemy as db
from sqlalchemy import func
import cryptography
import geocoder
import use_model.weather as weather



app = Flask(__name__)
moment = Moment(app)

# sql setting
engine = db.create_engine("mysql+pymysql://root:Asd_102938@localhost/accident")
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

# 接收location.html的year loc選項 並抓取該資料庫table的值
@app.route('/option/<loc_year>')
def location_year(loc_year):
    table_location = db.Table(f'{loc_year}', metadata , autoload=True , autoload_with=engine)
    query = db.select(table_location.c.lat, table_location.c.lng)
    proxy = connection.execute(query)

    latlng = []
    mylist = []
    
    for i in proxy.fetchall():
        latlng.append(i.lat)
        latlng.append(i.lng)
        
    mylist.extend(latlng)
    return mylist

@app.route('/model')
def model():
    return render_template('model.html')

# 收到使用者輸入的地址轉成座標
@app.route('/model/<city_dist>/<road>')
def model_address(city_dist,road):
    coo = geocoder.arcgis(f'{city_dist}{road}').latlng
    weather.weatherAPI(coo)
    density  = weather.population(f'{city_dist}')
    return coo

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
