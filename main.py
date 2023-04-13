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
    track.small()
    return render_template('main.html')


@app.route("/med")
def med():
    track.med()
    return render_template('main.html')


@app.route("/ground")
def ground():
    track.ground()
    return render_template('main.html')


@app.route("/high")
def high():
    track.high()
    return render_template('main.html')


@app.route("/park")
def park():
    track.park()
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
