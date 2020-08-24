import psycopg2
import random
import time
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Node:

    def __init__(self, user_name, password, db_name ):

        self.totalVotes = 0         #possibly obsolete
        self.con = psycopg2.connect(dbname='postgres',
        user=user_name, host='localhost',
        password=password)
        self.db_name = db_name

        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.cur = self.con.cursor()

        self.cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(db_name))
        )

        self.con = psycopg2.connect(dbname=self.db_name,
        user=user_name, host='localhost',
        password=password)

        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE Votes (id serial PRIMARY KEY, Vote integer, Vote_id bigint,id_number bigint, Name varchar, Surname varchar);")

        self.con.commit()

    def insert(self,vote,vote_id,id_number, name,surname,test=False):
        postgres_insert_query = """ INSERT INTO Votes (Vote, Vote_id, id_number, Name, Surname) VALUES (%s,%s,%s,%s,%s)"""
        record_to_insert = (vote, vote_id,id_number, name, surname)

        #randomly "drop" the connection if test=True
        if(test):
            drop = bool(random.getrandbits(1))
            if(drop):
                sleep_time = random.uniform(200, 3000)
                time.sleep(sleep_time/1000)
                print("%s: Vote not saved (Timeout)" % self.db_name)
                return -2          #code for timeout


        try:
            self.cur.execute(postgres_insert_query, record_to_insert)
            self.con.commit()
            return 1
        except:
            return -1

    def getTotalVotes(self):

        self.cur.execute("SELECT COUNT(*) FROM Votes;")
        res=self.cur.fetchall()
        return res[0][0]