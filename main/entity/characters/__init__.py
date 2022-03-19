# coding=utf-8

from .eula import Eula


character_dict = {
    'eula': Eula
}


def from_ch_name(ch_name):
    if ch_name not in character_dict:
        raise ValueError(f"Wrong Character name: {ch_name}")
    return character_dict.get(ch_name)
