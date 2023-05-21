from datetime import datetime  
from flask import Flask, flash, render_template, request
import csv
import os


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'asdasdasdasd'

if not os.path.isfile(r"data.csv"):
        with open('data.csv', 'a', encoding='UTF8', newline='') as f:
            # create the csv writer
            writer = csv.writer(f)
            data = ['nomeCompleto','cpf','telefone','email','data','ip' , 'browser', 'version', 'platform', 'uas']
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

    # convert the timestamp to a datetime object in the local timezone
    dt_object = datetime.fromtimestamp(timestamp)
    with open('data.csv', 'a', encoding='UTF8', newline='') as f:
    # create the csv writer
        writer = csv.writer(f)
        data = [request.form['nomeCompleto'],request.form['cpf'],request.form['telefone'],request.form['email'],dt_object,ip, browser, version, platform, uas]
        # write a row to the csv file
        writer.writerow(data)
    flash('Obrigado por se registrar')
    return render_template('horario.html')

@app.route("/horario")
def horario():
    return render_template('horario.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)