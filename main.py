from datetime import datetime  
from flask import Flask, flash, render_template, request, redirect
import csv
import os

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'asdasdasdasd'

if not os.path.isfile(r"data.csv"):
        with open('data.csv', 'a', encoding='UTF8', newline='') as f:
            # create the csv writer
            writer = csv.writer(f, delimiter=';')
            data = ['nome completo','cpf','telefone','email','cargos','data','ip','browser','version','platform','uas']
            # write a row to the csv file
            writer.writerow(data)

@app.route("/")
def coleta():
    return render_template('coleta.html')

@app.route("/registrar", methods=['POST'])
def registrar():
    ip = request.remote_addr
    browser = request.user_agent.browser
    version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
    platform = request.user_agent.platform
    uas = request.user_agent.string
    timestamp = datetime.timestamp(datetime.now())

    # get the offices
    offices = ','.join(x.upper() for x in list(request.form.keys())[4:])

    # convert the timestamp to a datetime object in the local timezone
    dt_object = datetime.fromtimestamp(timestamp)
    with open('data.csv', 'a', encoding='UTF8', newline='') as f:
        # create the csv writer
        writer = csv.writer(f, delimiter=';')
        data = [request.form['nomeCompleto'],request.form['cpf'],request.form['telefone'],request.form['email'],offices,dt_object,ip, browser, version, platform, uas]
        
        # write a row to the csv file
        writer.writerow(data)
    
    flash('Obrigado por se registrar!')
    return redirect('/', 302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)