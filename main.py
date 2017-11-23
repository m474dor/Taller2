from flask import Flask, render_template, request
from flaskext.mysql import MySQL

##sudo pip install flask-mysql / Flask /usar python2.7

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456789'
app.config['MYSQL_DATABASE_DB'] = 'ServosData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()
cursor.execute("SELECT * from Datos")
data = cursor.fetchone()

@app.route("/", methods = ['GET','POST'])
def index():
#	if request.method == 'POST':

	return render_template('index.html')

if __name__=="__main__":
	app.run(host='localhost', port=5000, debug=True)
