# coding=utf-8
from .base import BaseCharacter
from main.const import EXTRA_ATTACK, PERCENT_ATTACK, CRIT_RATE, CRIT_DAMAGE, RECHARGE, PHYSICAL_DAMAGE


class Eula(BaseCharacter):
    level_infos = {
        "89": {
            "base_attack": 340,
            "base_health": 13133,
            "base_defense": 746,
            "crit_damage": 88.4,
        }
    }

    def __init__(self, level=90):
        BaseCharacter.__init__(self, level)
        self.physical_damage = 0

    def calculate_damage(self, artifacts_info):
        useful_keys = [EXTRA_ATTACK, PERCENT_ATTACK, CRIT_RATE, CRIT_DAMAGE, RECHARGE, PHYSICAL_DAMAGE]
        for key in useful_keys:
            if key in artifacts_info:
                self.update(key, artifacts_info[key])

        attack = self.base_attack * (1 + (self.percent_attack / 100)) + self.extra_attack

        damage = attack * (1 + (self.crit_damage / 100)) * (1 +(self.physical_damage / 100))
        return round(damage, 2), round(self.recharge, 2), round(self.crit_rate, 2)





