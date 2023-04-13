from flask import Flask
from flask import render_template
import total_scores

app = Flask(__name__)

track = total_scores.Scores()


@app.route("/")
def home():
    return render_template('cards_lander.html')

@app.route("/easy")
def easy():
    return render_template('game.html')

@app.route("/normal")
def normal():
    return render_template('game.html')



if __name__ == "__main__":
    app.run(debug=True)
