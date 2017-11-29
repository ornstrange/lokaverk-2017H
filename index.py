from bottle import *
from sqlgenerator import *
from users import *
import smtplib


def updateData():
    data = [executeQuery(ITEMS.all()), executeQuery(USERS.all())]
    return (data, data[0], data[1], list(map(lambda x: x["uid"], data[1])))


data, items, users, uids = updateData()


def search_items(strings):
    datalist = []
    string = ""
    strings = strings.split(" ")
    if len(strings) == 1:
        string = strings[0]

    if string == "$new":
        for i in items:
            if i["new"]:
                datalist.append(i["iid"])
        return datalist
    elif string == "$dress":
        for i in items:
            if i["kind"] == "dress":
                datalist.append(i["iid"])
        return datalist
    elif string == "$top":
        for i in items:
            if i["kind"] == "top":
                datalist.append(i["iid"])
        return datalist
    elif string == "$jacket":
        for i in items:
            if i["kind"] == "jacket":
                datalist.append(i["iid"])
        return datalist

    for s in strings:
        for i in items:
            if s in i["iname"]:
                datalist.append(i["iid"])
            elif s in i["kind"]:
                datalist.append(i["iid"])
            elif s in i["color"]:
                datalist.append(i["iid"])
    return datalist


@route("/css/<css:path>")
def cssnorm(css):
    return static_file(css, "./css")


@route("/js/<js:path>")
def jsload(js):
    return static_file(js, "./js")


@route("/img/<img:path>")
def img(img):
    return static_file(img, "./img")


@route("/")
def root():
    updateData()
    return template("index.tpl")


@route("/search")
def search():
    data, items, users, uids = updateData()
    srch = request.query.s
    found = search_items(srch)
    return template("search.tpl", items=found, all=items)


@route("/sign-up", method="POST")
def sign_up():
    data, items, users, uids = updateData()

    username = request.forms.get("username")
    password = request.forms.get("password")
    email = request.forms.get("email")
    fname = request.forms.get("fname")
    lname = request.forms.get("lname")

    uid = random_uid(uids)

    if check_user(users, username):
        executeQuery(USERS.insert(data=("uid", "username", "passwd", "email", "fname", "lname"),
                     dataval=(uid, username, password, email, fname, lname)))
        # setja session á user
    else:
        # username tekið
        pass
    redirect("/")


@route("/login", method="POST")
def login():
    data, items, users, uids = updateData()

    username = request.forms.get("username")
    password = request.forms.get("password")

    if check_user(users, username, password):
        pass  # set session á þennan user
    else:
        pass  # rangt username og pass
    redirect("/")


@route("/logout")
def logout():
    # ef loggaður inn?
    redirect("/")  # taka session af þessum user


@route("/forgot", method="POST")
def forgot():
    data, items, users, uids = updateData()
    
    address = request.forms.get("email")
    
    uuid = int(list(map(lambda x: x["uid"],
                        list(filter(lambda x: x["email"] == address, users))))[0])

    rpass = random_password()

    USERS.update(data=("passwd"), dataval=(rpass), where=("uid"), whereval=(uuid))

    string =  "Hérna er nýja passwordið þitt: %s" % rpass

    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("noreply.tskoli@gmail.com", "lokaverk123")
    mail.sendmail("noreply.tskoli@gmail.com", address, string)
    mail.close()


run(host="localhost", port=8080, debug=True)
