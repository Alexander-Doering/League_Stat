
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import mysql.connector as dbc
import re
# CONFIG
teamname = ""
db = dbc.connect(
    host="",
    user="",
    database="",
    password=""
)

def getValues(attributes,table):
    value=[]
    cursor=db.cursor()
    sql=("SELECT "+ attributes + " FROM akumu."+ table + " INNER JOIN teams ON " + table +  ".GameID=teams.GameID WHERE teams.teamname=" + '"{}"'.format(teamname))
    cursor.execute(sql)        
    for (e) in cursor:
        value.append(e[0])
    vctr = np.array(value)
    return(vctr)
    
var1=getValues("kills","adc")
var2=getValues("assists","adc")
var3=getValues("deaths","adc")
kda=np.add(var1,var2)/var3
categories=["1","2","3","4","5","6","7"]
plt.bar(categories ,kda, color='skyblue')
plt.xlabel('Game Nr.')
plt.ylabel('KDA')
plt.title('ADC KDA per Game')
plt.show()