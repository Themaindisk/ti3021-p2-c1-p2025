import orcaledb
import os
from dotenv import load_dotenv

load_dotenv()

un = "SYS"
cs = "localhost/orclpdb"
pw = "INACAP" #

with oracledb.connect(user = un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = "select sysdate from dual"
        for r in cursor.execute(sql):
            print(r)
            
            
