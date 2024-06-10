import os


class Paths:

    base = os.path.dirname(__file__)
    ui_files = os.path.join(base, "ui")
    images = os.path.join(base, "images")
    icons = os.path.join(images, "icons")
    data = os.path.join(base, "images")

    # File loaders.
    @classmethod
    def ui_file(cls, filename):
        return os.path.join(cls.ui_files, filename)

    @classmethod
    def icon(cls, filename):
        return os.path.join(cls.icons, filename)

    @classmethod
    def image(cls, filename):
        return os.path.join(cls.images, filename)

    @classmethod
    def data(cls, filename):
        return os.path.join(cls.data, filename)
