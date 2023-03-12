#!/bin/bash

#optional
#sudo systemctl stop serial-getty@ttyS0.service
sudo ifconfig usb0 up
sudo minicom -D /dev/ttyUSB2
