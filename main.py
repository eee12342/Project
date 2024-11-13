import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# import forms from forms.py
from forms import ContentType


load_dotenv() # load environment variables

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_KEY")
bootstrap = Bootstrap(app)


# create and initialise database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# DATABASE TABLES
class Book(db.Model):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # user filled columns
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(250), unique=False, nullable=True)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_rating():
    form = ContentType()
    if form.validate_on_submit():
        if form.content_type.data == "Book":
            pass # UNFINISHED
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True) # set debug to false on deployment
