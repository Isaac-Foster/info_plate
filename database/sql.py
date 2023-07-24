from mysql.connector import connect
from pathlib import Path


db = connect(
    host="localhost",
    user="root",
    password="Soberano21@#",
    database="test"
)

    

cur =  db.cursor()
commit = db.commit

with open(Path(__file__).parent / Path('tables.sql')) as file:
    statements = file.read().split(';')

for statement in statements:
    cur.execute(statement)

commit()
