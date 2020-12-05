import psycopg2
import psycopg2.extras
import os

class DBHelper:

    def __init__(self):
        self.host = "ec2-34-200-116-132.compute-1.amazonaws.com"
        self.user = "ueeyxooovikpdg"
        self.password = "8fc08da44fdbdbb57807b56500f16c7526d2cf40389240508f7c3249e8401ba4"
        self.db = "d9guqu6qkhksd6"

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