import mysql.connector




myconn = mysql.connector.connect(
    host ="localhost" ,
    user = "root" ,
    database = 'official_motadamn'

)
mycursor = myconn.cursor()
print('Connected')
