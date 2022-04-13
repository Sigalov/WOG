from flask import render_template
from Score import read_score_from_file
from flask import Flask

app = Flask(__name__)
@app.route('/')
def score_server():
    try:
        file, score = read_score_from_file()
        return render_template('score.html', score=str(score))
    except Exception as e:
        return render_template('error.html', error=e)