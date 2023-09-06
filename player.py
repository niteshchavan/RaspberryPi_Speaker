import time
import os
import board
import busio
import digitalio
import subprocess
import threading
import signal
import adafruit_ssd1306
import shlex

from PIL import Image, ImageDraw, ImageFont

subprocess.run('rm /tmp/mplayer-control', shell=True)
subprocess.run('mkfifo /tmp/mplayer-control', shell=True)
subprocess.run('killall mplayer', shell=True)

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

#Button Up GPIO24
buttonUp = digitalio.DigitalInOut(board.D24)
buttonUp.direction = digitalio.Direction.INPUT
buttonUp.pull = digitalio.Pull.UP

#Button Down GPIO23
buttonDown = digitalio.DigitalInOut(board.D23)
buttonDown.direction = digitalio.Direction.INPUT
buttonDown.pull = digitalio.Pull.UP

#Button OK GPIO22
buttonOk = digitalio.DigitalInOut(board.D22)
buttonOk.direction = digitalio.Direction.INPUT
buttonOk.pull = digitalio.Pull.UP

#Button Play_pause GPIO27
button_play_pause = digitalio.DigitalInOut(board.D27)
button_play_pause.direction = digitalio.Direction.INPUT
button_play_pause.pull = digitalio.Pull.UP

#Button Exit GPIO17
buttonExit = digitalio.DigitalInOut(board.D17)
buttonExit.direction = digitalio.Direction.INPUT
buttonExit.pull = digitalio.Pull.UP


#Button Volume Up GPIO10
Volup = digitalio.DigitalInOut(board.D9)
Volup.direction = digitalio.Direction.INPUT
Volup.pull = digitalio.Pull.UP

#Button Volume Down GPIO9
Voldown = digitalio.DigitalInOut(board.D10)
Voldown.direction = digitalio.Direction.INPUT
Voldown.pull = digitalio.Pull.UP


# Display Parameters
WIDTH = 128
HEIGHT = 64

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)

# Path to the folder containing the MP4 files
folder_path = "/root/player/mp4"  # Replace with the actual path

# List MP4 files in the folder
file_list = [file for file in os.listdir(folder_path) if file.endswith(".mp4")]

# Keep track of the selected file index
selected_index = 0
window_end = 0
scroll_position = 0  # Start scrolling from the beginning

# Keep track of the process running the song
current_song_process = None

# Check Player After Exit
player_status = None

# Long Press Button Time
buttonExit_pressed_time = None


    
#-demuxer mov
cmd = "mplayer -slave -quiet -idle -demuxer mov -vo null -novideo -input file=/tmp/mplayer-control"
current_song_process = subprocess.Popen(cmd, shell=True, text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       

    
#Power Sequence Animation
def poweroff():
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    draw.text((20, 0), "Shutting Down", font=font, fill=255)
    oled.image(image)
    oled.show()
    draw.rectangle((50, 20, oled.width, oled.height), outline=0, fill=0)
    draw.text((50, 20), "3..", font=font, fill=255)
    time.sleep(1)
    oled.image(image)
    oled.show()
    draw.rectangle((50, 20, oled.width, oled.height), outline=0, fill=0)
    draw.text((50, 20), "2..", font=font, fill=255)
    time.sleep(1)
    oled.image(image)
    oled.show()
    draw.rectangle((50, 20, oled.width, oled.height), outline=0, fill=0)
    draw.text((50, 20), "1..", font=font, fill=255)
    time.sleep(1)
    oled.image(image)
    oled.show()
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    oled.image(image)
    oled.show()
    time.sleep(1)
    os.system("sudo shutdown -h now")

def display():
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    # Show IP Address
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell=True)
    draw.text((0, 0), "IP: " + str(IP, 'utf-8'), font=font, fill=255)

    # List MP4 files in the folder
    num_files = len(file_list)

    # Calculate scrolling window bounds
    window_start = scroll_position
    window_end = min(scroll_position + 3, num_files)

    # Display file names within the scrolling window
    y = 15  # Vertical position to start printing file names
    for i in range(window_start, window_end):
        if i == selected_index:
            draw.text((0, y), "> " + file_list[i], font=font, fill=255)
        else:
            draw.text((0, y), "  " + file_list[i], font=font, fill=255)
        y += 16  # Move to the next line

    # Display image
    oled.image(image)
    oled.show()

# Start Display    
display()


# Initialize previous_line variable
previous_line = ""

def load_next_song():
    global selected_index, scroll_position
    selected_index += 1       
    scroll_position = selected_index
    if selected_index < len(file_list):
        selected_file = file_list[selected_index]
        full_file_path = os.path.join(folder_path, selected_file)
        subprocess.run(f'echo "loadfile {shlex.quote(full_file_path)}" > /tmp/mplayer-control', shell=True)
        print(f"Autoplaying: {shlex.quote(full_file_path)}")
     
    display()

# Function to continuously read and print the last line of current_song_process.stdout
def read_last_line():
    global previous_line
    try:
        while True:
            time.sleep(0.1)
            last_line = None
            try:
                for line in current_song_process.stdout:
                    last_line = line.strip()  # Update last_line with each line
                    
                    if last_line != previous_line: 
                        print(last_line)  # Print each line if needed
                        if last_line == 'ANS_ERROR=PROPERTY_UNAVAILABLE':
                            load_next_song()
                        else:
                            subprocess.run('echo "get_property percent_pos" > /tmp/mplayer-control', shell=True)
                        previous_line = last_line  # Update previous_line
            except subprocess.TimeoutExpired:
                print("current_song_process stopped responding")
                break
    
    except KeyboardInterrupt:
        pass    
read_thread = threading.Thread(target=read_last_line, daemon=True)
read_thread.start()            


try:
    while True:
        time.sleep(0.1)

        if not buttonUp.value:
            if selected_index > 0:
                selected_index -= 1
                if selected_index < scroll_position:
                    scroll_position = selected_index
                display()
            elif scroll_position > 0:
                scroll_position -= 1
                display()
            print("UP","selected_index:", selected_index, "scroll_position:", scroll_position)
            time.sleep(0.2)
            
        if not buttonDown.value:
            if selected_index < len(file_list) - 1:
                selected_index += 1
                if selected_index >= scroll_position + 3:
                    scroll_position += 1
                display()
            elif scroll_position + 3 < len(file_list):
                scroll_position += 1
                display()
            print("Down","selected_index:", selected_index, "scroll_position:", scroll_position)
            time.sleep(0.2)
            
        if not buttonOk.value:
            display()
            if player_status == False:
                print("Player is offline restarting player")
                subprocess.run('rm /tmp/mplayer-control', shell=True)
                subprocess.run('mkfifo /tmp/mplayer-control', shell=True)
                subprocess.run('killall mplayer', shell=True)
                current_song_process = subprocess.Popen(cmd, shell=True, text=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                player_status = True
                
            selected_file = file_list[selected_index]
            full_file_path = os.path.join(folder_path, selected_file)
            subprocess.run(f'echo "loadfile {shlex.quote(full_file_path)}" > /tmp/mplayer-control', shell=True)
            print(f"{shlex.quote(full_file_path)}")
            display()
            time.sleep(0.2)
            
        if not button_play_pause.value:
            print("button_play_pause")
            subprocess.run('echo "pause" > /tmp/mplayer-control', shell=True)
            time.sleep(0.2)

        if not Volup.value:
            subprocess.run('amixer set "Speaker" 3%+', shell=True)
            print("Volume UP")
            time.sleep(0.2)
            
        if not Voldown.value:
            subprocess.run('amixer set "Speaker" 3%-', shell=True)
            print("Volume Down")
            time.sleep(0.2)
        
        if not buttonExit.value:
            print("buttonExit")

            subprocess.run('echo "quit" > /tmp/mplayer-control', shell=True)
            subprocess.run('rm /tmp/mplayer-control', shell=True)
            player_status = False
            draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
            draw.text((10, 0), "Player is Offline", font=font, fill=255)
            draw.text((10, 20), "Long Press OFF", font=font, fill=255)
            draw.text((10, 40), "Press Ok to Play", font=font, fill=255)            
            oled.image(image)
            oled.show()
            if buttonExit_pressed_time is None:
                buttonExit_pressed_time = time.time()
            else:
                # Button has been held down
                elapsed_time = time.time() - buttonExit_pressed_time
                if elapsed_time >= 2.0:
                    print("Long press detected, performing power off action")
                    poweroff()
            time.sleep(0.2)
        else:
            buttonExit_pressed_time = None  # Reset the timer when the button is released
  
  
except KeyboardInterrupt:
    pass
