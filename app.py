from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_mysqldb import MySQL, MySQLdb
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
        if calling_t == row[8]:
            row[8] = int(float(row[8]))
            row[9] = int(float(row[9]))
            row[6] = int(float(row[6]))
            row[16] = int(float(row[16]))
            row[34] = int(float(row[34]))
            data.append(row)

    tst = pandas.DataFrame(data, columns=['id', 'reserved1', 'partial', 'valid_indictor', 'charge_party_indicator', 'answer_time', 'end_time', 'conversation_time', 'caller_number', 'called_number', 'trunk_group_in', 'trunk_group_out', 'termination_code', 'terminating_reason', 'caller_src', 'called_src', 'connected_number', 'caller_gk_softswitch', 'caller_gw_terminal', 'callee_gk_softswitch', 'callee_gw_terminal', 'caller_roam_ip', 'called_roam_ip', 'incoming_route_id', 'outgoing_route_id', 'rec_type', 'alert_time', 'incoming_ts', 'outgoing_ts', 'dial_number ', 'redirect_number', 'charged_number', 'caller_number_before_change', 'called_number_before_change', 'call_setup_time', 'circuit_seizure_time', 'circuit_release_time', 'caller_seize_duration', 'called_seize_duration', 'call_setup_duration', 'opc', 'dpc', 'bearer_service', 'net_type', 'caller_port', 'called_port'])
    tst['end_time'] = pandas.to_datetime(tst['end_time'], format='%y%m%d%H%M%S')
    tst['call_setup_time'] = pandas.to_datetime(tst['call_setup_time'], format='%y%m%d%H%M%S')
    blankIndex = [''] * len(tst)
    tst.index = blankIndex
    tst.rename(columns={'end_time':'End Time', 'conversation_time':'Duration (sec.)', 'caller_number':'Calling Numbe', 'called_number':'Called Number', 'trunk_group_in':'Trunk In No.', 'trunk_group_out':'Trunk  Out No.', 'connected_number':'Connected Number', 'incoming_route_id':'Trunk In Name', 'outgoing_route_id':'Trunk Out Name', 'dial_number ':'Dial Number', 'redirect_number':'Redirect Number', 'call_setup_time':'Start Time'}, inplace=True)
    return tst[['Start Time', 'End Time', 'Duration (sec.)', 'Calling Numbe', 'Called Number', 'Connected Number', 'Dial Number', 'Redirect Number', 'Trunk In No.', 'Trunk In Name', 'Trunk  Out No.',  'Trunk Out Name']]


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
        if called_t == row[9]:
            row[8] = int(float(row[8]))
            row[9] = int(float(row[9]))
            row[6] = int(float(row[6]))
            row[16] = int(float(row[16]))
            row[34] = int(float(row[34]))
            data.append(row)

    tst = pandas.DataFrame(data, columns=['id', 'reserved1', 'partial', 'valid_indictor', 'charge_party_indicator', 'answer_time', 'end_time', 'conversation_time', 'caller_number', 'called_number', 'trunk_group_in', 'trunk_group_out', 'termination_code', 'terminating_reason', 'caller_src', 'called_src', 'connected_number', 'caller_gk_softswitch', 'caller_gw_terminal', 'callee_gk_softswitch', 'callee_gw_terminal', 'caller_roam_ip', 'called_roam_ip', 'incoming_route_id', 'outgoing_route_id', 'rec_type', 'alert_time', 'incoming_ts', 'outgoing_ts', 'dial_number ', 'redirect_number', 'charged_number', 'caller_number_before_change', 'called_number_before_change', 'call_setup_time', 'circuit_seizure_time', 'circuit_release_time', 'caller_seize_duration', 'called_seize_duration', 'call_setup_duration', 'opc', 'dpc', 'bearer_service', 'net_type', 'caller_port', 'called_port'])
    tst['end_time'] = pandas.to_datetime(tst['end_time'], format='%y%m%d%H%M%S')
    tst['call_setup_time'] = pandas.to_datetime(tst['call_setup_time'], format='%y%m%d%H%M%S')
    blankIndex = [''] * len(tst)
    tst.index = blankIndex
    tst.rename(columns={'end_time':'End Time', 'conversation_time':'Duration (sec.)', 'caller_number':'Calling Numbe', 'called_number':'Called Number', 'trunk_group_in':'Trunk In No.', 'trunk_group_out':'Trunk  Out No.', 'connected_number':'Connected Number', 'incoming_route_id':'Trunk In Name', 'outgoing_route_id':'Trunk Out Name', 'dial_number ':'Dial Number', 'redirect_number':'Redirect Number', 'call_setup_time':'Start Time'}, inplace=True)
    return tst[['Start Time', 'End Time', 'Duration (sec.)', 'Calling Numbe', 'Called Number', 'Connected Number', 'Dial Number', 'Redirect Number', 'Trunk In No.', 'Trunk In Name', 'Trunk  Out No.',  'Trunk Out Name']]


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
        if called_t == row[9] and calling_t == row[8]:
            row[8] = int(float(row[8]))
            row[9] = int(float(row[9]))
            row[6] = int(float(row[6]))
            row[16] = int(float(row[16]))
            row[34] = int(float(row[34]))
            data.append(row)

    tst = pandas.DataFrame(data, columns=['id', 'reserved1', 'partial', 'valid_indictor', 'charge_party_indicator', 'answer_time', 'end_time', 'conversation_time', 'caller_number', 'called_number', 'trunk_group_in', 'trunk_group_out', 'termination_code', 'terminating_reason', 'caller_src', 'called_src', 'connected_number', 'caller_gk_softswitch', 'caller_gw_terminal', 'callee_gk_softswitch', 'callee_gw_terminal', 'caller_roam_ip', 'called_roam_ip', 'incoming_route_id', 'outgoing_route_id', 'rec_type', 'alert_time', 'incoming_ts', 'outgoing_ts', 'dial_number ', 'redirect_number', 'charged_number', 'caller_number_before_change', 'called_number_before_change', 'call_setup_time', 'circuit_seizure_time', 'circuit_release_time', 'caller_seize_duration', 'called_seize_duration', 'call_setup_duration', 'opc', 'dpc', 'bearer_service', 'net_type', 'caller_port', 'called_port'])
    tst['end_time'] = pandas.to_datetime(tst['end_time'], format='%y%m%d%H%M%S')
    tst['call_setup_time'] = pandas.to_datetime(tst['call_setup_time'], format='%y%m%d%H%M%S')
    blankIndex = [''] * len(tst)
    tst.index = blankIndex
    tst.rename(columns={'end_time':'End Time', 'conversation_time':'Duration (sec.)', 'caller_number':'Calling Numbe', 'called_number':'Called Number', 'trunk_group_in':'Trunk In No.', 'trunk_group_out':'Trunk  Out No.', 'connected_number':'Connected Number', 'incoming_route_id':'Trunk In Name', 'outgoing_route_id':'Trunk Out Name', 'dial_number ':'Dial Number', 'redirect_number':'Redirect Number', 'call_setup_time':'Start Time'}, inplace=True)
    return tst[['Start Time', 'End Time', 'Duration (sec.)', 'Calling Numbe', 'Called Number', 'Connected Number', 'Dial Number', 'Redirect Number', 'Trunk In No.', 'Trunk In Name', 'Trunk  Out No.',  'Trunk Out Name']]

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM account WHERE username=%s", (username,))
        user = cur.fetchone()
        cur.close()

        if user:
            if password == user['password']:
                if user['firstlog'] == 'Y':
                    session['username'] = user['username']
                    session['id'] = user['id']
                    return redirect(url_for('search'))
                elif user['firstlog'] == 'N':
                    session['username'] = user['username']
                    session['id'] = user['id']
                    return redirect(url_for('change_password_new'))
            else:
                flash('username or password not match', category='error')
                return redirect(url_for('login'))
        else:
            flash('username or password not match', category='error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/changePassword', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        new_pass = request.form.get('new_password')
        confirm_pass = request.form.get('confirm_password')
        log = 'Y'

        Special_sym = ['@', '$', '!', '%', '*', '#', '?', '&']

        if new_pass !='' and confirm_pass != '':
        
            if len(new_pass) < 8:
                flash('length should be at least 8-16.', category='error')
        
            elif len(new_pass) > 16:
                flash('length should be not be greater than 16.', category='error')
        
            elif not any(char.isdigit() for char in new_pass):
                flash('Password should have at least one numeral.', category='error')
        
            elif not any(char.isupper() for char in new_pass):
                flash('Password should have at least one uppercase letter.', category='error')
        
            elif not any(char.islower() for char in new_pass):
                flash('Password should have at least one lowercase letter.', category='error')
        
            elif not any(char in Special_sym for char in new_pass):
                flash('Password should have at least one of the symbols @$!%*#?&', category='error')
        
            elif new_pass != confirm_pass:
                flash('Password don\'t match.', category='error')
        
            else:
                cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute("UPDATE account SET password = %s, conpassword = %s, firstlog = %s WHERE id = %s", (new_pass, confirm_pass, log, session['id'],))
                mysql.connection.commit()
                flash('Password Change.', category='success')
    
        else:
            flash('Please enter your new password', category='error')

    return render_template('change.html')

@app.route('/changePasswordnew', methods=['GET', 'POST'])
def change_password_new():
    if request.method == 'POST':
        new_pass = request.form.get('new_password')
        confirm_pass = request.form.get('confirm_password')
        log = 'Y'

        Special_sym = ['@', '$', '!', '%', '*', '#', '?', '&']

        if new_pass !='' and confirm_pass != '':
        
            if len(new_pass) < 8:
                flash('length should be at least 8-16.', category='error')
        
            elif len(new_pass) > 16:
                flash('length should be not be greater than 16.', category='error')
        
            elif not any(char.isdigit() for char in new_pass):
                flash('Password should have at least one numeral.', category='error')
        
            elif not any(char.isupper() for char in new_pass):
                flash('Password should have at least one uppercase letter.', category='error')
        
            elif not any(char.islower() for char in new_pass):
                flash('Password should have at least one lowercase letter.', category='error')
        
            elif not any(char in Special_sym for char in new_pass):
                flash('Password should have at least one of the symbols @$!%*#?&', category='error')
        
            elif new_pass != confirm_pass:
                flash('Password don\'t match.', category='error')
        
            else:
                cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute("UPDATE account SET password = %s, conpassword = %s, firstlog = %s WHERE id = %s", (new_pass, confirm_pass, log, session['id'],))
                mysql.connection.commit()
                flash('Password Change.', category='success')
                return redirect(url_for('search'))
    
        else:
            flash('Please enter your new password', category='error')

    return render_template('changep.html')

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
                return render_template("search.html", tables=[res.to_html(justify='center')], titles=[''])

        elif calling == '' and called != '' and startDate != '' and endDate != '':
            res = called_with_date(called, startDate, endDate)
            if res.empty == True:
                return render_template("search.html", err = 'No Record Found' )
            else:
                os.remove("combined_csv.csv")
                return render_template("search.html", tables=[res.to_html(justify='center')], titles=[''])

        elif calling != '' and called != '' and startDate != '' and endDate != '':
            res = fully_input(calling, called, startDate, endDate)
            if res.empty == True:
                return render_template("search.html", err = 'No Record Found' )
            else:
                os.remove("combined_csv.csv")
                return render_template("search.html", tables=[res.to_html(justify='center')], titles=[''])
        
        elif calling == '' and called == '' and startDate != '' and endDate != '':
            return render_template("search.html", err = 'No Record Found' )

    return render_template("search.html")

if __name__ == '__main__':
    app.secret_key = "SkjalskdAKAJSKjfkldjkasdk/*564"
    app.run(debug=True)