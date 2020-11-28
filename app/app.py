from flask import Flask, request, render_template
from dbconnection import executeQuery
import requests

app = Flask(__name__)
query = ""
database = ""

@app.route("/", methods=["POST", "GET"])
def mainPage():

    global query
    global database


    if not query:
        return render_template("index.html")

    # print((request.form["dbType"], query))
    cleanedQuery = query.strip().strip('\n').strip('\r').strip('\r\n')
    tableHeaders, results, timeElapsed = executeQuery(cleanedQuery, "rds", database)
    # print(tableHeaders, results)
    return render_template("index.html", tableHeaders=tableHeaders, results=results, timeElapsed=timeElapsed)
    # return {"headers":tableHeaders, "results": results, "timeElapsed": timeElapsed}


@app.route("/updateQuery", methods=["POST", "GET"])
def updateQuery():
    global query
    global database

    data = request.get_json()
    query = data['query']
    database = data['database']

    return {"status": True}

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
