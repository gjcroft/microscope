# microscope

Code for using the Raspberry Pi HQ Camera coupled with an amscope reduction lens to add a raspberry pi gui based software to take pictures and 
capture video from a microscope.

Current cameras are quite expensive to get decent frame rates, the Raspberry Pi HQ Camera provides for HD video capture at 30fps so makes for a nice
relatively cheap high quality camera for a microscope.

Current version is running on the legacy version of Raspberry Pi OS using the PiCamera module.

This is very much work in progress from myside the primary object was to use the picamera for filming for my youtube videos. 

There are two versions of the code the first one is a very simple Gui for controlling the camera.

The second version now has some of the more advanced features of the PiCamera module built out on sliders such as Brightness, Contrast, Saturation and
effects.

There is also a zoom feature (i need to add some error handling here as it only works for 4 clicks but pressing zoom out corrects the camera)

Work is in progress to add a direct video feed within the GUI with help from Martin Parker.

