from sprite_object import *
from npc import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = ('resources/sprites/npc/')
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.animated_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_sprite(AnimatedSprite(game,pos = (1.5,1.5)))
        add_sprite(AnimatedSprite(game,pos = (14.5,1.5)))
        add_sprite(AnimatedSprite(game,pos = (1.5,12.5)))
        add_sprite(AnimatedSprite(game,pos = (14.5,12.5)))
        #npc
        add_npc = self.add_npc
        self.npc_positions = {}
        add_npc(NPC(game))
        add_npc(CacoDemonNPC(game, pos=(5.5, 16.5)))
        add_npc(CyberDemonNPC(game, pos=(14.5, 20.5)))


    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_npc(self,npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
