import psycopg2
import MySQLdb
# import pyodbc


def executeQuery(query, dbType):

    if dbType.lower() == "redshift":
        with psycopg2.connect("dbname=database1 host=redshift-server-instacart.cxrld0xhd2yp.us-east-1.redshift.amazonaws.com port=5439 user=admin1 password=12345abcdE") as con:
            with con.cursor() as cur:
                cur.execute(query)
                tableHeaders = [i[0] for i in cur.description]
                results = cur.fetchall()
                return tableHeaders, results
    elif dbType.lower() == "rds":
        with MySQLdb.connect(host="instacart.ctn7lp6tviib.us-east-1.rds.amazonaws.com", user="admin1", passwd="12345abcdE", db="instacart") as con:
            with con.cursor() as cur:
                cur.execute(query)
                tableHeaders = [i[0] for i in cur.description]
                results = cur.fetchall()
                return tableHeaders, results
    return [], []




                