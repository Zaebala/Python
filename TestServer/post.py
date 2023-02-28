
class FDataBase(object):
    def __init__(self, db):
        self.db = db
        self.cur = db.cursor()

    def get_staff(self, name, size, gender):
        if name != "0" and size != "0":
            sql = f''' select name, size, price FROM {gender} where name = '{name}' and size = '{size}' '''
        elif name != "0" and size == "0":
            sql = f''' select name, size, price FROM {gender} where name = '{name}' '''
        elif name == "0" and size != "0":
            sql = f''' select name, size, price FROM {gender} where size = '{size}' '''
        else:
            sql = f''' select name, size, price FROM {gender} '''

        try:
            self.cur.execute(sql)
            res = self.cur.fetchall()
            if res: return res
        except:
            print("Ошибка бд")
        return []
