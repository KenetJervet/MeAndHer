'''
Created on 2012-9-26

@author: kj
'''

from module_handler import delete_module
from sys_env import SysEnv
from util.decorators import static_variable
import subprocess
import re
import ctypes

@static_variable('so', ctypes.CDLL('./external/xwininfo.so'))
def pick_window():
    window_id = pick_window.so.getwindow_main();
    p = subprocess.Popen([
                        'xprop',
                        '_NET_WM_PID',
                        '-id',
                        str(window_id),
                        ], stdout=subprocess.PIPE)
    prepared_process_id = p.communicate()[0]
    reg_matches = re.match(r'_NET_WM_PID\(CARDINAL\) = (\d+)', prepared_process_id)
    if reg_matches:
        process_id = reg_matches.group(1)
        return process_id
    else:
        return -1
