from flask import Flask, request, redirect, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Use your Atlas connection string with your credentials
client = MongoClient(
    "mongodb+srv://potthuruvenkataumeshchandra_db_user:Q1rNRNmg5mvmoxvl@umeshcluster.zmltzwr.mongodb.net/mydatabase?retryWrites=true&w=majority"
)

# Select database and collection
db = client["mydatabase"]
collection = db["mycollection"]

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        try:
            name = request.form.get("name")
            email = request.form.get("email")

            # Insert into MongoDB
            collection.insert_one({"name": name, "email": email})

            # Redirect to success page
            return redirect("/success")
        except Exception as e:
            error = str(e)

    # Render form with error if any
    return render_template("form.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
