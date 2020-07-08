import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Node:

    def __init__(self, user_name, password, db_name ):

        self.totalVotes = 0         #possibly obsolete
        self.con = psycopg2.connect(dbname='postgres',
        user=user_name, host='localhost',
        password=password)

        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.cur = self.con.cursor()

        self.cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(db_name))
        )

        self.con = psycopg2.connect(dbname=db_name,
        user=user_name, host='localhost',
        password=password)

        self.con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.cur = self.con.cursor()

        self.cur.execute("CREATE TABLE Votes (id serial PRIMARY KEY, vote integer, Name varchar, Surname varchar);")

        self.con.commit()

    def insert(self,vote,name,surname):
        postgres_insert_query = """ INSERT INTO Votes (vote, Name, Surname) VALUES (%s,%s,%s)"""
        record_to_insert = (vote, name, surname)
        try:
            self.cur.execute(postgres_insert_query, record_to_insert)
            self.con.commit()
        except:
            return -1

    def getTotalVotes(self);

        self.cur.execute("SELECT COUNT(*) FROM Votes;")
        return self.cur.fetchall()




    
