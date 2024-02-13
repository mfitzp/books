import os
import sys


class Paths:

    base = os.path.dirname(__file__)
    platform = os.path.join(
        base, sys.platform
    )  # platform specific folders
    images = os.path.join(base, "images")
    icons = os.path.join(platform, "icons")
    data = os.path.join(base, "images")

    # File loaders.
    @classmethod
    def icon(cls, filename):
        return os.path.join(cls.icons, filename)

    @classmethod
    def image(cls, filename):
        return os.path.join(cls.images, filename)

    @classmethod
    def data(cls, filename):
        return os.path.join(cls.data, filename)
