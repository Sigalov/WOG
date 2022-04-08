import sys

from Live import welcome, load_game_web
from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/start')
def start():
    return render_template('welcome.html')

@app.route('/load_game/<game_id>/<game_diff>')
def load_game(game_id, game_diff):
    print('Hello world!', file=sys.stdout)
    return load_game_web(game_id, game_diff)

@app.route('/start_new_game', methods=['GET', 'POST'])
def start_new_game():
    if request.method == 'POST':
        game_id_ = request.form['game_id']
        game_difficulty_ = request.form['game_diff']
        return redirect(url_for('load_game', game_id=game_id_,game_diff=game_difficulty_))
    else:
        game_id_ = request.args.get('game_id')
        game_difficulty_ = request.args.get('game_diff')
        return redirect(url_for('load_game', game_id=game_id_,game_diff=game_difficulty_))



@app.route('/success/<name>/<last>')
def success(name, last):
    return f'welcome {name} {last}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user, last='blabla'))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user, last='blabla'))


if __name__ == '__main__':
    app.run(debug=True)



# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

# gamer_name = 'Oleg'
# welcome(gamer_name)
# load_game()


