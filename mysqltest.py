from flask import Flask, render_template
from flask_moment import Moment
import sqlalchemy as db
from sqlalchemy import func

app = Flask(__name__)
moment = Moment(app)

# sql setting
# engine = db.create_engine("mysql+pymysql://root:123456@172.10.0.9:3306/Mydatabase")
# table = 'Accident'
# metadata = db.MetaData()
# table_accident = db.Table(table , metadata , autoload=True , autoload_with=engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/model')
def model():
    return render_template('model.html')

@app.route('/indextest')
def indexTest():
    return render_template('leaflet.html')

@app.route('/forivanfangyu')
def ivanfangyu():
    return render_template('ivanfangyu.html')



if __name__== "__main__":
    app.run(
        host='0.0.0.0',
        debug=True,
        port=5000
    )
