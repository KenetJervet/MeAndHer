#!/usr/bin/python

# Started working on windows branch.

import wx
from ui.my_frame import MyFrame

app = wx.PySimpleApp(0)
wx.InitAllImageHandlers()
myFrame = MyFrame(None, -1, "")
app.SetTopWindow(myFrame)
myFrame.Show()
app.MainLoop()
