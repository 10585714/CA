from flask import *
# from flask import FLASK, redirect, url_for, render_template, request, session
import sqlite3

app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template("index.html");

# @app.route('/css')


# @app.route('/css')
# def css():
#     return render_template("/assets/css/index.css");

@app.route('/login')
def signup():
    return render_template("/login/login.html");

@app.route('/signup')
def login():
    return render_template("/login/signup.html");

@app.route("/savedetails",methods = ["POST","GET"])

def savedetails():
    msg = "msg"
    if request.method == "POST":
        try:
            USERNAME = request.form["USERNAME"]
            PASSWORD = request.form["PASSWORD"]
            FIRST_NAME = request.form["FIRST_NAME"]
            LAST_NAME = request.form["LAST_NAME"]
            ADRESS = request.form["ADRESS"]
            TELEPHONE = request.form["TELEPHONE"]

            with sqlite3.connect("template/assets/database/WhatsForDinner.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ADRESS, TELEPHONE) values (?,?,?,?,?,?)",(USERNAME, PASSWORD, FIRST_NAME, LAST_NAME, ADRESS, TELEPHONE))
                con.commit()
                msg = "User successfully Added"
        except:
            con.rollback()
            msg = "We can not add the user to the list"
        finally:
            return render_template("/login/success.html", msg=msg)
            con.close()


if __name__ == "__main__":
    app.run(debug=True)
