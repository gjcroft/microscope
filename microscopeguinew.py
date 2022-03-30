import tkinter as tk
from tkinter.tix import Tk
import picamera
import datetime
from subprocess import call
from time import sleep
import os

#set sequence filenames
image = 1
video = 1

#camera variables
zoom = 1


#set session folders in shared directory creates a new folder on run for the session
#one folder created in photos and one in videos
session = str(datetime.datetime.now()).replace(" ","")
session = session.replace("-","")
session = session.replace(":","")
session = session.replace(".","")
os.mkdir("/home/pi/share/photos/" + session)
os.mkdir("/home/pi/share/videos/" + session)

camera = picamera.PiCamera()
camera.framerate = 30

#you need to run a sudo install gpac for MP4Box to work

#function to convert video to mp4
def convert(file_h264, file_mp4):
    command = "MP4Box -add " + file_h264 + ":fps=60 " + file_mp4
    call([command], shell=True)
    os.remove(file_h264)
#functions for button commands

def cam_on():
    #allows for live preview of the microscope
    #set up the camera to HD
    camera.resolution = (1920,1080)
    camera.start_preview(fullscreen=False, window=(20,80,1200,800))
    

def cam_off():
    #turn off preview
    camera.stop_preview()
              
def take_picture():
    global image
    global session
    #set up the camera for 4k for photo
    #camera.resolution = (4056,3040)
    camera.resolution = (1920,1080)
    filename = "/home/pi/share/photos/" + session + "/" + str(image) + ".jpg"
    #increment filename
    image += 1
    camera.capture(filename)
    camera.resolution = (1920,1080)

def start_video():
    #set up the camera to HD for filming
    camera.resolution = (1920,1080)
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
    #increment filename
    video +=1
    convert(filename,newfile)
    
#define functions to adjust camera
def set_bright(x):
    x = int(x)
    camera.brightness = x #50 is default 0 - 100
def set_cont(x):
    x = int(x)
    camera.contrast = x #0 is default -100 to 100
def set_sat(x):
    x = int(x)
    camera.saturation = x #0 is default -100 to 100
def set_sharp(x):
    x = int(x)
    camera.sharpness = x #0 is default -100 to 100
def set_iso(x):
    x = int(x)
    camera.iso = x #0 is default max is 1600

def effects(x):
    effectno = int(x)
    if effectno == 1:
        camera.image_effect = 'none'
        print("No Effect")
    elif effectno == 2:
        camera.image_effect = 'negative'
        print("Negative Effect")
    elif effectno == 3:
        camera.image_effect = 'solarize'
        print("Solarize Effect")
    elif effectno == 4:
        camera.image_effect = 'sketch'
        print("Sketch Effect")
    elif effectno == 5:
        camera.image_effect = 'denoise'
        print("Denoise Effect")
    elif effectno == 6:
        camera.image_effect = 'emboss'
        print("Emboss Effect")
    elif effectno == 7:
        camera.image_effect = 'oilpaint'
        print("Oilpaint Effect")
    elif effectno == 8:
        camera.image_effect = 'hatch'
        print("Hatch Effect")
    elif effectno == 9:
        camera.image_effect = 'gpen'
        print("gpen Effect")
    elif effectno == 10:
        camera.image_effect = 'pastel'
        print("Pastel Effect")
    elif effectno == 11:
        camera.image_effect = 'watercolor'
        print("Watercolour Effect")
    elif effectno == 12:
        camera.image_effect = 'film'
        print("Film Effect")
    elif effectno == 13:
        camera.image_effect = 'blur'
        print("Blur Effect")
    elif effectno == 14:
        camera.image_effect = 'saturation'
        print("Saturation Effect")
    elif effectno == 15:
        camera.image_effect = 'colorswap'
        print("Colourswap Effect")
    elif effectno == 16:
        camera.image_effect = 'washedout'
        print("Washed Out Effect")
    elif effectno == 17:
        camera.image_effect = 'posterise'
        print("Posterise Effect")
    elif effectno == 18:
        camera.image_effect = 'colorpoint'
        print("Colourpoint effect")
    elif effectno == 19:
        camera.image_effect = 'colorbalance'
        print("Colourbalance Effect")
    elif effectno == 20:
        camera.image_effect = 'cartoon'
        print("Cartoon Effect")
    elif effectno == 21:
        camera.image_effect = 'deinterlace1'
        print("Deint 1 Effect")
    elif effectno == 22:
        camera.image_effect = 'deinterlace2'
        print("Deint 2 Effect")
def awb(x):
    awb = int(x)
    if awb == 1:
        camera.AWB_MODES['auto']
    elif awb == 2:
        camera.AWB_MODES['sunlight']
    elif awb == 3:
        camera.AWB_MODES['cloudy']
    elif awb == 4:
        camera.AWB_MODES['shade']
    elif awb == 5:
        camera.AWB_MODES['tungsten']
    elif awb == 6:
        camera.AWB_MODES['fluorescent']
    elif awb== 7:
        camera.AWB_MODES['incandescent']
    elif awb == 8:
        camera.AWB_MODES['flash']
    elif awb == 9:
        camera.AWB_MODES['horizon']
    elif awb == 10:
        camera.AWB_MODES['off']
    else:
        awb = 0
def zoomIn():
        global zoom
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        if zoom >= 0.7:
            zoom -= 0.05
            x = (ws/2) - 0.5 * 400/(1 - zoom)
            y = (hs/2) - 0.5 * 285/(1 - zoom)
            camera.zoom = (x, y, zoom, zoom)
        else:
            zoom = 0.7
def zoomOut():
    global zoom
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    if zoom <= 1.3:
        zoom += 0.05
        x = (ws/2) - 0.5 * 400/(1 - zoom)
        y = (hs/2) - 0.5 * 285/(1 - zoom)
        camera.zoom = (x, y, zoom, zoom)
    else:
        zoom = 1.3
def rotate():
    camera.rotation += 90
    print("Rotation", camera.rotation, "degrees")

def hflip():
    if camera.hflip == True:
        camera.hflip = False
    else:
        camera.hflip = True   

def vflip():
    if camera.vflip == True:
        camera.vflip = False
    else:
        camera.vflip = True
#gui build out
window =tk.Tk()
window.title('Raspberry Pi Microscope Recorder')
#window set for 27" monitor on right hand side
window.geometry("640x980+1250+75")
window.configure(bg='white')
btn_camera_on = tk.Button(
    text='Camera ON',
    width = 10,
    height = 1,
    bg='green',
    fg='white',
    command = cam_on,
    )
btn_camera_off = tk.Button(
    text='Camera OFF',
    width = 10,
    height = 1,
    bg='red',
    fg='white',
    command = cam_off,
    )
btn_take_picture = tk.Button(
    text='Take Picture',
    width = 10,
    height = 1,
    bg='black',
    fg='white',
    command = take_picture,
    )
btn_start_video = tk.Button(
    text='Start Recording',
    width = 10,
    height = 1,
    bg='green',
    fg='white',
    command = start_video,
    )

btn_stop_video = tk.Button(
    text='Stop Recording',
    width = 10,
    height = 1,
    bg='red',
    fg='white',
    command = stop_video,
    )

btn_zoomin = tk.Button(
    text='Zoom in',
    width = 10,
    height = 1,
    bg='grey',
    fg='white',
    command = zoomIn,
    )

btn_zoomout = tk.Button(
    text='Zoom out',
    width = 10,
    height = 1,
    bg='grey',
    fg='white',
    command = zoomOut,
    )

btn_rotate = tk.Button(
    text='Rotate',
    width = 10,
    height = 1,
    bg='grey',
    fg='white',
    command = rotate,
    )

btn_hflip = tk.Button(
    text='HFLIP',
    width = 10,
    height = 1,
    bg='grey',
    fg='white',
    command = hflip,
)
btn_vflip = tk.Button(
    text='VFLIP',
    width = 10,
    height = 1,
    bg='grey',
    fg='white',
    command = vflip,
)

#build slider widgets
sldr_brightness = tk.Scale(window,
                           from_=0,
                           to=100,
                           orient=tk.HORIZONTAL,
                           tickinterval=10,
                           length=400,
                           command =set_bright,
                           bg='white',
                           troughcolor='white',
                           label="Brightness")
sldr_brightness.set(50)

sldr_contrast = tk.Scale(window,
                         from_=-100,
                         to=100,
                         orient=tk.HORIZONTAL,
                         tickinterval=10,
                         length=400,
                         command =set_cont,
                         bg='white',
                         troughcolor='white',
                         label="Contrast")
sldr_contrast.set(0)

sldr_saturation = tk.Scale(window,
                           from_=-100,
                           to=100,
                           orient=tk.HORIZONTAL,
                           tickinterval=10,
                           length=400,
                           command =set_sat,
                           bg='white',
                           troughcolor='white',
                           label="Saturation")
sldr_saturation.set(0)

sldr_sharpness = tk.Scale(window,
                           from_=-100,
                           to=100,
                           orient=tk.HORIZONTAL,
                           tickinterval=10,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
                           length=400,
                           command =set_sharp,
                           bg='white',
                           troughcolor='white',
                           label="Sharpness")
sldr_sharpness.set(0)

sldr_iso = tk.Scale(window,
                           from_=0,
                           to=1000,
                           orient=tk.HORIZONTAL,
                           tickinterval=100,
                           length=400,
                           command =set_iso,
                           bg='white',
                           troughcolor='white',
                           label="ISO")
sldr_iso.set(0)

sldr_effects = tk.Scale(window,
                           from_=1,
                           to=22,
                           orient=tk.HORIZONTAL,
                           tickinterval=1,
                           length=400,
                           command =effects,
                           bg='white',
                           troughcolor='white',
                           label="Effects")
sldr_effects.set(1)

sldr_awb = tk.Scale(window,
                           from_=1,
                           to=10,
                           orient=tk.HORIZONTAL,
                           tickinterval=1,
                           length=400,
                           command =awb,
                           bg='white',
                           troughcolor='white',
                           label="AWBs")
sldr_awb.set(1)


btn_camera_on.pack(side=tk.TOP)
btn_camera_off.pack()
btn_rotate.pack(side=tk.TOP)
btn_hflip.pack(side=tk.TOP)
btn_vflip.pack(side=tk.TOP)
sldr_brightness.pack()
sldr_contrast.pack()
sldr_saturation.pack()
sldr_sharpness.pack()
sldr_iso.pack()
sldr_effects.pack()
sldr_awb.pack()
btn_start_video.pack(ipadx=5,side=tk.LEFT)
btn_stop_video.pack(ipadx=5,side=tk.LEFT)
btn_take_picture.pack(ipadx=5,side=tk.LEFT)
btn_zoomin.pack(ipadx=5,side=tk.LEFT)
btn_zoomout.pack(ipadx=5,side=tk.LEFT)

window.mainloop()