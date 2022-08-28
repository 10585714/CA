from flask import *
# from flask import FLASK, redirect, url_for, render_template, request, session
import sqlite3


app = Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template("index.html");

@app.route('/store')
def store():
    return render_template("/store/store.html");

@app.route('/recipes')
def recipes():
    return render_template("/recipes/recipes.html");

# @app.route('/css')


# @app.route('/css')
# def css():
#     return render_template("/assets/css/index.css");

@app.route('/signup')
def signup():
    return render_template("/login/signup.html");

@app.route('/home_test')
def home_text():
    return render_template("/home/home.html");

@app.route("/saveDetails", methods = ["POST","GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            username = request.form["username"]
            password = request.form["password"]
            first_name = request.form["first_name"]
            last_name = request.form["last_name"]
            adress = request.form["adress"]
            telephone = request.form["telephone"]
            with sqlite3.connect("WhatsForDinner.db") as con:
                cur = con.cursor()
                cur.execute("insert into user(USERNAME, PASSWORD , FIRST_NAME , LAST_NAME, ADRESS, TELEPHONE) values (?,?,?,?,?,?)",
                            (username, password, first_name, last_name, adress, telephone))
                con.commit()
                msg = "User successfully Added"
        except:
            con.rollback()
            msg = "We can not add the user to the list"
        finally:
            return render_template("/login/success.html", msg=msg)
            con.close()


@app.route("/savecontact", methods=["POST","GET"])
def savecontact():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            message = request.form["message"]
            phone = request.form["phone"]
            with sqlite3.connect("WhatsForDinner.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO CONTACT(NAME, EMAIL, MESSAGE, TELEPHONE) values (?,?,?,?)",
                            (name, email, message, phone))
                con.commit()
                msg = "User successfully Added"
        except:
            con.rollback()
            msg = "Message was not sent, try again."
        finally:
            return render_template("/login/admin/success.html", msg=msg)
            con.close()


@app.route('/login')
def login_render():
    return render_template("/login/login.html");

def check_user(username, password):
    con = sqlite3.connect('WhatsForDinner.db')
    cur = con.cursor()
    cur.execute('Select username,password FROM user WHERE username=? and password=?', (username, password))
    result = cur.fetchone()
    if result:
        return True
    else:
        return False

# def check_user_type(usertype, username, password):
#     con = sqlite3.connect('WhatsForDinner.db')
#     cur = con.cursor()
#     cur.execute('Select usertype FROM user WHERE username=?, password?', (username, password))
#     result = cur.fetchone()
#     if usertype=='A':
#         return True
#     else:
#         return False

app.secret_key = "r@nd0mSk_1"

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(check_user(username, password))
        if check_user(username, password):
            session['username'] = username
        return redirect(url_for('home'))
    else:
        return redirect(url_for('/'))

#
# @app.route('/checkusertype', methods=["POST", "GET"])
# def checkusertype():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         print(check_user(username, password))
#         if check_user(username, password):
#             session['username'] = username
#             print(check_user_type(username, password))
#             if check_user_type(username, password):
#                 return redirect(url_for('/store'))
#             else:
#                 return redirect(url_for('home'))
#     else:
#         return redirect(url_for('/'))

@app.route('/home', methods=['POST', "GET"])
def home():
    if 'username' in session:
        return render_template('/home/home.html', username=session['username'])
    else:
        return "Username or Password is wrong!"

@app.route('/view')
def view():
    con = sqlite3.connect("WhatsForDinner.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from user")
    rows = cur.fetchall()
    return render_template("/view/view.html", rows=rows)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/recipe1')
def recipe1():
    return render_template("/recipes/recipe1.html");

@app.route('/recipe2')
def recipe2():
    return render_template("/recipes/recipe2.html");

@app.route('/recipe3')
def recipe3():
    return render_template("/recipes/recipe3.html");

@app.route('/recipe4')
def recipe4():
    return render_template("/recipes/recipe4.html");


if __name__ == "__main__":
    app.run(debug=True)
