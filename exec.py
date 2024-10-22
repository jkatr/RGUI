import sublime_plugin


class RGUIExecCommand(sublime_plugin.WindowCommand):

    def run(self, code=None, prog=None):
        self.window.active_view().run_command(
            "rgui",
            {"code": code, "prog": prog}
        )

