# coding=utf-8

from main.const import BENNETT_ATTACK, EXTRA_ATTACK, KUJOU_ATTACK, KUJOU_THUNDER, ROSARIA_CRIT, THUNDER_DAMAGE, \
    RESONANCE_ICE, RESONANCE_FIRE, REACTION_MELT, REACTION_VAPORIZE


class BaseCharacter:
    level_infos = {}

    def __init__(self, level=90):
        self.name = 'default'
        self.base_attack = 0        # 基础攻击力
        self.base_health = 0        # 基础生命
        self.base_defense = 0       # 基础防御力
        self.crit_rate = 5          # 暴击率
        self.crit_damage = 50       # 暴击伤害
        self.recharge = 100         # 元素充能
        self.mastery = 0            # 元素精通

        self.percent_attack = 0     # 百分比攻击力
        self.percent_health = 0     # 百分比生命
        self.percent_defense = 0    # 百分比防御力

        self.extra_attack = 0       # 额外攻击力
        self.extra_health = 0       # 额外生命
        self.extra_defense = 0      # 额外防御

        self.update_property_by_level(str(level))

    def update(self, key, value):
        if hasattr(self, key):
            setattr(self, key, getattr(self, key) + value)
        else:
            setattr(self, key, value)

    def update_property_by_level(self, level):
        if level not in self.level_infos:
            raise ValueError(f"wrong level: {level}")
        info = self.level_infos.get(level)
        for k, v in info.items():
            self.__setattr__(k, v)

    def equip_weapon(self, weapon):
        self.base_attack += weapon.base_attack
        for k, v in weapon.info.items():
            self.update(k, v)

    def set_extra_conditions(self, conditions):
        """
        额外条件： 班尼特/九条，元素共鸣等
        :return:
        """

        if BENNETT_ATTACK in conditions:            # 班尼特
            self.extra_attack += conditions[BENNETT_ATTACK]

        if KUJOU_ATTACK in conditions:              # 九条
            self.extra_attack += conditions[KUJOU_ATTACK]

        if KUJOU_THUNDER in conditions:             # 九条6命
            if hasattr(self, THUNDER_DAMAGE):
                setattr(self, THUNDER_DAMAGE, getattr(self, THUNDER_DAMAGE) + conditions[THUNDER_DAMAGE])
            else:
                setattr(self, THUNDER_DAMAGE, conditions[THUNDER_DAMAGE])

        if ROSARIA_CRIT in conditions:              # 罗莎莉亚
            self.crit_rate += conditions[ROSARIA_CRIT]

        if RESONANCE_ICE in conditions:             # 双冰共鸣
            self.crit_rate += 15

        if RESONANCE_FIRE in conditions:            # 双火共鸣
            self.percent_attack += 25

        if REACTION_MELT in conditions:             # 融化
            setattr(self, REACTION_MELT, True)

        if REACTION_VAPORIZE in conditions:         # 蒸发
            setattr(self, REACTION_VAPORIZE, True)

    def calculate_damage(self, artifacts_info):
        return 0







