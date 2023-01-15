import psycopg2

class Database:
    def __init__(self, dbname='postgres'):
        self.conn = psycopg2.connect(dbname=dbname)
    
    def __enter__(self):
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cur.close()
        self.conn.close()


def setup_database():
    with Database() as cur:
        databse_user: str = str(input("Enter your database username: "))
        databse_password: str = str(input("Enter your database password: "))
        database_name: str = str(input("Enter your database name: "))

        # Create the database user
        cur.execute("CREATE USER {databse_user} PASSWORD '{databse_password}'".format(
            databse_user=databse_user,
            databse_password=databse_password
        ))

        # Create the new database
        cur.execute("CREATE DATABASE {database_name}".format(
            database_name=database_name
        ))

        # Grant the new user all privileges on the new database
        cur.execute("GRANT ALL PRIVILEGES ON DATABASE {database_name} TO {databse_user}".format(
            database_name=database_name,
            databse_user=databse_user
        ))

        # Additional
        cur.execute("ALTER ROLE {databse_user} SET client_encoding TO 'utf8'".format(
            databse_user=databse_user
        ))
        cur.execute("ALTER ROLE {databse_user} SET default_transaction_isolation TO 'read committed'".format(
            databse_user=databse_user
        ))
        cur.execute("ALTER ROLE {databse_user} SET timezone TO 'UTC'".format(
            databse_user=databse_user
        ))

setup_database()