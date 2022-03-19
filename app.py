#!/usr/bin/python
import os
from flask import Flask
from peewee import MySQLDatabase, IntegerField

MYSQL_ROOT_USER = os.getenv('MYSQL_ROOT_USER', 'root')
MYSQL_ROOT_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', 'admin')
MYSQL_ROOT_HOST = os.getenv('MYSQL_ROOT_HOST', 'localhost')
MYSQL_ROOT_PORT = os.getenv('MYSQL_ROOT_PORT', '3306')
MYSQL_ROOT_DB = os.getenv('MYSQL_ROOT_DB', 'mydb')
FLASK_APP_PORT = os.getenv('FLASK_APP_PORT', '8282')

db = MySQLDatabase(database=MYSQL_ROOT_DB, user=MYSQL_ROOT_USER, password=MYSQL_ROOT_PASSWORD,
                   host=MYSQL_ROOT_HOST, port=int(MYSQL_ROOT_PORT))

app = Flask(__name__)
app.run(host='0.0.0.0', port=int(FLASK_APP_PORT))

@app.route('/')
def get_db_version():
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    db.close()
    return "Database version : %s " % data
