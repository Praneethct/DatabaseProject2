from flask import Flask, request, render_template
from dbconnection import executeQuery


app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("index.html")

@app.route("/execute", methods=["POST", "GET"])
def execute():
    print((request.form["dbType"], request.form["query"]))
    query = request.form["query"].strip().strip('\n').strip('\r').strip('\r\n')
    tableHeaders, results, time1 = executeQuery(query, request.form["dbType"])
    print(tableHeaders, results)
    return render_template("index.html", tableHeaders=tableHeaders, results=results, time1=time1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
