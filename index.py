from bottle import *
from pymysql import *

connection = connect(host='tsuts.tskoli.is',
											user='1910952789',
											password='mypassword',
											db='1910952789_fatasida',
											charset='utf8mb4',
											cursorclass=cursors.DictCursor)

def getData():
	try:
		with connection.cursor() as cursor:
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
		connection.close()

data = getData()

print(data)

# leita í data[1] -> data[1][1 - 3]
# nær í data[1][0] á þeim sem hittir og bætir í lista, og returnar þeim lista
def search_items(string):
	datalist = []
	for i in data[1]:
		if string in [i["iname"], i["kind"], i["color"]]:
			datalist.append(i["iid"])
	return datalist

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
	items = search_items(srch)
	return str(items)

run(host="localhost", port=8080, debug=True)