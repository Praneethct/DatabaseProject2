from flask import Flask, request, render_template
from dbconnection import executeQuery
# from QueryParser import QueryParser
from Parser import getQuery


app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("index.html")

@app.route("/execute", methods=["POST", "GET"])
def execute():
    print((request.form["dbType"], request.form["query"]))
    query = request.form["query"].strip().strip('\n').strip('\r').strip('\r\n')
    # parser = QueryParser.getInstance()
    query = getQuery(query)
    print("Got query: ", query)
    try:
        tableHeaders, results, timeElapsed = executeQuery(query, request.form["dbType"], request.form["dbName"])
    except:
        return render_template("index.html")
    print(tableHeaders, results)
    return render_template("index.html", tableHeaders=tableHeaders, results=results, timeElapsed=timeElapsed)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)