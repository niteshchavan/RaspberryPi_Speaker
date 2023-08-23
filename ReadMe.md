nitesh@zero:~ $
nitesh@zero:~ $
nitesh@zero:~ $ pulseau
-bash: pulseau: command not found
nitesh@zero:~ $ alsamixer
nitesh@zero:~ $ amixer
Simple mixer control 'Speaker',0
  Capabilities: pvolume pswitch pswitch-joined
  Playback channels: Front Left - Front Right - Rear Left - Rear Right - Front Center - Woofer - Side Left - Side Right
  Limits: Playback 0 - 197
  Mono:
  Front Left: Playback 108 [55%] [-16.69dB] [on]
  Front Right: Playback 108 [55%] [-16.69dB] [on]
  Rear Left: Playback 105 [53%] [-17.25dB] [on]
  Rear Right: Playback 105 [53%] [-17.25dB] [on]
  Front Center: Playback 105 [53%] [-17.25dB] [on]
  Woofer: Playback 105 [53%] [-17.25dB] [on]
  Side Left: Playback 105 [53%] [-17.25dB] [on]
  Side Right: Playback 105 [53%] [-17.25dB] [on]
Simple mixer control 'PCM',0
  Capabilities: cvolume cswitch cswitch-joined
  Capture channels: Front Left - Front Right
  Limits: Capture 0 - 6928
  Front Left: Capture 4096 [59%] [-0.01dB] [on]
  Front Right: Capture 4096 [59%] [-0.01dB] [on]
Simple mixer control 'PCM Capture Source',0
  Capabilities: enum
  Items: 'Mic' 'Line' 'IEC958 In' 'Mixer'
  Item0: 'Mic'
Simple mixer control 'Line',0
  Capabilities: pvolume cvolume pswitch pswitch-joined cswitch cswitch-joined
  Playback channels: Front Left - Front Right
  Capture channels: Front Left - Front Right
  Limits: Playback 0 - 8065 Capture 0 - 6928
  Front Left: Playback 6144 [76%] [-0.01dB] [off] Capture 0 [0%] [-16.00dB] [off]
  Front Right: Playback 6144 [76%] [-0.01dB] [off] Capture 0 [0%] [-16.00dB] [off]
Simple mixer control 'Mic',0
  Capabilities: pvolume cvolume pswitch pswitch-joined cswitch cswitch-joined
  Playback channels: Front Left - Front Right
  Capture channels: Front Left - Front Right
  Limits: Playback 0 - 8065 Capture 0 - 6928
  Front Left: Playback 6144 [76%] [-0.01dB] [off] Capture 4096 [59%] [-0.01dB] [on]
  Front Right: Playback 6144 [76%] [-0.01dB] [off] Capture 4096 [59%] [-0.01dB] [on]
Simple mixer control 'IEC958 In',0
  Capabilities: cswitch cswitch-joined
  Capture channels: Mono
  Mono: Capture [on]
nitesh@zero:~ $ cd /etc/pulse/
nitesh@zero:/etc/pulse $ ls
client.conf  client.conf.d  daemon.conf  default.pa  system.pa
nitesh@zero:/etc/pulse $ sudo nano default.pa
nitesh@zero:/etc/pulse $ systemctl --user start pulseaudio
Failed to start pulseaudio.service: Unit pulseaudio.service is masked.
nitesh@zero:/etc/pulse $ sudo apt purge bluealsa
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Package 'bluealsa' is not installed, so not removed
The following packages were automatically installed and are no longer required:
  libice6 libpulsedsp libsm6 libspeexdsp1 libwebrtc-audio-processing1 pulseaudio-utils rtkit
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
nitesh@zero:/etc/pulse $ sudo apt install pulseaudio-module-bluetooth
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  pulseaudio
Suggested packages:
  pavumeter paprefs
The following NEW packages will be installed:
  pulseaudio pulseaudio-module-bluetooth
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 1,194 kB of archives.
After this operation, 6,501 kB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://archive.raspberrypi.org/debian bullseye/main armhf pulseaudio armhf 14.2-2+rpt1 [1,107 kB]
Get:2 http://archive.raspberrypi.org/debian bullseye/main armhf pulseaudio-module-bluetooth armhf 14.2-2+rpt1 [87.5 kB]
Fetched 1,194 kB in 2s (489 kB/s)
Selecting previously unselected package pulseaudio.
(Reading database ... 56304 files and directories currently installed.)
Preparing to unpack .../pulseaudio_14.2-2+rpt1_armhf.deb ...
Unpacking pulseaudio (14.2-2+rpt1) ...
Selecting previously unselected package pulseaudio-module-bluetooth.
Preparing to unpack .../pulseaudio-module-bluetooth_14.2-2+rpt1_armhf.deb ...
Unpacking pulseaudio-module-bluetooth (14.2-2+rpt1) ...
Setting up pulseaudio (14.2-2+rpt1) ...
Setting up pulseaudio-module-bluetooth (14.2-2+rpt1) ...
Processing triggers for dbus (1.12.24-0+deb11u1) ...
Processing triggers for man-db (2.9.4-2) ...
nitesh@zero:/etc/pulse $ sudo usermod -a -G bluetooth nitesh
nitesh@zero:/etc/pulse $ systemctl --user restart pulseaudio
Failed to restart pulseaudio.service: Unit pulseaudio.service is masked.
nitesh@zero:/etc/pulse $ sudo reboot
Connection to 192.168.0.125 closed by remote host.
Connection to 192.168.0.125 closed.

C:\Users\Admin>ssh nitesh@192.168.0.125
nitesh@192.168.0.125's password:
Linux zero 6.1.21+ #1642 Mon Apr  3 17:19:14 BST 2023 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Aug 23 22:17:10 2023 from 192.168.0.105
nitesh@zero:~ $ pacmd list-sinks
1 sink(s) available.
  * index: 0
        name: <alsa_output.hw_1_0>
        driver: <module-alsa-sink.c>
        flags: HARDWARE DECIBEL_VOLUME LATENCY DYNAMIC_LATENCY
        state: SUSPENDED
        suspend cause: IDLE
        priority: 9040
        volume: front-left: 65536 / 100% / 0.00 dB,   front-right: 65536 / 100% / 0.00 dB
                balance 0.00
        base volume: 65536 / 100% / 0.00 dB
        volume steps: 65537
        muted: no
        current latency: 0.00 ms
        max request: 0 KiB
        max rewind: 0 KiB
        monitor source: 0
        sample spec: s16le 2ch 44100Hz
        channel map: front-left,front-right
                     Stereo
        used by: 0
        linked by: 0
        configured latency: 0.00 ms; range is 0.50 .. 2000.00 ms
        module: 5
        properties:
                alsa.resolution_bits = "16"
                device.api = "alsa"
                device.class = "sound"
                alsa.class = "generic"
                alsa.subclass = "generic-mix"
                alsa.name = "USB Audio"
                alsa.id = "USB Audio"
                alsa.subdevice = "0"
                alsa.subdevice_name = "subdevice #0"
                alsa.device = "0"
                alsa.card = "1"
                alsa.card_name = "ICUSBAUDIO7D"
                alsa.long_card_name = "ICUSBAUDIO7D at usb-20980000.usb-1, full speed"
                alsa.driver_name = "snd_usb_audio"
                device.bus_path = "platform-20980000.usb-usb-0:1:1.0"
                sysfs.path = "/devices/platform/soc/20980000.usb/usb1/1-1/1-1:1.0/sound/card1"
                udev.id = "usb-0d8c_USB_Sound_Device-00"
                device.bus = "usb"
                device.vendor.id = "0d8c"
                device.vendor.name = "C-Media Electronics, Inc."
                device.product.id = "0102"
                device.product.name = "CM106 Like Sound Device"
                device.serial = "0d8c_USB_Sound_Device"
                device.string = "hw:1,0"
                device.buffering.buffer_size = "352800"
                device.buffering.fragment_size = "176400"
                device.access_mode = "mmap+timer"
                device.description = "CM106 Like Sound Device"
                device.icon_name = "audio-card-usb"
nitesh@zero:~ $ pacmd list-sources
1 source(s) available.
  * index: 0
        name: <alsa_output.hw_1_0.monitor>
        driver: <module-alsa-sink.c>
        flags: DECIBEL_VOLUME LATENCY DYNAMIC_LATENCY
        state: SUSPENDED
        suspend cause: IDLE
        priority: 1000
        volume: front-left: 65536 / 100% / 0.00 dB,   front-right: 65536 / 100% / 0.00 dB
                balance 0.00
        base volume: 65536 / 100% / 0.00 dB
        volume steps: 65537
        muted: no
        current latency: 0.00 ms
        max rewind: 0 KiB
        sample spec: s16le 2ch 44100Hz
        channel map: front-left,front-right
                     Stereo
        used by: 0
        linked by: 0
        configured latency: 0.00 ms; range is 0.50 .. 2000.00 ms
        monitor_of: 0
        module: 5
        properties:
                device.description = "Monitor of CM106 Like Sound Device"
                device.class = "monitor"
                device.icon_name = "audio-input-microphone"
nitesh@zero:~ $ pacmd set-default-sink "alsa_output.hw_1_0" | index
-bash: index: command not found
nitesh@zero:~ $ pacmd set-default-sink "alsa_output.hw_1_0"
nitesh@zero:~ $ pacmd set-default-source "alsa_output.hw_1_0.monitor"
nitesh@zero:~ $ pacmd set-sink-volume index volume
Failed to parse volume.
nitesh@zero:~ $ pulseaudio -k
nitesh@zero:~ $ bluetoothctl
Agent registered
[CHG] Controller B8:27:EB:03:0F:5F Pairable: yes
[bluetooth]# discoverable on
Changing discoverable on succeeded
[CHG] Controller B8:27:EB:03:0F:5F Discoverable: yes
[CHG] Device C8:16:DA:62:1D:E8 Connected: yes
Request confirmation
[agent] Confirm passkey 640965 (yes/no): yes
[CHG] Device C8:16:DA:62:1D:E8 Connected: no
[CHG] Device C8:16:DA:62:1D:E8 Connected: yes
[CHG] Device C8:16:DA:62:1D:E8 Connected: no
[CHG] Device C8:16:DA:62:1D:E8 Connected: yes
[CHG] Device C8:16:DA:62:1D:E8 Connected: no
[bluetooth]# pacmd list-sinks | grep -e 'name:' -e 'index:'
[bluetooth]# quit
nitesh@zero:~ $ pacmd list-sinks | grep -e 'name:' -e 'index:'
No PulseAudio daemon running, or not running as session daemon.
nitesh@zero:~ $ reboot
Failed to set wall message, ignoring: Interactive authentication required.
Failed to reboot system via logind: Interactive authentication required.
Failed to open initctl fifo: Permission denied
Failed to talk to init daemon.
nitesh@zero:~ $ sudo reboot
nitesh@zero:~ $ Connection to 192.168.0.125 closed by remote host.
Connection to 192.168.0.125 closed.

C:\Users\Admin>ssh nitesh@192.168.0.125
nitesh@192.168.0.125's password:
Linux zero 6.1.21+ #1642 Mon Apr  3 17:19:14 BST 2023 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Aug 23 22:23:18 2023 from 192.168.0.105
nitesh@zero:~ $ pactl list short sinks
0       alsa_output.hw_1_0      module-alsa-sink.c      s16le 2ch 44100Hz       IDLE
nitesh@zero:~ $ pacmd set-default-sink 0
nitesh@zero:~ $ pactl list short sink-inputs
nitesh@zero:~ $ paplay
.asoundrc                 .bash_logout              .config/                  .local/                   .profile
.bash_history             .bashrc                   file_example_WAV_2MG.wav  nohup.out                 sample-12s.wav
nitesh@zero:~ $ paplay sample-12s.wav
^Cnitesh@zero:~ $ bluetooth
-bash: bluetooth: command not found
nitesh@zero:~ $ bluetoothctl
Agent registered
[CHG] Controller B8:27:EB:03:0F:5F Pairable: yes
[bluetooth]# discoverable on
Changing discoverable on succeeded
[CHG] Controller B8:27:EB:03:0F:5F Discoverable: yes
[CHG] Device C8:16:DA:62:1D:E8 Connected: yes
Request confirmation
[agent] Confirm passkey 186109 (yes/no): yes
[CHG] Device C8:16:DA:62:1D:E8 Connected: no
[CHG] Device C8:16:DA:62:1D:E8 Connected: yes
[realme X3]# exit
nitesh@zero:~ $ sudo reboot
nitesh@zero:~ $ Connection to 192.168.0.125 closed by remote host.
Connection to 192.168.0.125 closed.

C:\Users\Admin>ssh nitesh@192.168.0.125
ssh: connect to host 192.168.0.125 port 22: Connection timed out

C:\Users\Admin>ssh nitesh@192.168.0.125
nitesh@192.168.0.125's password:
Linux zero 6.1.21+ #1642 Mon Apr  3 17:19:14 BST 2023 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Aug 23 22:30:14 2023 from 192.168.0.105
nitesh@zero:~ $ exit
logout
Connection to 192.168.0.125 closed.

C:\Users\Admin>ssh nitesh@192.168.0.125
nitesh@192.168.0.125's password:
Linux zero 6.1.21+ #1642 Mon Apr  3 17:19:14 BST 2023 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Aug 23 22:34:08 2023 from 192.168.0.105
nitesh@zero:~ $ alsamixer
nitesh@zero:~ $ amixer
Simple mixer control 'Master',0
  Capabilities: pvolume pswitch pswitch-joined
  Playback channels: Front Left - Front Right
  Limits: Playback 0 - 65536
  Mono:
  Front Left: Playback 65536 [100%] [on]
  Front Right: Playback 65536 [100%] [on]
Simple mixer control 'Capture',0
  Capabilities: cvolume cswitch cswitch-joined
  Capture channels: Front Left - Front Right
  Limits: Capture 0 - 65536
  Front Left: Capture 65536 [100%] [on]
  Front Right: Capture 65536 [100%] [on]
nitesh@zero:~ $ bluetoothctl
Agent registered
[CHG] Controller B8:27:EB:03:0F:5F Pairable: yes
[bluetooth]# discoverable on
Changing discoverable on succeeded
[CHG] Controller B8:27:EB:03:0F:5F Discoverable: yes
[NEW] Device D0:97:FE:7A:0C:C0 realme 8 5G
Request confirmation
[agent] Confirm passkey 728571 (yes/no): yes
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001112-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 Modalias: bluetooth:v0046p1200d1436
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001105-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000110a-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000110c-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000110e-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001112-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001115-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001116-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000111f-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000112f-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001132-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001200-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001800-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001801-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000aa15-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: a49eaa15-cb06-495c-9f4f-bb80a90cdf00
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: a82efa21-ae5c-3dde-9bbc-f16da7b16c5a
[CHG] Device D0:97:FE:7A:0C:C0 ServicesResolved: yes
[CHG] Device D0:97:FE:7A:0C:C0 Paired: yes
Authorize service
[agent] Authorize service 00001108-0000-1000-8000-00805f9b34fb (yes/no): yes
Authorize service
[agent] Authorize service 0000110d-0000-1000-8000-00805f9b34fb (yes/no): yes
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001105-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000110a-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000110c-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000110d-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000110e-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001112-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001115-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001116-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000111f-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000112f-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001132-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001200-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001800-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 00001801-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: 0000aa15-0000-1000-8000-00805f9b34fb
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: a49eaa15-cb06-495c-9f4f-bb80a90cdf00
[CHG] Device D0:97:FE:7A:0C:C0 UUIDs: a82efa21-ae5c-3dde-9bbc-f16da7b16c5a
Authorize service
[agent] Authorize service 0000110d-0000-1000-8000-00805f9b34fb (yes/no): yes
Authorize service
[agent] Authorize service 0000110e-0000-1000-8000-00805f9b34fb (yes/no): yes
[CHG] Device D0:97:FE:7A:0C:C0 ServicesResolved: no
[CHG] Device D0:97:FE:7A:0C:C0 Connected: no
[CHG] Device C8:16:DA:62:1D:E8 Connected: yes
[CHG] Controller B8:27:EB:03:0F:5F Discoverable: no
[realme X3]# blueman-manager
[realme X3]# exit
nitesh@zero:~ $ blueman-manager
-bash: blueman-manager: command not found
nitesh@zero:~ $ blue
bluealsa        bluealsa-aplay  bluemoon        bluetoothctl    bluetoothd
nitesh@zero:~ $ blue
bluealsa        bluealsa-aplay  bluemoon        bluetoothctl    bluetoothd
nitesh@zero:~ $ blue
bluealsa        bluealsa-aplay  bluemoon        bluetoothctl    bluetoothd
nitesh@zero:~ $ bluetoothd
D-Bus setup failed: Connection ":1.103" is not allowed to own the service "org.bluez" due to security policies in the configuration file
nitesh@zero:~ $ bluealsa-aplay
bluealsa-aplay: W: Couldn't get BlueALSA PCM list: The name org.bluealsa was not provided by any .service files
^Cnitesh@zero:~ $
nitesh@zero:~ $
nitesh@zero:~ $ history
    1  sudo apt-get update
    2  sudo -i
    3  poweroff
    4  sudo poweroff
    5  sudo -i
    6  bluetoothctl
    7  defaults.bluealsa.profile "a2dp"
    8  sudo 0i
    9  sudo -i
   10  bluealsa --profile=a2dp-source --a2dp-force-audio-cd
   11  sudo usermod -aG dbus nitesh
   12  grep -i 'dbus' /etc/group
   13  cat /etc/group
   14  sudo systemctl status bluealsa
   15  ps aux | grep bluealsa
   16  killall bluealsa
   17  sudo -i
   18  bluealsa --profile=a2dp-source --a2dp-force-audio-cd
   19  ps aux | grep bluealsa
   20  sudo systemctl status bluealsa
   21  apt-get install bluealsa
   22  sudo apt-get install bluealsa
   23  bluealsa --profile=a2dp-source
   24  bluealsa
   25  sudo nano /etc/dbus-1/system.d/bluetooth.conf
   26  sudo -i
   27  pulseaudio --start
   28  bluealsa-aplay -l
   29  bluealsa --start
   30  bluealsa --help
   31  bluealsa-aplay -l
   32  pacmd set-default-sink bluez_sink.C8_16_DA_62_1D_E8.a2dp_sink
   33  pacmd list-sinks
   34  bluetoothctl
   35  bluealsa-play C8:16:DA:62:1D:E8
   36  bluealsa-aplay C8:16:DA:62:1D:E8
   37  bluetoothctl
   38  exit
   39  bluetooth
   40  bluetoothctl
   41  reboot
   42  sudo reboot
   43  nohup bluealsa-aplay C8:16:DA:62:1D:E8 &
   44  exit
   45  bluealsa-aplay C8:16:DA:62:1D:E8
   46  pacmd list-sinks
   47  systemctl restart bluealsa.service
   48  sudo reboot
   49  pactl set-default-sink bluez_sink.C8_16_DA_62_1D_E8.a2dp_sink
   50  pacmd list-sinks
   51  pactl set-default-sink bluez_sink.C8_16_DA_62_1D_E8.a2dp_sink
   52  bluetoothctl
   53  pactl set-default-sink bluez_sink.C8_16_DA_62_1D_E8.a2dp_sink
   54  pacmd list-sinks
   55  cat /etc/asound.conf
   56  bluealsa
   57  alsamixer
   58  pulseaudio --kill
   59  pulseaudio --start
   60  bluealsa --kill
   61  history
   62  bluealsa --profile=a2dp-source --a2dp-force-audio-cd
   63  killall bluealsa
   64  bluealsa --profile=a2dp-source --a2dp-force-audio-cd
   65  sudo -i
   66  pulseaudio --start
   67  pacmd list-sinks
   68  nitesh@zero:~ $ pacmd list-sinks
   69  1 sink(s) available.
   70  nitesh@zero:~ $
   71  bluetoothctl
   72  pactl
   73  pavucontrol
   74  pulseaudio --check
   75  pulseaudio --start
   76  pulseaudio --check
   77  pacmd list-sinks
   78  nano /etc/
   79  bluealsa --profile=a2dp-source --a2dp-force-audio-cd
   80  sudo -i
   81  wget https://file-examples.com/wp-content/storage/2017/11/file_example_WAV_2MG.wav
   82  ls
   83  aplay file_example_WAV_2MG.wav
   84  alsmixer
   85  alsamixer
   86  sudo -i
   87  ls
   88  aplay file_example_WAV_2MG.wav
   89  sudo
   90  sudo -i
   91  pulseaudio
   92  killall pulseaudio
   93  pulseaudio
   94  pulseaudio --kill
   95  pulseaudio --start
   96  pulseaudio --check
   97  pacmd list-sinks
   98  speaker-test c2
   99  speaker-test
  100  aplay -l
  101  aplay -L
  102  aplay -l
  103  nano /usr/share/alsa/alsa.conf
  104  sudo nano /usr/share/alsa/alsa.conf
  105  alsamixer
  106  sudo raspi-config
  107  nano /usr/share/alsa/alsa.conf
  108  sudo -i
  109  speaker-test
  110  speaker-test -c 2 -t wav -l 1
  111  speaker-test -c 2 -t wav
  112  speaker-test -c 6 -t wav
  113  alsamixer
  114  nano /etc/asond.conf
  115  aplay -l
  116  nano /usr/share/alsa/alsa.conf
  117  sudo -i
  118  pulseaudio
  119  pulseaudio --kill
  120  pulseaudio
  121  pulseaudio --start
  122  pacmd list-sinks
  123  sudo systemctl restart bluealsa.service
  124  pulseaudio --start
  125  pacmd list-sinks
  126  nitesh@zero:~ $ pacmd list-sinks
  127  1 sink(s) available.
  128  nitesh@zero:~ $
  129  sudo alsa force-reload
  130  apt-get install alsa-utils
  131  sudo apt-get install alsa-utils
  132  alsa
  133  nitesh@zero:~ $ alsa
  134  -bash: alsa: command not found
  135  pavucontrol
  136  sudo apt install pavucontrol
  137  pavucontrol
  138  amixer
  139  aplay
  140  aplay -l
  141  pavucontrol
  142  amixer
  143  pavucontrol
  144  sudo apt install bluealsa-utils
  145  bluealsa
  146  bluealsa-aplay
  147  sudo -i
  148  pulseaudio --start
  149  paplay /usr/share/sounds/alsa/Front_Center.wav
  150  sudo systemctl enable pulseaudio
  151  ls
  152  paplay file_example_WAV_2MG.wav
  153  cd /usr/share/sounds/
  154  cd alsa/
  155  ls
  156  aplay Front_
  157  aplay Front_Center.wav
  158  amixer
  159  alsamixer
  160  nano /etc/asound.conf
  161  alsamixer
  162  nano /etc/asound.conf
  163  alsamixer
  164  cd
  165  clear
  166  alsamixer
  167  [200~sudo raspi-config
  168  sudo raspi-config
  169  journalctl -u pulseaudio
  170  reboot
  171  sudo reboot
  172  systemctl --user status pulseaudio
  173  sudo nano sudo nano /etc/pulse/daemon.conf
  174  sudo nano /etc/pulse/default.pa
  175  systemctl --user status pulseaudio
  176  systemctl --user restart pulseaudio
  177  systemctl --user status pulseaudio
  178  sudo nano /etc/pulse/default.pa
  179  lsusb
  180  lspcu
  181  lspci
  182  aplay -lL
  183  pulseaudio -vvv
  184  sudo pulseaudio -vvv
  185  sudo -i
  186  sudo pulseaudio --start
  187  pulseaudio --start
  188  amixer
  189  aplay /usr/share/sounds/alsa/Front_Center.wav
  190  paplay /usr/share/sounds/alsa/Front_Center.wav
  191  sudo nano /etc/pulse/default.pa
  192  pulseaudio --start
  193  pulseaudio --kill
  194  pulseaudio --start
  195  paplay /usr/share/sounds/alsa/Front_Center.wav
  196  sudo nano /etc/pulse/default.pa
  197  pulseaudio --kill
  198  pulseaudio --start
  199  paplay /usr/share/sounds/alsa/Front_Center.wav
  200  pulseaudio --kill
  201  paplay /usr/share/sounds/alsa/Front_Center.wav
  202  sudo nano /etc/pulse/default.pa
  203  aplay -l
  204  sudo nano /etc/pulse/default.pa
  205  pulseaudio --kill
  206  pulseaudio --start
  207  paplay /usr/share/sounds/alsa/Front_Center.wav
  208  amixer
  209  pulseaudio --check
  210  echo $?
  211  journalctl -u pulseaudio
  212  sudo usermod -a -G audio nitesh
  213  reboot
  214  sudo reboot
  215  journalctl -u pulseaudio
  216  systemctl status pulseaudio-enable-autospawn.service
  217  sudo -i
  218  history
  219  systemctl --user status pulseaudio
  220  sudo nano /usr/lib/systemd/user/pulseaudio.service
  221  sudo nano /user.slice/user-1000.slice/user@1000.service/app.slice/pulseaudio.service
  222  export $(dbus-launch)
  223  journalctl -xe --user-unit pulseaudio
  224  aseqdump -l
  225  lspci
  226  sudo -i
  227  pacmd list-cards
  228  clear
  229  pacmd list-cards
  230  sudo /etc/pulse/default.pa
  231  sudo nano /etc/pulse/default.pa
  232  pacmd list-cards
  233  systemctl --user status pulseaudio
  234  systemctl --user restart pulseaudio
  235  systemctl --user status pulseaudio
  236  pacmd list-cards
  237  sudo nano /etc/pulse/default.pa
  238  systemctl --user restart pulseaudio
  239  systemctl --user status pulseaudio
  240  sudo nano /etc/pulse/default.pa
  241  systemctl --user restart pulseaudio
  242  systemctl --user status pulseaudio
  243  sudo nano /etc/pulse/default.pa
  244  systemctl --user restart pulseaudio
  245  systemctl --user status pulseaudio
  246  sudo nano /etc/pulse/default.pa
  247  systemctl --user restart pulseaudio
  248  systemctl --user status pulseaudio
  249  sudo nano /etc/pulse/default.pa
  250  systemctl --user restart pulseaudio
  251  systemctl --user status pulseaudio
  252  sudo nano /etc/pulse/default.pa
  253  systemctl --user restart pulseaudio
  254  sudo nano /etc/pulse/default.pa
  255  systemctl --user status pulseaudio
  256  sudo nano /etc/pulse/default.pa
  257  systemctl --user restart pulseaudio
  258  systemctl --user status pulseaudio
  259  amixer
  260  ls
  261  paplay file_example_WAV_2MG.wav
  262  history | grep paplay
  263  paplay file_example_WAV_2MG.wav
  264  sudo nano /etc/pulse/default.pa
  265  systemctl --user restart pulseaudio
  266  systemctl --user status pulseaudio
  267  sudo nano /etc/pulse/default.pa
  268  amixer
  269  alsamixer
  270  speaker-test -D hw:0,1
  271  speaker-test -D hw:1,0
  272  speaker-test -D hw:0,0
  273  aplay -l
  274  speaker-test -D hw:1,0
  275  alsamixer -c 3
  276  alsamixer -c 2
  277  alsamixer -c 1
  278  alsamixer
  279  alsamixer -c 1
  280  pactl list sinks
  281  pulseaudio -D
  282  sudo nano /etc/asound.conf
  283  alsamixer
  284  amixer
  285  speaker-test -Dhw:0,3 -c2
  286  speaker-test -Dhw:1,0 -c2
  287  speaker-test -Dhw:1,1 -c2
  288  speaker-test -Dhw:0,0 -c2
  289  speaker-test -Dhw:0,1 -c2
  290  speaker-test -Dhw:0,2 -c2
  291  speaker-test -Dhw:0,3 -c2
  292  speaker-test -Dhw:0,0 -c2
  293  speaker-test -Dhw:1,0 -c2
  294  speaker-test -Dhw:2,0 -c2
  295  speaker-test -Dhw:23,0 -c2
  296  speaker-test -Dhw:3,0 -c2
  297  speaker-test -Dhw:1,0 -c2
  298  speaker-test -Dhw:1,1 -c2
  299  speaker-test -Dhw:1,2 -c2
  300  speaker-test -Dhw:1,3 -c2
  301  speaker-test -Dhw:1,0 -c2
  302  pacmd list-cards
  303  pacmd list-sinks
  304  audio-speakers
  305  speaker-test -Dhw:1,0,1 -c2
  306  speaker-test -Dhw:1,0,2 -c2
  307  speaker-test -Dhw:1,0,0 -c2
  308  speaker-test -Dhw:1,0,1 -c2
  309  systemctl --user start pulseaudio
  310  systemctl --user status pulseaudio
  311  sudo nano /etc/pulse/default.pa
  312  systemctl --user RESTART pulseaudio
  313  systemctl --user restart pulseaudio
  314  sudo nano /etc/pulse/default.pa
  315  systemctl --user restart pulseaudio
  316  systemctl --user status pulseaudio
  317  speaker-test -Dhw:1,0,1 -c2
  318  speaker-test -Dhw:1,0 -c2
  319  speaker-test -Dhw:1,0 -c6
  320  sudo poweroff
  321  rasp-config
  322  raspi-config
  323  sudo raspi-config
  324  sudo reboot
  325  sudo -i
  326  cd /etc/wpa_supplicant/
  327  la
  328  ls
  329  nano wpa_supplicant.conf
  330  sudo nano wpa_supplicant.conf
  331  sudo raspi-config
  332  sudo nano wpa_supplicant.conf
  333  sudo reboot
  334  sudo -i
  335  alsamixer
  336  ls
  337  aplay file_example_WAV_2MG.wav
  338  paplay
  339  paplay file_example_WAV_2MG.wav
  340  wget https://download.samplelib.com/wav/sample-12s.wav
  341  aplay
  342  aplay sample-12s.wav
  343  bluetoothctl
  344  reboot
  345  sudo reboot
  346  bluetoothctl
  347  clear
  348  pulseau
  349  alsamixer
  350  amixer
  351  cd /etc/pulse/
  352  ls
  353  sudo nano default.pa
  354  systemctl --user start pulseaudio
  355  sudo apt purge bluealsa
  356  sudo apt install pulseaudio-module-bluetooth
  357  sudo usermod -a -G bluetooth nitesh
  358  systemctl --user restart pulseaudio
  359  sudo reboot
  360  pacmd list-sinks
  361  pacmd list-sources
  362  pacmd set-default-sink "alsa_output.hw_1_0" | index
  363  pacmd set-default-sink "alsa_output.hw_1_0"
  364  pacmd set-default-source "alsa_output.hw_1_0.monitor"
  365  pacmd set-sink-volume index volume
  366  pulseaudio -k
  367  bluetoothctl
  368  pacmd list-sinks | grep -e 'name:' -e 'index:'
  369  reboot
  370  sudo reboot
  371  pactl list short sinks
  372  pacmd set-default-sink 0
  373  pactl list short sink-inputs
  374  paplay sample-12s.wav
  375  bluetooth
  376  bluetoothctl
  377  sudo reboot
  378  exit
  379  alsamixer
  380  amixer
  381  bluetoothctl
  382  blueman-manager
  383  bluetoothd
  384  bluealsa-aplay
  385  history
nitesh@zero:~ $
