"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.channel_controller import ChannelController
from .orders.game_controller import GameController
from .orders.message_controller import MessageController
from .orders.server_controller import ServerController
from .orders.user_controller import UserController
from .orders.role_controller import RoleController



channel_controller = ChannelController()
game_controller = GameController()
message_controller = MessageController()
server_controller = ServerController()
user_controller = UserController()
role_controller = RoleController()
