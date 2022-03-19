# coding=utf-8

import json
import re

replace_dict = {
    'lifeStatic': 'extra_health',
    'attackStatic': 'extra_attack',
    'defendStatic': 'extra_defense',
    'attackPercentage': 'percent_attack',
    'lifePercentage': 'percent_health',
    'defendPercentage': 'percent_defense',
    'elementalMastery': 'mastery',
    'recharge': 'recharge',
    'criticalDamage': 'crit_damage',
    'critical': 'crit_rate',

    'physicalBonus': 'physical_damage',
    'fireBonus': 'fire_damage',
    'iceBonus': 'ice_damage',
    'thunderBonus': 'thunder_damage',
    # '': 'water_damage',
    # '': 'wind_damage',
    # '': 'rock_damage',
    # '': 'grass_damage',
    'cureEffect': 'heal_addition',
    'paleFlame': 'cang_bai',
    'emblemOfSeveredFate': 'jue_yuan',
    'oceanHuedClam': 'hai_ran',
    'shimenawaReminiscence': 'zhui_yi',
    'wandererTroupe': 'yue_tuan',
    'gladiatorFinale': 'jue_dou',
    'noblesseOblige': 'zong_shi',
    'tenacityOfTheMillelith': 'qian_yan',
    # '': 'bing_tao',
    # '': 'ru_lei',
    # '': 'ping_lei',
    # '': 'mo_nv',
    # '': 'du_huo',
    'huskOfOpulentDreams': 'hua_guan',
    # '': 'chen_lun',
    'bloodstainedChivalry': 'ran_xie',
    # '': '',


}


def replace_number(match):
    num = match.group(0)
    c = float(num) * 100
    return str(round(c, 1))



def main():
    data = json.loads(open('origin_data.json', 'r', encoding='utf-8').read())
    print(list(data.keys()))
    print(data['flower'][0])

    keys = ['flower', 'feather', 'sand', 'cup', 'head']
    result = {k: [] for k in keys}

    for key in keys:
        artifacts = data[key]
        for i, atf in enumerate(artifacts):
            info = {}
            info[atf['mainTag']['name']] = atf['mainTag']['value']
            for tag in atf['normalTags']:
                info[tag['name']] = tag['value']
            item = {
                'id': i,
                'type': atf['setName'],
                'info': info
            }
            result[key].append(item)

    out_data = json.dumps(result, indent=4)
    for k, v in replace_dict.items():
        out_data = out_data.replace(k, v)

    out_data = re.sub(r'0\.\d+', replace_number, out_data)

    with open('artifacts.json', 'w', encoding='utf-8') as f:
        f.write(out_data)


if __name__ == '__main__':
    main()