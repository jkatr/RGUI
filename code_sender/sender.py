import sublime
import re
import time
import ctypes
import os

from ..settings import Settings

PostMessage = ctypes.windll.user32.PostMessageA
FindWindow = ctypes.windll.user32.FindWindowW
SetWindowPos = ctypes.windll.user32.SetWindowPos

class CodeSender:

    def __init__(self, view, cmd=None, prog=None, hwnd = None):
        self.view = view
        self.settings = Settings(view)
        if prog:
            self.prog = prog
        else:
            self.prog = self.settings.get("prog")
        self.hwnd = hwnd

    def send_text(self, cmd):
        cmd = cmd.rstrip()
        cmd = cmd.expandtabs(self.view.settings().get("tab_size", 4))
        prog = self.prog.lower()
        if prog == "r" or prog == "r.post":
            self.send_to_r(cmd)
        elif prog == "r.tmp.file":
            self.send_to_r_tmp_file(cmd)
        else:
            sublime.message_dialog("%s is not supported for current syntax." % prog)

    def send_to_r(self, cmd):
        rid = self.find_rgui()

        self.bring_rgui_to_top(rid)

        self.post_to_rgui(rid, cmd)
        

    def send_to_r_tmp_file(self, cmd):
        tmp_fn = os.path.join(os.path.dirname(__file__), "tmp.R")
        
        rid = self.find_rgui()
        self.bring_rgui_to_top(rid)

        tmp_file = open(tmp_fn, 'w')
        tmp_file.write(cmd)
        tmp_file.close()

        self.post_to_rgui(rid, "source('" + tmp_fn.replace(os.sep, "/") + "')")

    def find_rgui(self):
        rid = FindWindow(None, 'R Console (64-bit)')
        if not rid:
            sublime.message_dialog("Rgui (R Console (64-bit)) not found.")
        return rid

    def bring_rgui_to_top(self, rid):
        
        if ctypes.windll.user32.IsIconic(rid) == 1: #if minimized
            PostMessage(rid, int(0x0112), int(0xF120), 0) #restore

        SetWindowPos(rid,-1,None,None,None,None, int(0x0001)+int(0x0002)) #change z-order
        SetWindowPos(rid,-2,None,None,None,None, int(0x0001)+int(0x0002)) #change z-order
        
        #PostMessage(self.hwnd, int(0x0112), int(0xF120), 0) #restore

        SetWindowPos(self.hwnd,-1,None,None,None,None, int(0x0001)+int(0x0002)) #change z-order
        SetWindowPos(self.hwnd,-2,None,None,None,None, int(0x0001)+int(0x0002)) #change z-order        

    def post_to_rgui(self, rid, cmd):
        for char in cmd:
            PostMessage(rid, int(0x102), ord(char), 0)     
        PostMessage(rid, int(0x102), ord('\n'), 0)  