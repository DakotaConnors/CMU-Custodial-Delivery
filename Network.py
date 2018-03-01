#http://flask.pocoo.org/docs/0.12/quickstart/

#https://www.youtube.com/watch?v=lUCmVNGs5gw&t=274s
#https://www.youtube.com/watch?v=ZVGwqnjOKjk




from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
currentUser = ''

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        currentUser = request.form['person']
        print(currentUser)
        #return redirect(url_for('orders'))

    return render_template('form.html')

@app.route('/orders', methods=['POST', 'GET'])
def submit():
    buildings = ["Houston", "Wubben", "Escalante"]
    return render_template('form.html', buildings=buildings)

app.run(debug=True)
