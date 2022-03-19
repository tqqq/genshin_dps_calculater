# coding=utf-8

import csv
from main.calculater import calculate


def main():
    conditions = {
        "rosaria_crit": 13.5,
        "resonance_ice": True
    }

    data = calculate(character_name='eula', character_level=89, weapon_name="xue_zang", weapon_level=90,
                     conditions=conditions)

    output_data = [list(d.values()) for d in data]

    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(output_data)


if __name__ == '__main__':
    main()
