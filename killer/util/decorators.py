'''
Created on 2012-9-26

@author: kj
'''

def static_variable(varname, value):
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate