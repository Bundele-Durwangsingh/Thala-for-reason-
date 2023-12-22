from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/thala", methods=["POST"])
def thala():
    str = request.form.get("str")
    count = len(re.findall("[a-zA-Z]", str))
    print("Count of Alphabets: ", count)
    if count == 7:
        return render_template("index.html", label=1)
    else:
        return render_template("index.html", label=-1)


if __name__ == "__main__":
    app.run(debug=False)
