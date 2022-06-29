from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import pandas
from datetime import date
import glob
import csv
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'scam'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


def calling_fnc(calling_t):

    path = 'C:/Users/Thanalak/PycharmProjects/True/'
    df = pandas.concat(map(pandas.read_csv, glob.glob(path + "*.csv")))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')
    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if calling_t == row[1]:
            data.append(row)
    return pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])


def called_fnc(called_t):

    path = 'C:/Users/Thanalak/PycharmProjects/True/'
    df = pandas.concat(map(pandas.read_csv, glob.glob(path + "*.csv")))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')
    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if called_t == row[2]:
            data.append(row)
    return pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])


def calling_with_date(calling_t, start, end):

    fileopen_lst = []
    path = 'C:/Users/Thanalak/PycharmProjects/True/'

    start_date = list(start.split('-'))
    end_date = list(end.split('-'))

    for i in range(0, len(start_date)):
        start_date[i] = int(start_date[i])

    for j in range(0, len(end_date)):
        end_date[j] = int(end_date[j])

    sdate = date(start_date[2], start_date[1], start_date[0])  # start date
    edate = date(end_date[2], end_date[1], end_date[0])  # end date
    surname_file = "-*.csv"

    lst_date = pandas.date_range(sdate, edate, freq='d').strftime('%m-%d-%Y').tolist()

    for k in range(0, len(lst_date)):
        combine = lst_date[k] + surname_file
        for file in glob.glob(path + combine):
            fileopen_lst.append(file)

    df = pandas.concat(map(pandas.read_csv, fileopen_lst))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if calling_t == row[1]:
            data.append(row)
    
    tst = pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])

    return tst[['calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk']]


def called_with_date(called_t, start, end):

    fileopen_lst = []
    path = 'C:/Users/Thanalak/PycharmProjects/True/'

    start_date = list(start.split('-'))
    end_date = list(end.split('-'))

    for i in range(0, len(start_date)):
        start_date[i] = int(start_date[i])

    for j in range(0, len(end_date)):
        end_date[j] = int(end_date[j])

    sdate = date(start_date[2], start_date[1], start_date[0])  # start date
    edate = date(end_date[2], end_date[1], end_date[0])  # end date
    surname_file = "-*.csv"

    lst_date = pandas.date_range(sdate, edate, freq='d').strftime('%m-%d-%Y').tolist()

    for k in range(0, len(lst_date)):
        combine = lst_date[k] + surname_file
        for file in glob.glob(path + combine):
            fileopen_lst.append(file)

    df = pandas.concat(map(pandas.read_csv, fileopen_lst))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if called_t == row[2]:
            data.append(row)

    tst = pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])

    return tst[['calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk']]


def fully_input(calling_t, called_t, start, end):

    fileopen_lst = []
    path = 'C:/Users/Thanalak/PycharmProjects/True/'

    start_date = list(start.split('-'))
    end_date = list(end.split('-'))

    for i in range(0, len(start_date)):
        start_date[i] = int(start_date[i])

    for j in range(0, len(end_date)):
        end_date[j] = int(end_date[j])

    sdate = date(start_date[2], start_date[1], start_date[0])  # start date
    edate = date(end_date[2], end_date[1], end_date[0])  # end date
    surname_file = "-*.csv"

    lst_date = pandas.date_range(sdate, edate, freq='d').strftime('%m-%d-%Y').tolist()

    for k in range(0, len(lst_date)):
        combine = lst_date[k] + surname_file
        for file in glob.glob(path + combine):
            fileopen_lst.append(file)

    df = pandas.concat(map(pandas.read_csv, fileopen_lst))
    df.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

    csv_file = csv.reader(open('combined_csv.csv', "r"), delimiter=",")

    data = []
    for row in csv_file:
        if called_t == row[2] and calling_t == row[1]:
            data.append(row)

    tst = pandas.DataFrame(data, columns=['id', 'calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk'])

    return tst[['calling', 'called', 'date', 'startTime', 'Endtime', 'incomingTrunk']]


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM account WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()

        if len(user) > 0:
            if password== user['password'].encode('utf-8'):
                if user['firstlog'] == 'Y':
                    session['username'] = user['username']
                    return render_template('search.html')
                else:
                    session['username'] = user['username']
                    return render_template('change.html')
        else:
            flash('username or password not match', category='error')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM account WHERE username=%s", (username,))
        user = cur.fetchone()
        print(user)
        cur.close()

        if len(user) > 0:
            if password == user['password'].encode('utf-8'):
                if user['firstlog'] == 'Y':
                    session['username'] = user['username']
                    return render_template('search.html')
                elif user['firstlog'] == 'N':
                    session['username'] = user['username']
                    return render_template('change.html')
                else:
                    flash('username or password not match', category='error')
                    return render_template('login.html')

        elif len(user) == None:
            flash('username or password not match', category='error')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/changePassword', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        new_pass = request.form.get('new_password').encode('utf-8')
        confirm_pass = request.form.get('confirm_password').encode('utf-8')
        log = 'Y'

        Special_sym = ['@', '$', '!', '%', '*', '#', '?', '&']

        if new_pass !='' and confirm_pass != '':
        
            if len(new_pass) < 8:
                flash('length should be at least 8-16.', category='error')
        
            if len(new_pass) > 16:
                flash('length should be not be greater than 16.', category='error')
        
            if not any(char.isdigit() for char in new_pass):
                flash('Password should have at least one numeral.', category='error')
        
            if not any(char.isupper() for char in new_pass):
                flash('Password should have at least one uppercase letter.', category='error')
        
            if not any(char.islower() for char in new_pass):
                flash('Password should have at least one lowercase letter.', category='error')
        
            if not any(char in Special_sym for char in new_pass):
                flash('Password should have at least one of the symbols @$!%*#?&', category='error')
        
            if new_pass != confirm_pass:
                flash('Password don\'t match.', category='error')
        
            else:
                cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute("UPDATE account SET password = %s, conpassword = %s, firstlog = %s WHERE id = %s", (new_pass, confirm_pass, log, session['id'],))
                mysql.connection.commit()
                flash('Password Change.', category='success')
    
    else:
        flash('Please enter your new password', category='error')

    return render_template("change.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        calling = request.form.get('calling_number')
        called = request.form.get('called_number')
        startDate = request.form.get('startdate')
        endDate = request.form.get('enddate')

        if calling != '' and called == '' and startDate != '' and endDate != '':
            res = calling_with_date(calling, startDate, endDate)
            if res.empty == True:
                return render_template("search.html", err = 'No Record Found' )
            else:
                os.remove("combined_csv.csv")
                return render_template("search.html", tables=[res.to_html()], titles=[''])

        elif calling == '' and called != '' and startDate != '' and endDate != '':
            res = called_with_date(called, startDate, endDate)
            if res.empty == True:
                return render_template("search.html", err = 'No Record Found' )
            else:
                os.remove("combined_csv.csv")
                return render_template("search.html", tables=[res.to_html()], titles=[''])

        elif calling != '' and called != '' and startDate != '' and endDate != '':
            res = fully_input(calling, called, startDate, endDate)
            if res.empty == True:
                return render_template("search.html", err = 'No Record Found' )
            else:
                os.remove("combined_csv.csv")
                return render_template("search.html", tables=[res.to_html()], titles=[''])

    return render_template("search.html")

if __name__ == '__main__':
    app.secret_key = "SkjalskdAKAJSKjfkldjkasdk/*564"
    app.run(debug=True)