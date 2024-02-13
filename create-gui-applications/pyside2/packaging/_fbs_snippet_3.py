from fbs_runtime.application_context.PySide2 import ApplicationContext, cached_property


class AppContext(ApplicationContext):

    # ... snip ...

    @cached_property
    def img_bomb(self):
        return QImage(self.get_resource("images/bug.png"))

    @cached_property
    def img_flag(self):
        return QImage(self.get_resource("images/flag.png"))

    @cached_property
    def img_start(self):
        return QImage(self.get_resource("images/rocket.png"))

    @cached_property
    def img_clock(self):
        return QImage(self.get_resource("images/clock-select.png"))

    @cached_property
    def status_icons(self):
        return {
            STATUS_READY: QIcon(self.get_resource("images/plus.png")),
            STATUS_PLAYING: QIcon(self.get_resource("images/smiley.png")),
            STATUS_FAILED: QIcon(self.get_resource("images/cross.png")),
            STATUS_SUCCESS: QIcon(self.get_resource("images/smiley-lol.png")),
        }


# ... snip ...
