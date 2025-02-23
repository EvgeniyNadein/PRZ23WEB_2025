from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route("/mainpage")
def mainpage():
    return render_template('mainpage.html')


@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():
    if request.method == 'POST':
        Login = request.form.get('Login')
        Password = request.form.get('Password')

        db_lp = sqlite3.connect('login_password.db')
        cursor_db = db_lp.cursor()
        cursor_db.execute("SELECT password FROM login_password WHERE login=?", (Login,))
        pas = cursor_db.fetchall()

        cursor_db.close()
        try:
            if pas[0][0] != Password:
                return render_template('authBad.html')
        except:
            return render_template('authBad.html')

        db_lp.close()
        return render_template('successfulAuth.html')

    return render_template('auth.html')


@app.route('/registration', methods=['GET', 'POST'])
def form_registration():
    try:
        if request.method == 'POST':
            Login = request.form.get('Login')
            Password = request.form.get('Password')

            db_lp = sqlite3.connect('login_password.db')
            cursor_db = db_lp.cursor()

            cursor_db.execute('INSERT INTO login_password (login, password) VALUES(?, ?)', (Login, Password))
            db_lp.commit()
            cursor_db.close()
            db_lp.close()

            return render_template('successfulReg.html')

    except:
        return render_template('regBad.html')

    return render_template('reg.html')


if __name__ == '__main__':
    app.run()
