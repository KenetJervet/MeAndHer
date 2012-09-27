'''
Created on 2012-9-26

@author: kj
'''

from sys_env import SysEnv
from ctypes import *

def pick_window():
    x = input("Input X coordinate:")
    y = input("Input Y coordinate:")

    user32 = windll.user32

    window_id = user32.WindowFromPoint(x,y)
    print window_id
    
    process_id = c_long()
    user32.GetWindowThreadProcessId(window_id, byref(process_id))
    
    return process_id.value if process_id > 0 else -1

if __name__ == '__main__':
    print pick_window()
