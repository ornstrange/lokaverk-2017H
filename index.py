from bottle import *
from sqlgenerator import *
from users import *
import smtplib
from beaker.middleware import SessionMiddleware
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# session stillingar
session_opts = {
    'session.type': 'file',
    'session.data_dir': './data',
    'session.auto': True
}

app = SessionMiddleware(app(), session_opts)
s = request.environ.get('beaker.session')


def updateData():
    data = [executeQuery(ITEMS.all()), executeQuery(
        USERS.all()), executeQuery(CART.all())]
    return (data, data[0], data[1], list(map(lambda x: x["uid"], data[1])), data[2])


data, items, users, uids, cart = updateData()


def search_items(strings):
    found, colors = [], []
    string = ""
    strings = strings.strip().split(" ")
    if len(strings) == 1:
        string = strings[0]

    if string == "$new":
        for i in items:
            if i["new"]:
                found.append(i["iid"])
                colors.append(i["color"])
        return (found, colors)
    elif string == "$dress":
        for i in items:
            if i["kind"] == "dress":
                found.append(i["iid"])
                colors.append(i["color"])
        return (found, colors)
    elif string == "$top":
        for i in items:
            if i["kind"] == "top":
                found.append(i["iid"])
                colors.append(i["color"])
        return (found, colors)
    elif string == "$jacket":
        for i in items:
            if i["kind"] == "jacket":
                found.append(i["iid"])
                colors.append(i["color"])
        return (found, colors)

    for s in strings:
        for i in items:
            if s in i["iname"].lower():
                found.append(i["iid"])
                colors.append(i["color"])
            elif s in i["kind"].lower():
                found.append(i["iid"])
                colors.append(i["color"])
            elif s in i["color"].lower():
                found.append(i["iid"])
                colors.append(i["color"])
    return (found, colors)


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
    data, items, users, uids, cart = updateData()
    return template("index.tpl")


@route("/search")
def search():
    data, items, users, uids, cart = updateData()
    srch = request.query.s
    sort = request.query.srt

    pressed = ["#000", "#FFF"]

    if sort == "":
        sort = "mu"

    found, colors = search_items(srch)
    colors = list(set(colors))

    return template("search.tpl", items=found,
                    all=items, sort=sort, srch=srch,
                    colors=colors, pressed=pressed)


@route("/item")
def item():
    data, items, users, uids, cart = updateData()
    iid = int(request.query.id)

    item = list(filter(lambda x: x["iid"] == iid, items))[0]

    return template("item.tpl", item=item)


@route("/sign-up", method="POST")
def sign_up():
    s = request.environ.get('beaker.session')
    data, items, users, uids, cart = updateData()

    username = request.forms.get("username")
    password = request.forms.get("password")
    email = request.forms.get("email")
    fname = request.forms.get("fname")
    lname = request.forms.get("lname")

    uid = random_uid(uids)

    if check_user(users, username):
        try:
            executeQuery(USERS.insert(
                data=("uid", "username", "passwd", "email", "fname", "lname"),
                dataval=(uid, username, password, email, fname, lname)))
        except Exception as error:
            return error
    else:
        return """<script>alert("Þetta notendanafn er tekið...")
                  ;window.location.replace("/");</script>"""
    redirect("/")


@route("/login", method="POST")
def login():
    s = request.environ.get('beaker.session')
    data, items, users, uids, cart = updateData()

    username = request.forms.get("username")
    password = request.forms.get("password")

    if check_user(users, username, password):
        s["user"] = username
        s["uid"] = int(list(map(lambda x: x["uid"],
                                list(filter(lambda x: x["username"] == username,
                                            users))))[0])
        return """<script>alert("Innskráning tókst\\nVelkominn aftur %s")
                  ;window.location.replace("/");</script>""" % username
    else:
        return """<script>alert("Innskráning tókst ekki\\nprufaðu username: admin, password: admin")
                  ;window.location.replace("/");</script>"""
    redirect("/")


@route("/logout")
def logout():
    s = request.environ.get('beaker.session')
    if s["user"] != "":  # taka session af þessum user
        s["user"] = ""
        s["uid"] = 0
        return """<script>alert("Þú hefur verið skráður út");window.location.replace("/");</script>"""
    redirect("/")


@route("/forgot", method="POST")
def forgot():
    data, items, users, uids, cart = updateData()

    address = request.forms.get("email")

    uuid = str(list(map(lambda x: x["uid"],
                        list(filter(lambda x: x["email"] == address, users))))[0])

    data, items, users, uids, cart = updateData()
    usern = str(list(map(lambda x: x["username"],
                         list(filter(lambda x: x["email"] == address, users))))[0])

    rpass = random_password()

    executeQuery(USERS.update(data="passwd", dataval=rpass,
                              where="uid", whereval=uuid))

    fromaddr = "noreply.tskoli@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = address
    msg['Subject'] = "Forgotten password"

    body = "Here's your new password %s: %s\nDont forget it again..." % (
        usern, rpass)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "lokaverk123")
    text = msg.as_string()
    server.sendmail(fromaddr, address, text)
    server.quit()

    redirect("/")


@route("/add-cart", method="POST")
def add_cart():
    data, items, users, uids, cart = updateData()
    s = request.environ.get('beaker.session')

    iid = request.forms.get("btn")

    try:
        if s["user"] != "":
            executeQuery(CART.insert(
                data=("uid", "iid"), dataval=(s["uid"], iid)))
        else:
            return """<script>alert("Þú verður að vera skráður inn");window.location.replace("/item?id=%s");</script>""" % iid
    except Exception as err:
        return """<script>alert("Þú verður að vera skráður inn");window.location.replace("/item?id=%s");</script>""" % iid

    redirect("/item?id=%s" % iid)


@route("/del-cart", method="POST")
def del_cart():
    data, items, users, uids, cart = updateData()
    s = request.environ.get('beaker.session')

    iid = request.forms.get("btn")

    try:
        if s["user"] != "":
            executeQuery(CART.delete(data="", where="iid", whereval=iid))
    except Exception as err:
        return """<script>alert("Villa kom upp...");window.location.replace("/cart");</script>""" % iid

    redirect("/cart")


@route("/cart")
def cart():
    data, items, users, uids, cart = updateData()
    s = request.environ.get('beaker.session')

    ucart = list(filter(lambda x: x["uid"] == s["uid"], cart))

    total = 0
    for i in ucart:
        for j in items:
            if i["iid"] == j["iid"]:
                total += j["price"]

    return template("cart.tpl", items=items, cart=ucart, total=total)


if os.environ.get('APP_LOCATION') == 'heroku':
    run(app=app, port=int(os.environ.get("PORT", 5000)))
else:
    run(app=app, port=8080, debug=True, reloader=True)
