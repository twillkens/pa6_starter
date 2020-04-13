"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app

app = Flask(__name__)

global state
state = {'guesses': [],
         'word': "interesting",
         'word_so_far': "----------",
         'done': False}


@app.route('/')
@app.route('/main')
def main():
    return render_template('hangman.html')


@app.route('/tom-bio')
def tom_bio():
    # demonstrate basic approach for bio page
    # explain how the route relates to the address bar
    # explain how extend works with fancylayout.html
    return render_template('tom-bio.html')


@app.route('/start')
def start():
    global state
    # explain how the state dictionary is used
    # demonstrate how code can be reused from the module
    state['word'] = hangman_app.generate_random_word() # generate_random_word() only returns 'cat' in this case
    state['guesses'] = []

    word_so_far = hangman_app.get_word_so_far(state['word'])  # this shows how we change the state dictionary
                                                              # now get_word_so_far() returns hyphens equal to length of word
    state['word_so_far'] = word_so_far
    print(state)  # printing can be seen only in terminal, not on web page
    return render_template("start.html",
                           state=state,
                           game_type='word game')  # shows how arguments can be passed in and used in jinja


@app.route('/play', methods=['GET', 'POST'])
def play_hangman():
    """ plays hangman game """
    global state
    if request.method == 'GET':
        return start()

    elif request.method == 'POST':
        # no need to get very deep with how get/post works
        # just that this is what comes from hitting the submit button
        letter = request.form['guess']
        state['guesses'] += [letter]
        print(state)  # run this a number of times and show them how the list grows in terminal as well as web page
        return render_template('play.html', state=state)


if __name__ == '__main__':
    app.run('0.0.0.0', port=3000)
