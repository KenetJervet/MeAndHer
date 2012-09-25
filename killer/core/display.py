'''
Created on 2012-9-24

@author: kj
'''

import xcb

global dpy, screen

def setup_display_and_screen(display_name, dpy, screen):
    global dpy, screen
    dpy = xcb.connect(display_name)