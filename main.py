#!/usr/bin/python

import wx
from my_frame import MyFrame

app = wx.PySimpleApp(0)
wx.InitAllImageHandlers()
myFrame = MyFrame(None, -1, "")
app.SetTopWindow(myFrame)
myFrame.Show()
app.MainLoop()
