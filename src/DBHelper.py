import psycopg2
import psycopg2.extras
import os

class DBHelper:

    def __init__(self):
        self.host = "ec2-34-237-236-32.compute-1.amazonaws.com"
        self.user = "kgyhoaojwpysgc"
        self.password = "7e551814bdbb93795220c0b02ae6e15c5038e85d0296347ec31bb336c238d170"
        self.db = "dcpo0te8jhm9oi"

    def __connect__(self):
        self.con = psycopg2.connect(host=self.host, user=self.user, password=self.password, dbname=self.db)
        self.cur = self.con.cursor()

    def __disconnect__(self):
        self.con.close()

    def fetch(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        columns = []
        for desc in self.cur.description:
            columns.append(desc.name)
        columns = tuple(columns)
        self.__disconnect__()
        return data, columns

    def execute(self, sql):
        self.__connect__()
        self.cur.execute(sql)
        self.con.commit()
        self.__disconnect__()