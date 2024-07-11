# Number Guessing Game

## Overview

This project is a simple web-based number guessing game built using Flask. The game randomly selects a number between **0** and **9**, and the user tries to guess the number through the web interface. The application provides feedback on whether the guess is too high, too low, or correct.

## Features

- Random Number Generation:

    The game generates a random number between **0** and **9** each time it starts or is reset.


- Web-Based Interface:

    The game is accessible via a web browser, providing an intuitive and user-friendly interface.


- User Feedback:

    The game provides immediate feedback on each guess, indicating if the guess is too high, too low, or correct.


- Correct Guess:
    
    Displays a success message with a green color and a congratulatory GIF.


- Low Guess:

    Displays a hint message with a blue color and a descriptive GIF.


- High Guess:

    Displays a hint message with a red color and a descriptive GIF.


- Reset Functionality:

    The game can be reset at any time, generating a new random number and allowing the user to start over.

## Usage

### Start the Game:

Access the game by navigating to the homepage. The user will be prompted to guess a number between **0** and **9**.

### Make a Guess:

Enter a number in the URL path (e.g., /5) to make a guess.

### Reset the Game:

Navigate to the `/reset` path to reset the game. This will generate a new random number and prompt the user to guess again.

## Setup

1. Ensure Flask is installed in your environment. You can install it using pip:
```bash
pip install Flask
```

2. Execute the Python script to start the Flask application:
```bash
python main.py
```

3. The application will run in debug mode and can be accessed via http://127.0.0.1:5000/.

## *Good Luck With Guessing* 🎲 *!*