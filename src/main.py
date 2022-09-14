from controller.GameController import GameController
from controller.UserController import UserController

user_controller = UserController()
user_controller.run()

game_controller = GameController(user_controller.get_user())
game_controller.run()
