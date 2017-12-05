#import postgres interface for python
import psycopg2
import os
import json
import pandas as pd
from IPython.display import display

#keeping output from each cell a little smaller for easy scrolling.
pd.set_option('display.max_rows',14)

with open('config.json') as f:
    conf = json.load(f) 

postgres_string = "dbname='{database}' user='{user}' host='{host}' password='{passw}'".format(**conf)

relative_data_path = '../../Data/SQL'
database_filename = 'clubdata.sql'

try:
    conn = psycopg2.connect("dbname='exercises' user='james' host='localhost' password='fakepassword'")
except:
    print("couldn't connect")
cursor = conn.cursor()

#helper function for printing. For better jupyter formatting, I'm just using panda's built in read function. 
def print_output(query):
    global conn
    display(pd.read_sql_query(query, conn))
