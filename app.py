from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

self_db = {'Ayesha':'rastablocker', 'Hira':'motianto'}

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        usr = request.form['usrname']
        pswrd = request.form['pswrd']
        if usr in self_db and pswrd == self_db[usr]:
            return redirect(url_for('schedule'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/schedule')
def schedule():
    return render_template('Schedule.html')

if __name__ == '__main__':
    app.run(debug=True)