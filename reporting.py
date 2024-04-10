
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import mysql.connector as dbc
import re
# CONFIG
kills=[]
teamname = ""
db = dbc.connect(
    host="",
    user="",
    database="",
    password=""
)
def getKills(attributes,role):
    cursor=db.cursor()
    sql=("SELECT "+ attributes + " FROM akumu."+ role)
    cursor.execute(sql)        
    for (e) in cursor:
        kills.append(e[0])
    return(kills)

        
var=getKills("kills","adc")
print(var)