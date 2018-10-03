from flask import Flask, render_template, request, flash, url_for
import mysql.connector as mariadb
app = Flask(__name__)


@app.route('/act', methods=['GET', 'POST'])
def act():
    if(request.method == 'POST'):

        try:
            # $variable = $_POST['name_of_select'];
            name = request.form['name']
            mytime = request.form['mytime']
            mydate = request.form['mydate']
            symptoms = request.form['symptoms']
            conn = mariadb.connect(user='root', password='root', database='hospitalbookingdb')
            cur = conn.cursor()
            # $query = "INSERT INTO table (field) VALUES ($variable)";
            sql = "INSERT INTO patientsbookings(name, booking_time, date_of_birth, symptoms) VALUES('{}', '{}', '{}', '{}')".format(
                name, mytime, mydate, symptoms)
            cur.execute(sql)
            conn.commit()
            msg = "Thanks for Booking Your Data Has Been Stored"
            return render_template('status.html', msg=msg)
        except:
            return "Database connection error"


if __name__ == '__main__':
    app.run(debug=True)