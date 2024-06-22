# 3keys_1knob
Custom firmware for a 3-key + rotary encoder macropad (https://hackaday.io/project/189914)

### dependencies

#### MacOS
```bash
brew install srecord
brew install sdcc
```
#### Debian
```bash
apt install -y srecord sdcc
```

#### Wchisp
Install wchisp by following this page: https://github.com/ch32-rs/wchisp (rust needed)
```bash
# tldr; (for macos)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
brew install libusb
cargo install wchisp --git https://github.com/ch32-rs/wchisp
```


#### PyUSB (for flashing script)
```bash
pip3 install pyusb
```

### compile:
`make bin`

### compile & flash to pad:
- if on original firmware: connect P1.5 to GND and connect USB (or P3.6 to 3v3 if using ch55xduino)
- if on this firmware: press key1 while connecting USB (key opposite from knob)
- `make flash`

### configure keys:
1. `wchisp eeprom dump flashdata.bin`
2. `./tools/keybin.py flashdata.bin A B c D E F 0xFF 0xFF 0x80 0xFF 0xFF 0xFF`
- A..F is your normal keys: LeftTap, MiddleTap, RightTap, KnobTap, KnobRight, KnobLeft
- 0xFF are modifiers (like CTRL), each for one normal key (use 0xFF if you don't need modifiers)
3. `wchisp eeprom write flashdata.bin`
4. Here is a [list for all modifier hex codes](include/usb_conkbd.h)
