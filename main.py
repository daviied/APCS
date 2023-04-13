from flask import Flask
from flask import render_template
import total_scores

app = Flask(__name__)

track = total_scores.Scores()


@app.route("/")
def home():
    return render_template('main.html')

@app.route("/get")
def get():
    return str(track)

@app.route("/current")
def current():
    return track.current()


@app.route("/small")
def small():
    total_scores.Scores.add("low")
    return render_template('main.html')


@app.route("/med")
def med():
    total_scores.Scores.add("med")
    return render_template('main.html')


@app.route("/ground")
def ground():
    total_scores.Scores.add("ground")
    return render_template('main.html')


@app.route("/high")
def high():
    total_scores.Scores.add("high")
    return render_template('main.html')


@app.route("/park")
def park():
    total_scores.Scores.add("park")
    return render_template('main.html')


@app.route("/new")
def new():
    track.new()
    return render_template('main.html')


@app.route("/history")
def history():
    return str(track)


if __name__ == "__main__":
    app.run(debug=True)
