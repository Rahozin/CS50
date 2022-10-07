# import cs50
import csv
from pandas import DataFrame, read_csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    
    # Check whether the required fields have been filled
    name = request.form.get("Name")
    # email = request.form.get("Email")
    house = request.form.get("House")
    position = request.form.get("Position")
    if not name or not house or not position:
        return render_template("error.html", message="Please, fill out all required fields")
    
    # Write data to csvfile
    with open('survey.csv', 'a', newline='') as csvfile:
        fieldnames = ['Name', 'Email', 'House', 'Position']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        try:
            read_csv('survey.csv')
        except:
            writer.writeheader()
        writer.writerow(request.form.to_dict())

    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():

    # Read and display data from csvfile
    with open('survey.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        return render_template("sheet.html", table=reader)


if __name__ == '__main__':
    app.run(debug=True)