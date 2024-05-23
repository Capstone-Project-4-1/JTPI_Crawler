import mysql.connector

class DB_Connecter:
    def __init__(self, host, user, password, database_name):
        self.host = host
        self.user = user
        self.password = password
        self.database_name = database_name

    def __enter__(self):
        self.cnx = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database_name
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cnx:
            self.cnx.commit() 
            self.cnx.close()

    def insert_data(self, data): # 수정필요
        cursor = self.cnx.cursor()
        try:
            query = "INSERT INTO table_name (column_name) VALUES (%s)"  # 수정 필요
            cursor.execute(query, (data,)) #샘플 코드 
            self.cnx.commit()
        except Exception as e:
            print(f"Failed to insert data: {e}")
        finally:
            cursor.close()