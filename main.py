from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Dict
import uvicorn

from game import Game
from word_manager import WordManager

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Initialize word manager and game
word_manager = WordManager()
game = Game(word_manager)

class GuessRequest(BaseModel):
    word: str

@app.get("/", response_class=HTMLResponse)
async def get_game(request: Request):
    """Render the game page."""
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "word_length": word_manager.get_word_length(),
            "max_attempts": game.max_attempts
        }
    )

@app.post("/guess")
async def make_guess(guess_request: GuessRequest):
    """Make a guess in the game."""
    try:
        evaluation = await game.make_guess(guess_request.word)
        return {
            "evaluation": evaluation,
            "game_state": game.get_game_state()
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/reset")
async def reset_game():
    """Reset the game with a new word."""
    game.reset()
    return {"message": "Game reset successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 