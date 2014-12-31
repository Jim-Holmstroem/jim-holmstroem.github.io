---
layout: post
title: "Fix for Yun not showing as hotspot in Ubuntu"
date: 2014-12-30 23:00:00
categories: network
---
I'm currently running Ubuntu 12.04 and trying to setup my newly bought
Arduino Yun when I by accident entered the Wifi password with the wrong caps
(step 7 in [arduino yun - getting started](http://fibasile.github.io/arduino-yun-getting-started.html)).
For some reason the Arduino Yun hotspot whouldn't show up even after WLAN reset, Factory reset of the entire system (WLAN reset for 30 seconds), disconnecting Wifi and put it back on (I realized now that I didn't try to restart Wifi with the hardware button on my computer).

Make sure your "wifi interface" is named ``wlan0`` (I think it is the most common name for it)

~~~ bash
ls /sys/class/net
~~~

~~~ bash
sudo ip link set dev wlan0 down
sudo dhclient -r wlan0
sudo ip link set dev wlan0 up
~~~

After this operations my wlan autoconnected to my home network so
I force disconnected it and ran (otherwise the Wifi would be busy):

Then after scanning

~~~ bash
sudo iwlist wlan0 scan | grep ESSID
~~~

The Yun was showing up again, it also showed up in the ordinary network drop-down.

Everything started to work as expected after this.

See [Scan for Wireless Network](https://help.ubuntu.com/community/WifiDocs/Scan_for_Wireless_Network) guide for more information (note that not all wireless interface cards supports ``scan``)
