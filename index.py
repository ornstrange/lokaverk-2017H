from bottle import *
from sqlgenerator import *

ITEMS = Sql("items")
USERS = Sql("users")


def updateData():
    data = [executeQuery(ITEMS.all()), executeQuery(USERS.all())]
    return data


data = updateData()
items, users = data[0], data[1]


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
    updateData()
    srch = request.query.s
    found = search_items(srch)
    return template("search.tpl", items=found, all=items)


run(host="localhost", port=8080, debug=True)
