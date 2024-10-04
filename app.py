from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# API to get flashcards
@app.route('/get_flashcards', methods=['GET'])
def get_flashcards():
    # You can fetch from DB or JSON (simulate for now)
    flashcards = [
        {"word": "cat", "translation": "gato", "language": "Spanish"},
        {"word": "dog", "translation": "perro", "language": "Spanish"},
        # Add more flashcards
    ]
    return jsonify(flashcards)
@app.route('/flashcards')
def flashcards():
    return render_template('flashcards.html')

user_progress = {}

@app.route('/update_progress', methods=['POST'])
def update_progress():
    data = request.json
    # Store performance and adjust card order based on correctness
    user_progress[data['word']] = data['correct']
    return jsonify(success=True)
@app.route('/games')
def games():
    return render_template('games.html')



if __name__ == '__main__':
    app.run(debug=True)
