from ht16k33 import HT16K33


class Matrix5x7(HT16K33):
    """LTP-305 Matrix Display"""

    def pixel(self, x, y, color=None):
        """Get or set the color of a given pixel."""
        if not 0 <= x <= 4:
            return None
        if not 0 <= y <= 6:
            return None
        return super()._pixel(x, y, color)

    def __getitem__(self, key):
        x, y = key
        return self.pixel(x, y)

    def __setitem__(self, key, value):
        x, y = key
        self.pixel(x, y, value)
