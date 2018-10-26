from flask import Flask, render_template, request, flash, url_for, redirect
import mysql.connector as mariadb
app = Flask(__name__)


@app.route('/')
def index():

    return render_template('home.html')


@app.route('/about')
def about():

    return render_template('about.html')


@app.route('/bookings', methods=['GET', 'POST'])
def bookings():
    if(request.method == 'POST'):

        # $variable = $_POST['name_of_select'];
        name = request.form['name']
        mytime = request.form['mytime']
        print(request.form)
        mydate = request.form['mydate']
        symptoms = request.form['symptoms']
        conn = mariadb.connect(user='root', password='root', database='HospitalBookingDB')
        cur = conn.cursor()
        # $query = "INSERT INTO table (field) VALUES ($variable)";
        sql = "INSERT INTO patientsbookings(name, booking_time, date_of_birth, symptoms) VALUES('{}', '{}', '{}', '{}')".format(
            name, mytime, mydate, symptoms)
        cur.execute(sql)
        conn.commit()

        flash('Thanks For Your Patronage, Check Your Booking Details Below', 'success')
        return redirect(url_for('bookingdetails'))

    return render_template('bookings.html')


@app.route('/bookingdetails')
def bookingdetails():
    conn = mariadb.connect(user='root', password='root', database='hospitalbookingdb')
    # connecting to Database
    cur = conn.cursor()
    # query the DB
    cur.execute(
        "SELECT name, booking_time, date_of_birth, symptoms, date FROM patientsbookings WHERE date>=DATE_SUB(NOW(), INTERVAL 24 HOUR)")
    # This query is used to fetch The Data from the Database(READ)
    rows = cur.fetchall()

    return render_template('bookingdetails.html', rows=rows)


if __name__ == '__main__':
    app.secret_key = 'secret123hack'
    app.run(debug=True)
