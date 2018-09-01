# WhyCarNotGo: The world's simplest OBD-II scanner for ELM327-compatible interfaces

**WhyCarNotGo** can report the Diagnostic Trouble Codes (DCT) that are making your car's check engine light turn on, potentially saving you an expensive trip to the mechanic.

WhyCarNotGo is based on the extremely useful [python-OBD library](https://github.com/brendan-w/python-OBD).

## Installation

```
git clone https://github.com/adamnovak/whycarnotgo.git
cd whycarnotgo
pip install --process-dependency-links --trusted-host github.com --no-cache-dir .
```

The extra weird pip arguments are necessary to install a python-OBD version that has fixed [#101](https://github.com/brendan-w/python-OBD/issues/101). You may also need to add `--user`, or run `pip` with `sudo`, depending on your environment.

## Usage

1. Make sure you have the drivers to talk to your OBD-II reader. For my USB ELM327 interface, with a Prolific 2303 USB-to-serial chip, and my Mac, I had to install the [Prolific drivers for OS X](http://www.prolific.com.tw/us/showproduct.aspx?p_id=229&pcid=41). Linux users should have any needed drivers already.

2. Plug your OBD-II reader into your vehicle and connect it to your computer.

3. Run the program:

```
whycarnotgo
```

4. Interpret the results:

```
[('P0441', 'Evaporative Emission System Incorrect Purge Flow'), ('P0455', 'Evaporative Emission System Leak Detected (large leak)')]
```

