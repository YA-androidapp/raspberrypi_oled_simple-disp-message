#!/usr/bin/env python3
# coding: utf-8

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import paho.mqtt.client as mqtt


OLED_WIDTH   =  128
OLED_HEIGHT  =  64

RST         =  24
DC          =  23
SPI_PORT    =  0
SPI_DEVICE  =  0

DEFAULT_FONT  =  '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'
FONT_SIZE     =  14

jpfont = ImageFont.truetype(DEFAULT_FONT, FONT_SIZE, encoding='unic')

spi = SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=spi)

gyou = [ '本日は晴天なり。',
         '本日は曇天なり。',
         '本日は雨天なり。',
         'ABCＡＢＣ123' ]


def draw_gyou():
    global gyou
    global jpfont
    global disp

    image = Image.new("1", (OLED_WIDTH, OLED_HEIGHT), 0)
    draw = ImageDraw.Draw(image)
    for i, j in enumerate(gyou):
        draw.text((0,16 * i), j, font=jpfont, fill=1)
    disp.image(image)
    disp.display()


disp.begin()
disp.clear()
disp.display()

draw_gyou()
