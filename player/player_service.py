from service import Service
from helpers import client
from models import Player


class PlayerService(Service):
    __model__ = Player

    def search(self, player_name):
        result = client.get_player(player_name)
        self._create_from(result)

    def refresh(self, model):
        player_data = client.get_player(player_name=model.name)

        self.update(model, **player_data)

        return model

    def _create_from(self, data):
        if data.get('id'):
            player = self.__model__(**data)
            self.save(player)
