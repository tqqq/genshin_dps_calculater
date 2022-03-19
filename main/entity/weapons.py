# coding=utf-8

# TODO: sqlite

WEAPONS = {
    "xue_zang": {
        "level": {
            "90": {
                "base_attack": 565,
                "info": {
                    "physical_damage": 34.5
                }
            }
        },
        "refinement": {}
    }

}


class Weapon:
    def __init__(self, name, level=90, refinement=0):
        self.name = name
        self.level = level
        self.refinement = refinement

        level_info = WEAPONS[name]["level"].get(str(level))
        ref_info = WEAPONS[name]["refinement"].get(str(refinement))

        if not level_info:
            raise ValueError(f"no data for lv {level} {name}")

        self.base_attack = level_info["base_attack"]
        self.info = level_info["info"]

        if ref_info:
            for k, v in ref_info.items():
                if k in self.info:
                    self.info[k] += v
                else:
                    self.info[k] = v

