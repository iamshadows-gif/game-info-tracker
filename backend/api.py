from fastapi import FastAPI,HTTPException,status
from fastapi.middleware.cors import CORSMiddleware  #corsmiddleware helps frontend to talk to the fastapi. then fastapi allows that the frontend ios allowed.
from pydantic import BaseModel
from database.game_functions import get_games,get_game,add_game,update_game,delete_game

app = FastAPI()

app.add_middleware(
    CORSMiddleware,     
    allow_origins=["*"],
    allow_methods=["*"],        #this is the functioning of corsmiddleware
    allow_headers=["*"],
)

class Game(BaseModel):              #What a game looks like when we SEND it back
    id: int
    name: str
    release_date: str
    developer: str
    publisher: str | None
    rating: float | None


@app.get("/")
def home():
    return {"message": "Game info Tracker API is running"}


@app.get("/games", response_model=list[Game])
def games():
    games = get_games()

    return [
        {
            "id": game[0],
            "name": game[1],
            "release_date": game[2],
            "developer": game[3],
            "publisher": game[4],
            "rating": game[5]
        }
        for game in games
    ]

@app.get("/games/{game_id}")
def game(game_id:int):
    game = get_game(game_id)

    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
   
    return {
        "id":game[0],
        "name":game[1],
        "release_date":game[2],
        "developer":game[3],
        "publisher":game[4],
        "rating":game[5]
    }

class GameCreate(BaseModel):          #what the client must SEND to create one
    name:str
    release_date:str
    developer:str
    publisher:str | None
    rating:float | None

@app.post("/games",status_code=201)
def create_game(game:GameCreate):
    game_id = add_game(
        game.name,
        game.release_date,
        game.developer,
        game.publisher,
        game.rating
    )

    return {
        "message":"Game Created!",
        "id":game_id
    }
class GameUpdate(BaseModel):
    rating:float

@app.patch("/games/{game_id}")
def update_game_endpoint(game_id:int,game:GameUpdate):

    existing_game = get_game(game_id)

    if existing_game is None:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )

    update_game(
        game_id,
        game.rating
    )

    updated_game = get_game(game_id)

    return {
        "id":updated_game[0],
        "name":updated_game[1],
        "release_date":updated_game[2],
        "developer":updated_game[3],
        "publisher":updated_game[4],
        "rating":updated_game[5]
    }

@app.delete("/games/{game_id}")
def delete_game_endpoint(game_id: int):

    existing_game = get_game(game_id)
    if existing_game is None:
        raise HTTPException(
            status_code=404,
            detail="Game not found"
        )
    delete_game(game_id)

    return{
        "message":"Game deleted"
    }
