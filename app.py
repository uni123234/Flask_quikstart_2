"""
This module contains a simple Flask application with three routes:
- '/' for the index page
- '/page1' for page1
- '/page2' for page2
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Render the index page."""
    return render_template("index.html")


@app.route("/page1")
def page1():
    """Render page1."""
    return render_template("page1.html")


@app.route("/page2")
def page2():
    """Render page2."""
    return render_template("page2.html")


if __name__ == "__main__":
    app.run(debug=True)
