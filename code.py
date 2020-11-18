'''
NeoTrellis/nrf52840 Feather Zoom Keyboard

(c) 2020 George White

MIT License
'''

import time
from board import SDA, SCL
from adafruit_neotrellis.neotrellis import NeoTrellis

import busio

import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c_bus = busio.I2C(SCL, SDA)
trellis = NeoTrellis(i2c_bus)
hid = HIDService()

KEYCOUNT = 16

OFF = (0,0,0)
ON = (125,125,125)
RED = (125,0,0)
GREEN = (0,125,0)
BLUE = (0,0,125)

k = Keyboard(hid.devices)
kl = KeyboardLayoutUS(k)

# define the buttons and positions
def send(event):
    if event.edge == NeoTrellis.EDGE_FALLING:
        trellis.pixels[event.number] = BLUE
        if event.number == 15:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.A) # mute/unmute
        elif event.number == 14:
           k.release(Keycode.SPACE) # turn off push to talk (when muted)
        elif event.number == 13:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.V) # disable/enable camera
        elif event.number == 12:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.N) # swap cameras
        elif event.number == 11:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.H) # show/hide chat
        elif event.number == 10:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.S) # start share
        elif event.number == 9:
            k.send(Keycode.COMMAND, Keycode.U) # show/hide participants 
        elif event.number == 8:
            k.send(Keycode.COMMAND, Keycode.I) # invite
        elif event.number == 7:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.W) # speaker/gallery view switch
        elif event.number == 6:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.M) # enter/leave minimal view
        elif event.number == 5:
           k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.F) # enter/leave full screen
        elif event.number == 4:
            k.send(Keycode.COMMAND,Keycode.SPACE) # use Spotlight to open Zoom or switch Zoom windows
            time.sleep(0.01)
            kl.write("zoom.us\n")
        elif event.number == 3:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.R) # record locally
        elif event.number == 2:
            k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.C) # record in the cloud
        elif event.number == 1:
             k.send(Keycode.SHIFT, Keycode.COMMAND, Keycode.P) # pause recording (either mode)        
        elif event.number == 0: 
            k.send(Keycode.COMMAND, Keycode.W) # leave meating
    elif event.edge == NeoTrellis.EDGE_RISING:
        trellis.pixels[event.number] = ON
        if event.number == 14:
             k.press(Keycode.SPACE) # turn on push to talk 

for i in range(KEYCOUNT):
    # activate rising edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_RISING)
    # activate falling edge events on all keys
    trellis.activate_key(i, NeoTrellis.EDGE_FALLING)
    # set all keys to trigger the blink callback
    trellis.callbacks[i] = send

    # cycle the LEDs on startup
    trellis.pixels[i] = GREEN
    time.sleep(0.05)

for i in range(KEYCOUNT):
    trellis.pixels[i] = BLUE

device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,
                                manufacturer="Stonehippo")
advertisement = ProvideServicesAdvertisement(hid)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "ZoomKeys HID"

ble = adafruit_ble.BLERadio()
if not ble.connected:
    print("advertising")
    ble.start_advertising(advertisement, scan_response)
else:
    print("connected")
    print(ble.connections)

while True:
    while not ble.connected:
        pass
    print("Start typing:")

    while ble.connected:
        trellis.sync()
        time.sleep(0.02)

    ble.start_advertising(advertisement)
