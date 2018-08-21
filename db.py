#!/usr/bin/python3
import hashlib
import configparser
import sqlite3

class info_database:

    def __init__(self,config):
        try:
            Config = configparser.ConfigParser()
            Config.read(config)
            self.db = Config['Main']['Database']
        except:
            print("Config Error!")
            exit()
        try:    
            self.connect()
        except:
            print("Database Error!")

    def close(self):
        self.conn.close()

    def connect(self):
        self.conn = sqlite3.connect(self.db)
        self.cur = self.conn.cursor()

    def execute(self,command):
        self.connect()
        self.cur.execute(command)
        self.conn.commit()
        text_return = self.cur.fetchall()
        self.close()
        return text_return

    def executevar(self,command,operands):
        self.connect()
        self.cur.execute(command,operands)
        self.conn.commit()
        text_return = self.cur.fetchall()
        self.close()
        return text_return

    def returntop(self,table,fields,sort_field):
        querystr = "SELECT " + ','.join(fields) +" FROM "+ table + " ORDER BY " + sort_field + " DESC LIMIT 1"
        topVal = self.execute(querystr)
        if topVal == []:
            return topVal
        else:
            return topVal[0]
