from flask import Flask, render_template, redirect, url_for
from game_logic import BadmintonGame

app = Flask(__name__)
game = BadmintonGame()

@app.route("/")
def index():
    return render_template("index.html", game=game)

@app.route("/point/<player>")
def point(player):
    if not game.match_winner():
        game.add_point(player)
    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    global game
    game = BadmintonGame()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
