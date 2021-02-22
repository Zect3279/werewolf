import discord

import random

from lib.roles import roles

class Player():
    def __init__(self):
        self.yes = "no"

player = Player()

class Players():
    """プレイヤー情報
    id(int): プレイヤーID
    is_dead (bool): 死亡しているか
    role(str): 職業名
    channel(discord.text_channel): 役職チャンネル
    vote_target (Optional[Player]): 投票指定した参加者
    raid_target (Optional[Player]): 襲撃指定した参加者
    fortune_target (Optional[Player]): 占い指定した参加者
    """


    def give_data(self,user: discord.User):
        player.id = user.id
        player.is_dead = False
        player.role = "市民"
        player.channel = None
        player.vote_target = None
        player.raid_target = None
        player.fortune_target = None
        return player

    def give_role(self,player_list):
        n = len(player_list)
        role = roles[n]
        role_list = random.sample(role, n)
        for i, p in enumerate(player_list):
            p.role = role_list[i]

    def make_data(self,player_list):
        data_list = []
        for p in player_list:
            data = self.give_data(p)
            data_list.append(data)
        self.give_role(data_list)
        return data_list
