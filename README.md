# zoom-keyboard
A bluetooth keyboard for controlling the Zoom application, based on an [Adafruit NeoTrellis](https://www.adafruit.com/product/3954) and [Feather nRF52840 Express](https://www.adafruit.com/product/4062).


## Dependencies

## Bill of Materials

- 1 x [Feather nRF52840 Express]()
- 1 x [Lithium Ion Polymer Battery - 3.7v 500mAh](https://www.adafruit.com/product/1578)
- 1 x [Mini Panel Mount DPDT Toggle Switch](https://www.adafruit.com/product/3220)
- 1 x [4x4 NeoTrellis Acrylic Enclosure and Hardware kit](https://www.adafruit.com/product/4339)
- 1 x [NeoTrellis RGB Driver PCB for 4x4 keypad](https://www.adafruit.com/product/3954)
- 1 x [Silicon Elastomer 4x4 Button Keypad](https://www.adafruit.com/product/1611)
- 1 x [JST PH 4-pin to Male Header Cable - I2C STEMMA Cable 200mm](https://www.adafruit.com/product/3955)
- 1 x [Little Rubber Bumper Feet](https://www.adafruit.com/product/550)

Instead of buying the enclosure, PCB, elastomer, cable and bumpers, you could get the NeoTrellis kit pack that includes them all (and you'll have a spare Feather M4 Express for some other project):

- 1 x [4x4 NeoTrellis Feather Kit Pack](https://www.adafruit.com/product/4352)

## Assembly

Adafruit has a nice tutorial that explains the assembly of the enclosure: https://learn.adafruit.com/neotrellis-feather-case-assembly

One thing that is important to note is that you'll have to modify the Feather nRF52840 slightly to get it to fit in the enclosure. The board has a shrouded connector in the center for its SWD port, and this interferes with mounting the Feather. I found the it was easiet to pull the plastic shroud off before desoldering the pins.

## Customizing the build

Although I used a Feather nRF52840 Express and a NeoTrellis with the enclosure kit, there are a whole host of ways to customize or expand on this build. For example, you could swap out the Feather nRF52840 and replace it with another Feather that supports HID, like the M4 Express included in the kit pack, and use this as a wired keyboard rather than BLE-based.

