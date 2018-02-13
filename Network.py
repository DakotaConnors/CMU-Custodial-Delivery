#http://flask.pocoo.org/docs/0.12/quickstart/

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def homePage():
    
    return render_template('index.html')

@app.route('/index',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      print('requesting data')
      result = request.form
      print('recieved data',result)
      return render_template("index.html")

app.run()
