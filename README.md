# Wordle Game

A web-based implementation of the popular Wordle game using FastAPI and modern web technologies.

## Features

- Classic Wordle gameplay with 6 attempts
- Real-time word validation using dictionary API
- Beautiful animations for wins and losses
- Virtual keyboard support
- Responsive design
- Confetti animation on winning
- Shake animation on losing

## Live Demo

[Play the game here](https://your-github-username.github.io/wordle)

## Local Development

1. Clone the repository:
```bash
git clone https://github.com/your-github-username/wordle.git
cd wordle
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python main.py
```

5. Open your browser and visit `http://localhost:8000`

## Technologies Used

- Backend:
  - FastAPI
  - Python 3.8+
  - httpx for async HTTP requests

- Frontend:
  - HTML5
  - CSS3
  - JavaScript (ES6+)
  - Canvas Confetti for animations

## API Endpoints

- `GET /`: Main game page
- `POST /guess`: Submit a guess
- `POST /reset`: Start a new game

## Contributing

Feel free to submit issues and enhancement requests! 