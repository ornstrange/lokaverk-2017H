from pymysql import connect, cursors

CONNECTION = connect(host='tsuts.tskoli.is',
                     user='1910952789',
                     password='mypassword',
                     db='1910952789_fatasida',
                     charset='utf8mb4',
                     cursorclass=cursors.DictCursor)


class Sql:
    def __init__(self, table):
        self.table = table

    def all(self):
        return "SELECT * FROM " + self.table + ";"

    def select(self, data="*", where="", whereval="", operator="="):
        if isinstance(data, tuple):
            query = "SELECT " + str(data)[1:-1] + " FROM " + self.table
        else:
            query = "SELECT " + str(data) + " FROM " + self.table
        if where:
            if isinstance(where, tuple):
                if whereval != "":
                    query += " WHERE " + where[0] + \
                        " " + operator + " " + whereval[0]
                    for i in range(1, len(where)):
                        query += " AND " + where[i] + \
                            " " + operator + " " + whereval[i]
                else:
                    return "SELECT * FROM " + self.table + ";"
            else:
                query += " WHERE " + where + " " + operator + " " + whereval
        return query + ";"

    def update(self, data="*", dataval="", where="", whereval="", operator="="):
        query = "UPDATE " + self.table + " SET "
        if data != "*":
            if isinstance(data, tuple):
                query += data[0] + " = " + dataval[0]
                for i in range(1, len(data)):
                    query += ", " + data[i] + " = " + dataval[i]
            else:
                query += data + " = " + dataval
        else:
            return "SELECT * FROM " + self.table + ";"
        if where:
            if isinstance(where, tuple):
                if whereval != "":
                    query += " WHERE " + where[0] + \
                        " " + operator + " " + whereval[0]
                    for i in range(1, len(where)):
                        query += " AND " + where[i] + \
                            " " + operator + " " + whereval[i]
                else:
                    return "SELECT * FROM " + self.table + ";"
            else:
                query += " WHERE " + where + " " + operator + " " + whereval
        return query + ";"

    def delete(self, data="", where="", whereval="", operator="="):
        if isinstance(data, tuple):
            query = "DELETE " + str(data)[1:-1] + " FROM " + self.table
        else:
            query = "DELETE " + str(data) + " FROM " + self.table
        if where:
            if isinstance(where, tuple):
                if whereval != "":
                    query += " WHERE " + where[0] + \
                        " " + operator + " " + whereval[0]
                    for i in range(1, len(where)):
                        query += " AND " + where[i] + \
                            " " + operator + " " + whereval[i]
                else:
                    return "SELECT * FROM " + self.table + ";"
            else:
                query += " WHERE " + where + " " + operator + " " + whereval
        else:
            sure = input("?? ! ARE YOU SURE ! ??: ").lower()
            if sure == "yyy":
                return "DELETE FROM " + self.table
            else:
                return "SELECT * FROM " + self.table
        return query + ";"


def executeQuery(s):
    if "SELECT" in s:
        try:
            with CONNECTION.cursor() as cursor:
                cursor.execute(s)
                return cursor.fetchall()
        finally:
            cursor.close()
    else:
        try:
            with CONNECTION.cursor() as cursor:
                cursor.execute(s)
            CONNECTION.commit()
        finally:
            cursor.close()
