- [greenhouse](#greenhouse)
  - [config](#config)

# greenhouse

Raspberry Pi **Greenhouse** 🍁

## config

### boot

in `/boot/config.txt`

```
hdmi_force_hotplug=1
boot_delay=3
```

### cron

```
*/1 * * * * python3 /home/pi/projects/greenhouse/main.py
*/1 * * * * python3 /home/isaac/greenhouse/chicauma.py
```
