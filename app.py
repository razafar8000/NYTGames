"""
NYT Games Clone - Flask Application
Main application entry point for the web-based game suite.
"""

from flask import Flask, render_template, request, session, jsonify, redirect, url_for
import sys
import os

# Add project root to path for imports
sys.path.insert(0, os.path.dirname(__file__))
sys.path.append(os.path.abspath('WordRepository'))
sys.path.append(os.path.abspath('SpellingBee'))

from wordle.WordleController import WordleController
from SpellingBee.SpellingBeeController import SpellingBeeController

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')


# ==================== HOMEPAGE ====================

@app.route('/')
def index():
    """Render the homepage with available games."""
    return render_template('index.html')


# ==================== WORDLE GAME ====================

@app.route('/wordle')
def wordle():
    """Initialize or resume Wordle game session."""
    return render_template('wordle.html')


@app.route('/wordle/start', methods=['POST'])
def wordle_start():
    """Start a new Wordle game."""
    controller = WordleController()
    # Store game state in session
    session['wordle_secret'] = controller.getSecretWord()
    session['wordle_guesses'] = []
    session['wordle_active'] = True
    session.modified = True
    return jsonify({'status': 'started'})


@app.route('/wordle/guess', methods=['POST'])
def wordle_guess():
    """
    Process a Wordle guess.
    Expects JSON: {'guess': 'apple'}
    Returns: game state with guess evaluation
    """
    data = request.get_json()
    guess = data.get('guess', '').lower()

    if not guess or len(guess) != 5:
        return jsonify({'error': 'Invalid guess length'}), 400

    # Check if game is active
    if 'wordle_secret' not in session or 'wordle_guesses' not in session:
        return jsonify({'error': 'No active game. Start a new game first.'}), 400

    # Validate the guess using controller
    controller = WordleController()
    for char in guess:
        controller.onKeyPress(char)
    
    # Check if word is valid before processing
    if not controller.isValid(guess):
        return jsonify({'error': 'Not a valid word'}), 400

    # Get secret word from session
    secret_word = session['wordle_secret']
    guesses_made = session['wordle_guesses']

    # Process the guess using Guess class
    from wordle.Guess import Guess
    guess_obj = Guess(guess, secret_word)
    
    # Store guess evaluation
    guess_data = {
        'word': guess,
        'evaluation': [guess_obj.getLetterEval(i) for i in range(5)]
    }
    guesses_made.append(guess_data)
    session['wordle_guesses'] = guesses_made
    session.modified = True

    # Check win/loss conditions
    guess_count = len(guesses_made)
    is_won = guess == secret_word
    is_lost = guess_count >= 6 and not is_won

    # Format response
    response = {
        'guess_count': guess_count,
        'is_won': is_won,
        'is_lost': is_lost,
        'guesses': guesses_made
    }

    if is_won or is_lost:
        response['secret_word'] = secret_word

    return jsonify(response)


@app.route('/wordle/reset', methods=['POST'])
def wordle_reset():
    """Reset the Wordle game."""
    session.pop('wordle_secret', None)
    session.pop('wordle_guesses', None)
    session['wordle_active'] = False
    session.modified = True
    return jsonify({'status': 'reset'})


# ==================== PLACEHOLDER ROUTES (for future games) ====================

@app.route('/spelling-bee')
def spelling_bee():
    """Spelling Bee game (to be implemented)."""
    return render_template('spellingbee.html', game='Spelling Bee')

@app.route('/spelling_bee/start', methods=['POST'])
def spellingBeeStart():
    #create session
    spellingBeeController = SpellingBeeController()
    session["SpellingBee"] = spellingBeeController
    
    usableLetters = spellingBeeController.getUsableLetters()
    points = spellingBeeController.getGamePoints()

    return jsonify({"usableLetters": usableLetters})

@app.route('/spelling_bee/spellingBeeGuess')
def submitAnswer():
    print("hello")
    return None





# ================================================================================


@app.route('/tictactoe')
def tictactoe():
    """Tic-Tac-Toe game (to be implemented)."""
    return render_template('coming_soon.html', game='Tic-Tac-Toe')


# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('500.html'), 500


# ==================== MAIN ====================

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
