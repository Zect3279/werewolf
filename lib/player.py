import random

from lib.roles import roles


class Player:
    def __init__(self, user_id: int):
        self.id = user_id
        self.is_dead = False
        self.role = "市民"
        self.channel = None
        self.vote_target = None
        self.raid_target = None
        self.fortune_target = None


# player = Player()

class Players:
    """プレイヤー情報
    id(int): プレイヤーID
    is_dead (bool): 死亡しているか
    role(str): 職業名
    channel(discord.text_channel): 役職チャンネル
    vote_target (Optional[Player]): 投票指定した参加者
    raid_target (Optional[Player]): 襲撃指定した参加者
    fortune_target (Optional[Player]): 占い指定した参加者
    """

    def __init__(self):
        self.users = []

    # def p_list(self,user: discord.User):
    #     p_data = self.give_data(user)
    #     self.users.append(p_data)
    #     for p in self.users:
    #         print(p.id)

    # def give_data(self,user: discord.User):
    #     player.id = user.id
    #     player.is_dead = False
    #     player.role = "市民"
    #     player.channel = None
    #     player.vote_target = None
    #     player.raid_target = None
    #     player.fortune_target = None
    #     return player

    def give_role(self, player_list):
        n = len(player_list)
        role = roles[n]
        print(role)
        random.shuffle(role)
        print(role)
        for i, p in enumerate(player_list):
            p.role = role[i]
            print(p.role)
        return player_list

    # def make_data(self):
    #     print(self.users)
    #     self.give_role(self.users)
    #     return data_list

# 作ったオブジェクトが全部同じになるバグ発生
