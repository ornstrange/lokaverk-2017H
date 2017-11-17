from bottle import *
from pymysql import *

connection = connect(host='tsuts.tskoli.is',
											user='1910952789',
											password='mypassword',
											db='1910952789_fatasida',
											charset='utf8mb4',
											cursorclass=cursors.DictCursor)

@route("/css/main.css")
def cssmain():
	return static_file("main.css", "./css")

@route("/css/normalize.css")
def norm():
	return static_file("normalize.css", "./css")

@route("/img/<img:path>")
def img(img):
	return static_file(img, "./img")

@route("/")
def root():
	return template("index.tpl")

@route("/search")
def root():
	srch = request.query.s
	return srch

run(host="localhost", port=8080, debug=True)