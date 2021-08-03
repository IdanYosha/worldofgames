from flask import Flask, render_template
from Utils import *

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        scores_file = open(SCORES_FILE_NAME, "r")
        SCORE = int(float(scores_file.readline()))
        return render_template('World of Games scores.html', SCORE=SCORE)
    except:
        return render_template('World of Games error.html', ERROR=BAD_RETURN_CODE)


if __name__ == '__main__':
    app.run(debug=True)
