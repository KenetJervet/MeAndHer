'''
Created on 2012-9-26

@author: kj
'''

from subprocess import call
import signal
import os
from sys_env import SysEnv
import wx

def kill_process(process_id):
    os.kill(int(process_id), signal.SIGTERM)
