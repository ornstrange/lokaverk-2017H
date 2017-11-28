from pymysql import connect, cursors
from bottle import *
import random
import string
import smtplib
from sqlgenerator import *

@route("/create", method="POST")
def create_user():
    conn = connect(host='tsuts.tskoli.is',
                     user='1910952789',
                     password='mypassword',
                     db='1910952789_fatasida',
                     charset='utf8mb4',
                     cursorclass=cursors.DictCursor)

    cur = conn.cursor()
    uname = request.forms.get("uname")
    psw = request.forms.get("psw")
    email = request.forms.get("email")
    fname = request.forms.get("fname")
    lname = request.forms.get("lname")
    cur.execute("INSERT INTO users Values('%s','%s','%s','%s','%s')" % (uname, psw, email, fname, lname))
    conn.commit()
    cur.close()
    conn.close()

@route("/check", method="POST")
def check_user():
    conn = connect(host='tsuts.tskoli.is',
                     user='1910952789',
                     password='mypassword',
                     db='1910952789_fatasida',
                     charset='utf8mb4',
                     cursorclass=cursors.DictCursor)
    cur = conn.cursor()
    cur.execute("SELECT username, passwd FROM users;")
    uname = request.forms.get("uname")
    psw = request.forms.get("psw")

    for i in cur:
        if i[0] == uname and i[1] == psw:
            return True
        else:
            return False
    cur.close()
    conn.close()

@route("/forgot", method="POST")
def forgot_password():
    address = request.forms.get("email")
    content = (''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase + string.ascii_letters) for i in range(10)))

    USERS = Sql("users")
    def update_password():
        update = executeQuery(USERS.update(data="passwd", dataval="'%s'",where="email", whereval="'%s'",) % content, address)
        return update
    update_password()

    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("noreply.tskoli@gmail.com", "lokaverk123")
    mail.sendmail("noreply.tskoli@gmail.com", address, content)
    mail.close()