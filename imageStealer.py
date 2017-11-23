from pymysql import connect, cursors
from PIL import Image
import io
import requests


CONNECTION = connect(host='tsuts.tskoli.is',
                     user='1910952789',
                     password='mypassword',
                     db='1910952789_fatasida',
                     charset='utf8mb4',
                     cursorclass=cursors.DictCursor)


def get_data():
    try:
        with CONNECTION.cursor() as cursor:
            sql = "SELECT iid, img FROM `items`"
            cursor.execute(sql)
            items = cursor.fetchall()
            return items
    finally:
        CONNECTION.close()


data = get_data()

for i in data:
    r = requests.get("http://"+i["img"])
    image_file = io.BytesIO(r.content)
    img = Image.open(image_file)
    basewidth = 600
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save("item-%d.jpg" % (i["iid"]))