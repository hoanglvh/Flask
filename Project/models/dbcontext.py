from pyodbc import connect
class DbContext:
    def __init__(self):
        cn = 'Driver={SQL Server};Database=BikeStore;Server=MAYTINH-0TVGJVH;Trusted_connection=yes'
        self.db = connect(cn)
    def __del__(self):
        self.db.close()
    def save(self, sql, arr):
        cur = self.db.cursor()
        cur.execute(sql, arr)
        ret = cur.rowcount
        self.db.commit()
        cur.close()
        return ret
    
    def fetchOne(self, sql, arr):
        cur = self.db.cursor()
        cur.execute(sql, arr)
        v = cur.fetchone()
        cur.close()
        return v
    
    def fetchAll(self, sql, arr=None):
        cur = self.db.cursor()
        if arr:
            cur.execute(sql, arr)
        else:
            cur.execute(sql)
        a = cur.fetchAll()
        cur.close()
        return a