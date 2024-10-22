import sublime
import re
import time
import ctypes
import os

from ..settings import Settings

PostMessage = ctypes.windll.user32.PostMessageA
FindWindow = ctypes.windll.user32.FindWindowW
BringWindowToTop = ctypes.windll.user32.BringWindowToTop
SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow

class CodeSender:

    def __init__(self, view, cmd=None, prog=None, from_view=True, hwnd = None):
        self.view = view
        self.settings = Settings(view)
        if prog:
            self.prog = prog
        else:
            self.prog = self.settings.get("prog")
        self.from_view = from_view
        self.hwnd = hwnd

    @classmethod
    def initialize(cls, view, **kwargs):
        return CodeSender(view, **kwargs)

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
        return rid

    def bring_rgui_to_top(self, rid):
        
        #BringWindowToTop(rid)
        #SetForegroundWindow(rid)
        
        PostMessage(rid, int(0x0112), int(0xF020), 0) #minimize
        PostMessage(rid, int(0x0112), int(0xF120), 0) #restore

        PostMessage(self.hwnd, int(0x0112), int(0xF020), 0) #minimize
        PostMessage(self.hwnd, int(0x0112), int(0xF120), 0) #restore
        
    def post_to_rgui(self, rid, cmd):
        for char in cmd:
            PostMessage(rid, int(0x102), ord(char), 0)     
        PostMessage(rid, int(0x102), ord('\n'), 0)  