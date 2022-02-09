import tkinter as tk
import picamera
import datetime
from subprocess import call
from time import sleep
import os

image = 1
video = 1
session = str(datetime.datetime.now()).replace(" ","")
session = session.replace("-","")
session = session.replace(":","")
session = session.replace(".","")
os.mkdir("/home/pi/share/photos/" + session)
os.mkdir("/home/pi/share/videos/" + session)

#set up the camera to HD
camera = picamera.PiCamera()
camera.resolution = (1920,1080)
camera.framerate = 30
camera.iso = 800

#function to convert video to mp4
def convert(file_h264, file_mp4):
    command = "MP4Box -add " + file_h264 + ":fps=60 " + file_mp4
    call([command], shell=True)
    os.remove(file_h264)
#functions for button commands

def on():
    #allows for live preview of the microscope
    camera.start_preview(fullscreen=False, window=(20,80,1200,800))
def off():
    #turn off preview
    camera.stop_preview()
              
def take_picture():
    global image
    global session
    filename = "/home/pi/share/photos/" + session + "/" + str(image) + ".jpg"
    image += 1
    camera.capture(filename)
    
def start_video():
    global video
    global session
    filename = "/home/pi/share/videos/" + session + "/"+ str(video) + ".h264"
    camera.start_recording(filename)
    
def stop_video():
    camera.stop_recording()
    global video
    global session
    filename = "/home/pi/share/videos/" + session + "/" + str(video) + ".h264"
    newfile = "/home/pi/share/videos/" + session + "/" + str(video) + ".mp4"
    
    video +=1
    convert(filename,newfile)
    
    
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



btn_camera_on.pack()
btn_camera_off.pack()
btn_take_picture.pack()
btn_start_video.pack()
btn_stop_video.pack()


window.mainloop()
