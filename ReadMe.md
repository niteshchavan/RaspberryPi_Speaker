## Update and Upgrade
```
sudo apt update

sudo apt full-upgrade
```
# Install PulseAudio Bluetooth profile loader.
```
sudo apt install pulseaudio-module-bluetooth
```
# Add User
```
sudo usermod -a -G bluetooth nitesh
```

# Login with nitesh user and start pulse audio

```
systemctl --user start pulseaudio

```
# start bluetooth controller

```
bluetoothctl

discoverable on

power on

trust "Mac address"

```
# Install Python Envoirment 
```
apt-get install python3-venv

python -m venv player
```
# For Oled Display use adafruit-circuitpython-ssd1306 and Pillow

```
pip3 install adafruit-circuitpython-ssd1306

pip3 install Pillow

```
# From raspi-config enable I2C

## Raspberry Pi Zero Bluetooth Speaker Cmd Output
https://gist.github.com/actuino/9548329d1bba6663a63886067af5e4cb
https://unix.stackexchange.com/questions/65246/change-pulseaudio-input-output-from-shell
## Follow Second
https://aptx1337.github.io/posts/general/surround_soundsystem_pulseaudio.html

## player.py
Player.py Works with Mplayer with buttons

## rename_songs.py 
Renames files and remove junk caracters


## How to make mplayer continue after pausing it via a named pipe?

Create a named pipe.
```
mkfifo /tmp/mplayer-control

mplayer -slave -input file=/tmp/mplayer-control mymusic.mp3

echo "pause" > /tmp/mplayer-control

echo "quit" > /tmp/mplayer-control

echo "volume +10" > /tmp/mplayer-control

echo "volume -10" > /tmp/mplayer-control
```
