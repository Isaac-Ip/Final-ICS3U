#!/usr/bin/env python3

# Created by: Isaac Ip
# Created on: Oct 2026
# This program is the "Space Aliens" program on the PyBadge

import stage
import ugame
import random
import time
import supervisor

import constants


def splash_scene():
    blue_heart = stage.Bank.from_bmp16("blue_heart.bmp")
    blue = stage.Sprite(
        blue_heart, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))


if __name__ == "__main__":
    splash_scene()
