import mysql.connector
from mysql.connector import errorcode

class Alumnos():
    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='user_agenda', 
                password='Agenda_2020',
                host='127.0.0.1',
                port=3306,
                database='escuela')
            print("Conectado")
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print("Error connect: ", e)
    
    
objeto=Alumnos()
objeto.connect()