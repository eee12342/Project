import os
from dotenv import load_dotenv
from flask import Flask, render_template


load_dotenv() # load environment variables

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True) # set debug to false on deployment
