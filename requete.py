import mysql.connector

host = 'localhost'
userdb = 'root'
password = 'azerty'
database = 'palworld_database'

def connect(self):
    connection = mysql.connector.connect(
        host=host,
        user=userdb,
        password=password,
        database=database
    )
    self.cursor = connection.cursor()

def disconnect(self):
    self.connection.close()
    
# def add_user(self, surname, name, pseudo, email, password, photo, id_role):
#     sql = "INSERT INTO user (surname, name, pseudo, email, password, photo, id_role) VALUES (%s, %s, %s, %s, %s, %s, %s)"
#     values = (surname, name, pseudo, email, password, photo, id_role)
#     self.execute_query(sql, values)

# a
def count_size(self,id):
    sql = "SELECT Size, COUNT(*) FROM hidden-attribute GROUP BY Size ORDER BY COUNT(*) DESC;"
    values = (id,)
    return self.fetch_one(sql,values)

# b
def count_size(self,id):
    sql = "SELECT GenusCategory, COUNT(*) FROM hidden-attribute GROUP BY GenusCategory ORDER BY COUNT(*) DESC;"
    values = (id,)  
    return self.fetch_one(sql,values)

# c
def count_size(self,id):
    sql = "SELECT HP, COUNT(*) FROM hidden-attribute GROUP BY HP ORDER BY COUNT(*) DESC;"
    values = (id,)  
    return self.fetch_one(sql,values)