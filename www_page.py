#!/usr/bin/python3 
from flask import Flask, request, Response 
import configparser 
from db import *

config = configparser.ConfigParser() 
config_path = '/var/www/info_server/info_server.config'
config.read(config_path) 
idb = info_database(config_path) 

def table_validate(table,config):
    tables = config["Main"]["Tables"].split(',')
    print("Tables: ", tables)
    if table in tables:
        return 0
    return 1

def return_fields(table,config):
    return config[table]["Fields"].split(',')

class response_server: 
    def __init__(self): 
        self.app = Flask(__name__) 
        @self.app.route('/info/<sub_path>', methods=["GET"]) 
        def data(sub_path): 
            if table_validate(sub_path,config) == 1:
                return Response("")
            
            fields = return_fields(sub_path,config)
            data = idb.returntop(sub_path,fields,"date")
            return Response(' '.join(str(x) for x in data))
 
serv = response_server() 
app = serv.app
