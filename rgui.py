import sublime
import sublime_plugin

from .code_getter import CodeGetter
from .code_sender import CodeSender

class RguiCommand(sublime_plugin.TextCommand):

    def run(self, edit, code=None, prog=None, resolve=True, all=None):
        # set CodeSender before get_code() because get_code may change cursor locations.
        if all:
            self.view.run_command("select_all")

        getter = CodeGetter(self.view)
        sender = CodeSender(self.view, prog=prog, hwnd = self.view.window().hwnd())


        if code and resolve:
            code = getter.resolve(code)
        else:
            code = getter.get_code()

        if not code.strip():
            return    
        
        sublime.set_timeout_async(lambda: sender.send_text(code))

