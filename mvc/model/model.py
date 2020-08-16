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
    
    def select(self):
        try:
            self.connect()
            query=('SELECT * FROM alumnos;')
            self.cursor.execute(query)
            result=[]
            for row in self.cursor:
                r = {
                    'id_persona' : row[0],
                    'nombre' : row[1],
                    'ap_paterno' : row[2],
                    'ap_materno' : row[3],
                    'edad' : row[4],
                    'fecha_nac' : row[5],
                    'genero' : row[6],
                    'estado' : row[7],
                    }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print("Error Select: ", e)
            result =[]
            return result

objeto=Alumnos()
objeto.connect()

for row in objeto.select():
    print(row)