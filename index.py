from bottle import *
from pymysql import connect, cursors
from re import search, compile

CONNECTION = connect(host='tsuts.tskoli.is',
                     user='1910952789',
                     password='mypassword',
                     db='1910952789_fatasida',
                     charset='utf8mb4',
                     cursorclass=cursors.DictCursor)


def get_data():
    try:
        with CONNECTION.cursor() as cursor:
            data = []
            sql = "SELECT * FROM `users`"
            cursor.execute(sql)
            users = cursor.fetchall()
            data.append(users)
            sql = "SELECT * FROM `items`"
            cursor.execute(sql)
            items = cursor.fetchall()
            data.append(items)
            sql = "SELECT * FROM `cart`"
            cursor.execute(sql)
            cart = cursor.fetchall()
            data.append(cart)
            return data
    finally:
        CONNECTION.close()


data = get_data()
# print(data)


def search_items(string):
    datalist = []
    if string == "$new":
        print("jas")
        for i in data[1]:
            if i["new"]:
                datalist.append(i["iid"])
        return datalist
    string = string.lower()
    for i in data[1]:
        if search_string(string, i):
            datalist.append(i["iid"])
    return datalist


def search_string(s, l):
    pattern = compile(s)
    if pattern.search(l["iname"].lower()) or pattern.search(l["color"]) or pattern.search(l["kind"]):
        return True
    return False


@route("/css/main.css")
def cssmain():
    return static_file("main.css", "./css")


@route("/css/normalize.css")
def cssnorm():
    return static_file("normalize.css", "./css")


@route("/img/<img:path>")
def img(img):
    return static_file(img, "./img")


@route("/")
def root():
    return template("index.tpl")


@route("/search")
def search():
    srch = request.query.s
    items = search_items(srch)
    return template("search.tpl", items=items, all=data[1])


run(host="localhost", port=8080, debug=True)
