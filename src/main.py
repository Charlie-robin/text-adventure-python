from controller.TextAdventure import TextAdventureController
from model.GameRepository import GameRepository


game_repository = GameRepository("Leroy")
text_adventure = TextAdventureController(game_repository)
text_adventure.run()

