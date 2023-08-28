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
folder_path = "/home/nitesh/oled/mp4"  # Replace with the actual path

# List MP4 files in the folder
file_list = [file for file in os.listdir(folder_path) if file.endswith(".mp4")]

# Keep track of the selected file index
selected_index = 0
window_end = 0
scroll_position = 0  # Start scrolling from the beginning

# Keep track of the process running the song
current_song_process = None

# Global variable to control autoplay
autoplay_enabled = True

# Long Press Button Time
buttonExit_pressed_time = None


def play_selected_file(selected_file):
    global current_song_process

    # Terminate the previous song process if it exists
    if current_song_process:
        try:
            os.killpg(os.getpgid(current_song_process.pid), signal.SIGTERM)
            current_song_process.wait()
        except ProcessLookupError:
            pass
    
    full_file_path = os.path.join(folder_path, selected_file)
    cmd = f"mplayer -slave -input file=/tmp/mplayer-control -vo null -novideo {shlex.quote(full_file_path)}"
    current_song_process = subprocess.Popen(cmd, shell=True, preexec_fn=os.setsid)

    global autoplay_enabled
    autoplay_enabled = True

def autoplay_next_song():
    global selected_index, autoplay_enabled, scroll_position
    try:
        while autoplay_enabled:
            time.sleep(0.1)
            if current_song_process and current_song_process.poll() is not None:
                if autoplay_enabled and selected_index < len(file_list) - 1:
                    selected_index += 1
                    print("selected_index:", selected_index)
                    if selected_index >= scroll_position + 3:
                        scroll_position += 1
                    
                    selected_file = file_list[selected_index]
                    play_selected_file(selected_file) 

                    display()
                elif scroll_position + 3 < len(file_list):
                    scroll_position += 1
                    selected_file = file_list[selected_index]
                    play_selected_file(selected_file)
                    print("Autoplay:", selected_file)
                    display()
    except KeyboardInterrupt:
        pass


    
# Start the autoplay thread
autoplay_thread = threading.Thread(target=autoplay_next_song)
autoplay_thread.daemon = True  # This allows the thread to exit when the main program exits
autoplay_thread.start()

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
    
display()

try:
    while True:
        time.sleep(0.1)
        
        if not buttonUp.value:
            print("Up")
            if selected_index > 0:
                selected_index -= 1
                print("selected_index:", selected_index)
                if selected_index < scroll_position:
                    scroll_position = selected_index
                display()
            elif scroll_position > 0:
                scroll_position -= 1
                display()
            time.sleep(0.2)
            
        if not buttonDown.value:
            print("Down")
            if selected_index < len(file_list) - 1:
                selected_index += 1
                print("selected_index:", selected_index)
                if selected_index >= scroll_position + 3:
                    scroll_position += 1
                display()
            elif scroll_position + 3 < len(file_list):
                scroll_position += 1
                display()
            time.sleep(0.2)
            
        if not buttonOk.value:
            print("OK")
            selected_file = file_list[selected_index]
            play_selected_file(selected_file)
            print(selected_file)
            display()
            time.sleep(0.2)
            
        if not button_play_pause.value:
            print("button_play_pause")

            if current_song_process:
                try:
                    if current_song_process.poll() is not None:
                        print("Not Playing")
                    else:
                        print("Playing")
                        subprocess.run('echo "pause" > /tmp/mplayer-control', shell=True)
                except ProcessLookupError:
                    pass   
            #display()
            time.sleep(0.2)
        
        if not buttonExit.value:
            print("buttonExit")
            if current_song_process:
                try:
                    if current_song_process.poll() is not None:
                        print("Not Playing")
                    else:
                        print("Playing")
                        os.killpg(os.getpgid(current_song_process.pid), signal.SIGTERM)
                        #autoplay_enabled = False
                        #print("Autoplay: OFF")
                except ProcessLookupError:
                    pass
                    

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
