import psycopg2
import random
import select
import time
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Node:

    def __init__(self, user_name, password, db_name, mode='sync'):

        self.totalVotes = 0  # possibly obsolete
        self.con = psycopg2.connect(dbname='postgres',
                                    user=user_name, host='localhost',
                                    password=password)
        self.db_name = db_name
        self.user_name = user_name
        self.password = password

        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self.cur = self.con.cursor()

        self.cur.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(db_name))
        )

        if(mode=='sync'):
            self.con = psycopg2.connect(dbname=self.db_name,
                                    user=user_name, host='localhost',
                                    password=password)
            self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        else:
            self.con = psycopg2.connect(dbname=self.db_name,
                                    user=user_name, host='localhost',
                                    password=password, async=1)
            self.wait(self.con)

        self.cur = self.con.cursor()

        self.cur.execute(
            "CREATE TABLE Votes (id serial PRIMARY KEY, Vote integer, Vote_id bigint,id_number bigint, Name varchar, Surname varchar);")
        if(mode!='sync'):
            self.wait(self.con)
            self.cur.close()
            self.con.close()

    def insert(self, vote, vote_id, id_number, name, surname, test=False):
        postgres_insert_query = """ INSERT INTO Votes (Vote, Vote_id, id_number, Name, Surname) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (vote, vote_id, id_number, name, surname)

        # randomly "drop" the connection if test=True
        if (test):
            '''
            drop = bool(random.getrandbits(1))
            if (drop):
                sleep_time = random.uniform(200, 3000)
                time.sleep(sleep_time / 1000)
                print("%s: Vote not saved (Timeout)" % self.db_name)
                return -2  # code for timeout
            '''
            postgres_insert_query  = """select pg_sleep(30); """ + postgres_insert_query

        try:
            self.cur.execute(postgres_insert_query, record_to_insert)
            return 1
        except:
            return -1

    def insert_async(self, vote, vote_id, id_number, name, surname, test=False):
        postgres_insert_query = """ INSERT INTO Votes (Vote, Vote_id, id_number, Name, Surname) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (vote, vote_id, id_number, name, surname)

        self.con = psycopg2.connect(dbname=self.db_name,
                                    user=self.user_name, host='localhost',
                                    password=self.password, async=1)
        self.wait(self.con)

        # randomly "drop" the connection if test=True
        if (test):
            drop = bool(random.getrandbits(1))
            if (drop):
                sleep_time = random.uniform(200, 3000)
                time.sleep(sleep_time / 1000)
                print("%s: Vote not saved (Timeout)" % self.db_name)
                return -2  # code for timeout

        try:
            self.cur = self.con.cursor()
            self.cur.execute(postgres_insert_query, record_to_insert)
            self.cur.close()
            self.con.close()
            return 1
        except:
            self.cur.close()
            self.con.close()
            return -1

    def getTotalVotes(self):

        self.cur.execute("SELECT COUNT(*) FROM Votes;")
        res = self.cur.fetchall()
        return res[0][0]

    def wait(self,conn):
        while True:
            state = conn.poll()
            if state == psycopg2.extensions.POLL_OK:
                break
            elif state == psycopg2.extensions.POLL_WRITE:
                select.select([], [conn.fileno()], [])
            elif state == psycopg2.extensions.POLL_READ:
                select.select([conn.fileno()], [], [])
            else:
                raise psycopg2.OperationalError("poll() returned %s" % state)