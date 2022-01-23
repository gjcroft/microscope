import tkinter as tk
import picamera
import datetime


#set up the camera to HD
camera = picamera.PiCamera()
camera.resolution = (1920,1080)
#camera.iso = 600

#functions for button commands
def on():
    #allows for live preview of the microscope
    camera.start_preview(fullscreen=False, window=(20,80,1200,800))
def off():
    #turn off preview
    camera.stop_preview()
              
def take_picture():
    filename = "/home/pi/share/photos/" + str(datetime.datetime.now()) + ".jpg"
    camera.capture(filename)
    
def start_video():
    filename = "/home/pi/share/videos/" + str(datetime.datetime.now()) + ".h264"
    camera.start_recording(filename)
    
def stop_video():
    camera.stop_recording()

#gui build out
window =tk.Tk()
window.title('Raspberry Pi Microscope Recorder')
window.geometry("640x480+1250+150")
btn_camera_on = tk.Button(
    text='Camera ON',
    width = 20,
    height = 5,
    bg='green',
    fg='white',
    command = on,
    )
btn_camera_off = tk.Button(
    text='Camera OFF',
    width = 20,
    height = 5,
    bg='red',
    fg='white',
    command = off,
    )
btn_take_picture = tk.Button(
    text='Take Picture',
    width = 20,
    height = 5,
    bg='black',
    fg='white',
    command = take_picture,
    )
btn_start_video = tk.Button(
    text='Start Recording',
    width = 20,
    height = 5,
    bg='green',
    fg='white',
    command = start_video,
    )

btn_stop_video = tk.Button(
    text='Stop Recording',
    width = 20,
    height = 5,
    bg='red',
    fg='white',
    command = stop_video,
    )

lbl_filename = tk.Label(window, text='Capture filename')
e_filename = tk.Entry(window)

btn_camera_on.pack()
btn_camera_off.pack()
btn_take_picture.pack()
btn_start_video.pack()
btn_stop_video.pack()
lbl_filename.pack()
e_filename.pack()

window.mainloop()