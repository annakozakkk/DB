
# orders DB
from .orders.channel_dao import ChannelDAO
from .orders.game_dao import GameDAO
from .orders.user_dao import UserDAO
from .orders.server_dao import ServerDAO
from .orders.message_dao import MessageDAO
from .orders.role_dao import RoleDAO


game_dao = GameDAO()
channel_dao = ChannelDAO()
user_dao = UserDAO()
server_dao = ServerDAO()
message_dao = MessageDAO()
role_dao = RoleDAO()
