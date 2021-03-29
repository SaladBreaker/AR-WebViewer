from flask import Flask, render_template

app = Flask(__name__)


@app.route("/burger")
def burger():
    return render_template("index.html", model_path="/models/burger.glb")


@app.route("/burger2")
def burger2():
    return render_template("index.html", model_path="/models/burger2.glb")


@app.route("/panda")
def panda():
    return render_template("index.html", model_path="/models/pandas.glb")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
