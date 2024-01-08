 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """Renders the main page of the website."""
    return render_template('index.html')

# Define the lessons route
@app.route('/lessons')
def lessons():
    """Renders the lessons page of the website."""
    return render_template('lessons.html')

# Define the history route
@app.route('/history')
def history():
    """Renders the history page of the website."""
    return render_template('history.html')

# Define the quiz route
@app.route('/quiz')
def quiz():
    """Renders the quiz page of the website."""
    return render_template('quiz.html')

# Define the submit quiz route
@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    """Handles the submission of the quiz and provides feedback to the user."""

    # Get the user's answers from the request
    answers = request.form.getlist('answer')

    # Check the user's answers and calculate the score
    score = 0
    for answer in answers:
        if answer == 'correct_answer':
            score += 1

    # Provide feedback to the user
    return render_template('quiz_results.html', score=score)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
