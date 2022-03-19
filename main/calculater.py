# coding=utf-8

from main.scan import scan_artifacts
from main.entity.characters import from_ch_name
from main.entity.artifacts import bonuses_2
from main.entity.weapons import Weapon


def merge_artifacts(artifacts):
    """
    输入5个圣遗物，计算属性和

    :param artifacts:
    :return:
    """
    result = {}
    atf_types = {}
    for atf in artifacts:
        if atf['type'] in atf_types:
            atf_types[atf['type']] += 1
        else:
            atf_types[atf['type']] = 1

        for k, v in atf['info'].items():
            if k in result:
                result[k] = result[k] + v
            else:
                result[k] = v

    bonus_set = []
    for at, count in atf_types.items():
        if count >= 2:
            bonus_set.append(at)
            if at in bonuses_2:
                for k, v in bonuses_2[at].items():
                    if k in result:
                        result[k] = result[k] + v
                    else:
                        result[k] = v

    return result, bonus_set


def calculate(character_name, character_level, weapon_name, weapon_level, conditions):
    artifacts_data = scan_artifacts()

    weapon = Weapon(weapon_name, weapon_level)

    result = []

    for at_1 in artifacts_data['flower']:
        for at_2 in artifacts_data['feather']:
            for at_3 in artifacts_data['sand']:
                for at_4 in artifacts_data['cup']:
                    for at_5 in artifacts_data['head']:
                        artifacts_set = [at_1, at_2, at_3, at_4, at_5]
                        key = '_'.join([str(atf['id']) for atf in artifacts_set])
                        artifacts_info, bonus_set = merge_artifacts(artifacts_set)
                        character = from_ch_name(character_name)(character_level)
                        character.equip_weapon(weapon)
                        character.set_extra_conditions(conditions)
                        damage, recharge, crit_rate = character.calculate_damage(artifacts_info)

                        item = {
                            "key": key,
                            "damage": damage,
                            "recharge": recharge,
                            "crit_rate": crit_rate,
                            "bonus_set": str(bonus_set)
                        }
                        result.append(item)
    result.sort(key=lambda x: x["damage"], reverse=True)
    return result



