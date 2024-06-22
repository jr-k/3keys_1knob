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

#### Whcisp
Install whcisp by following this page: https://github.com/ch32-rs/wchisp (rust needed)

### compile:
`$ make bin`

### compile & flash to pad:
- if on original firmware: connect P1.5 to GND and connect USB
- if on this firmware: press key1 while connecting USB
- `$ make flash`

### configure keys:
1. `$ wchisp eeprom dump flashdata.bin`
2. edit first 6 bytes of this binary (3 keys, plus 3 for the knob), and write it back:
3. `$ wchisp eeprom write flashdata.bin`
