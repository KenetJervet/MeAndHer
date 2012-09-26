'''
Created on 2012-9-26

@author: kj
'''

from subprocess import call
from sys_env import SysEnv
import wx

def kill_process(process_id):
    if call(['kill', '-9', str(process_id)]) == 0:
        pass
    else:
        wx.MessageBox('Internal error.', 'Process ID', wx.OK)