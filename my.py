from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    print(url_for("index"))
    return render_template("index.html")

@app.route("/api/<navigation>")
def navigation(navigation):
    return navigation


if __name__ == "__main__":
    app.run(debug=True)
