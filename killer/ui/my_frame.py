#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Fri Sep 21 16:35:49 2012

import wx
import wnck
from core.module_handler import delete_module

# begin wxGlade: extracode
# end wxGlade


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.FRAME_TOOL_WINDOW | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.btnTest = wx.Button(self, -1, "Click Me")
        self.btnDau = wx.Button(self, -1, "Show Handle Info")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.OnBtnTestClick, self.btnTest)
        self.Bind(wx.EVT_BUTTON, self.OnBtnDauClick, self.btnDau)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.GridSizer(1, 2, 0, 0)
        sizer_1.Add(self.btnTest, 0, 0, 0)
        sizer_1.Add(self.btnDau, 0, 0, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def OnBtnTestClick(self, event):  # wxGlade: MyFrame.<event_handler>
        from core.sys_env import SysEnv
        wx.MessageBox(str(SysEnv.get_os()), 'Fuck', wx.OK+wx.CANCEL)
        delete_module('core.module_handler')
        event.Skip()

    def OnBtnDauClick(self, event):  # wxGlade: MyFrame.<event_handler>
        window_list = wnck.screen_get_default().get_windows()
        if len(window_list) == 0:
            wx.MessageBox("No window found", 'Info', wx.OK)
        wx.MessageBox(str(self.GetHandle()), 'Fuck', wx.OK+wx.CANCEL)
        event.Skip()

# end of class MyFrame
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    myFrame = MyFrame(None, -1, "")
    app.SetTopWindow(myFrame)
    myFrame.Show()
    app.MainLoop()
