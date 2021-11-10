# greenhouse

Raspberry Pi **Greenhouse** 🍁

## config edited

in /boot/config.txt

```
hdmi_force_hotplug=1
boot_delay=3
```

## cron

```
*/5 * * * * python3 /home/pi/projects/greenhouse/main.py
```
