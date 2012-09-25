'''
Created on 2012-9-23

@author: kj
'''

import platform

class SysEnv:
    '''
    Provides access to system environment parameters.
    '''
    
    @staticmethod
    def get_os():
        '''
        Gets OS info in a tuple (system, release, version)
        '''
        return (platform.system(), platform.release(), platform.version())
    