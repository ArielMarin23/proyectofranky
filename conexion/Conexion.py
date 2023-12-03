import psycopg2

class Conexion:
    def __init__(self):
        self.__con = psycopg2.connect("dbname=postgres user=postgres host=localhost password=1234")

    def getConexion(self):
        return self.__con