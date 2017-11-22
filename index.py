from bottle import *
from pymysql import connect, cursors

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


def search_items(strings):
    datalist = []
    string = ""
    strings = strings.split(" ")
    if len(strings) == 1:
        string = strings[0]

    if string == "$new":
        for i in data[1]:
            if i["new"]:
                datalist.append(i["iid"])
        return datalist
    elif string == "$dress":
        for i in data[1]:
            if i["kind"] == "dress":
                datalist.append(i["iid"])
        return datalist
    elif string == "$top":
        for i in data[1]:
            if i["kind"] == "top":
                datalist.append(i["iid"])
        return datalist
    elif string == "$jacket":
        for i in data[1]:
            if i["kind"] == "jacket":
                datalist.append(i["iid"])
        return datalist

    for s in strings:
        for i in data[1]:
            if s in i["iname"]:
                datalist.append(i["iid"])
            elif s in i["kind"]:
                datalist.append(i["iid"])
            elif s in i["color"]:
                datalist.append(i["iid"])
    return datalist


@route("/css/main.css")
def cssmain():
    return static_file("main.css", "./css")


@route("/css/normalize.css")
def cssnorm():
    return static_file("normalize.css", "./css")

@route("/js/main.js")
def jsmain():
    return static_file("main.js", "./js")

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
    print(items)
    return template("search.tpl", items=items, all=data[1])

run(host="localhost", port=8080, debug=True)
