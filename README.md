# Raspberry Pi Wake Word Detection

_This repository is part of the Twitch series, "Voice + Robotics", found at [https://twitch.tv/amazonalexa/](https://twitch.tv/amazonalexa)._

Following this code will allow you to test a connection between an Amazon Echo device that is paired via BlueTooth to a Raspberry Pi. In this example, the Raspberry Pi is equipped with a [Sense HAT](https://www.raspberrypi.org/products/sense-hat/), which provides an 8x8 LED matrix and sensors like an accelerometer, gyroscope, and more. The LED matrix will be used to show the succesful connection between the Raspberry Pi and Echo.

## Steps

### Register your gadget – Follow the instructions in Register a Gadget to register your gadget with the Alexa Voice Service (AVS) using the developer portal.

- Take note of your Amazon ID and Alexa Gadget Secret when you've completed the initial setup

### Setup Your Raspberry Pi

You'll first want to setup your Raspberry Pi with the [latest version of Raspbian](https://www.raspberrypi.org/downloads/raspbian/). 

Then, you'll need to install the Alexa Gadgets Toolkit. The easiest way to setup the Alexa Gadgets Toolkit is to clone the sample repo at [https://github.com/alexa/Alexa-Gadgets-Raspberry-Pi-Samples](https://github.com/alexa/Alexa-Gadgets-Raspberry-Pi-Samples) and follow the instructions to configure your Raspberry Pi and register it as a gadget. 

### Pair your Raspberry Pi with your Echo via BlueTooth

You'll need to put your Raspberry Pi into Pairing Mode. First, make sure a BlueTooth adapter is connected to your Raspberry Pi. Then, SSH into your Pi and check the BlueTooth status:

```bash
$ service bluetooth status
bluetooth.service - Bluetooth service
Loaded: loaded (/lib/systemd/system/bluetooth.service; enabled; vendo
Active: active (running) since Wed 2019-08-28 09:04:56 CDT; 3h 16min
    Docs: man:bluetoothd(8)
Main PID: 304 (bluetoothd)
    Status: "Running"
    Tasks: 1 (limit: 2077)
Memory: 1.8M
...
```

As you can see in the example above, we have a status of `RUNNING`. If it is not running, run it with

    $ service bluetooth start

Once running, we want to prep the BlueTooth agent for pairing. First, enter into BlueTooth control mode by typing `bluetoothctl` in your terminal:

    $ bluetoothctl
    Agent registered
    [bluetooth]# power on
    Changing power on succeeded
    [bluetooth]# agent on
    Agent is already registered

The agent is running, so let's scan for devices. 

    [bluetooth]# scan on
    Discovery started
    [CHG] Controller 00:F:7B:EA:21:18 Discovering: yes
    [NEW] Device E6:9A:49:6A:F0:4B 45-9A-AA-6A-E5-4B
    [NEW] Device E7:9A:AA:8C:E5:1A OfficeJet 5200 series
    [NEW] Device C3:3A:9D:EC:AC:64 Tile
    [NEW] Device 7C:C3:02:D1:D0:B5 7C-C3-02-D1-D0-B5
    [NEW] Device F8:86:04:2E:99:F1 [TV] UN82JW650B

At this point, we want put our Echo into pairing mode. This varies from device to device, but in many cases, you can say

    Alexa, pair BlueTooth

The scan should find your device,

    [NEW] Device 74:22:C2:46:CE:11 Echo-2BA

Note the device ID (`74:22:C2:46:CE:11`), stop the scan, and pair:

    [bluetooth]# scan off
    [bluetooth]# pair 74:22:C2:46:CE:11
    Attempting to pair with 74:22:C2:46:CE:11
    [CHG] Device 74:22:C2:46:CE:11 Connected: yes

Once you see the `Connected: yes` status, you'll have successfully paired your Raspberry Pi with your Echo. When troubleshooting, you can see your paired devices with

    [bluetooth]# paired-devices
    Device 74:22:C2:46:CE:11 Echo-2BA

## Code for your Raspberry Pi

You'll need two files on your Raspberry Pi for this to work, which can be found in the `device` folder. Change the values of `wakeword-sample.ini` to match those that you took note of when you registered your gadget. Then, change the filename to `wakeword.ini`.

From you terminal, run

    python3 wakeword.py

## Resources

- [https://github.com/alexa/Alexa-Gadgets-Raspberry-Pi-Samples](https://github.com/alexa/Alexa-Gadgets-Raspberry-Pi-Samples)
- [Bluetooth Commands](https://www.raspberrypi.org/forums/viewtopic.php?t=214373)
- [https://github.com/alexa/Alexa-Gadgets-Raspberry-Pi-Samples/tree/master/src/examples/colorcycler](https://github.com/alexa/Alexa-Gadgets-Raspberry-Pi-Samples/tree/master/src/examples/colorcycler)