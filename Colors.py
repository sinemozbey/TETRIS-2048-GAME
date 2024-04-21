class Colors:

    def __init__(self, red=0, green=0, blue=0):
        """
        Initializes a Color object with the given RGB components.
        """
        self.red = red
        self.green = green
        self.blue = blue

    def getRed(self):
        """
        Returns the red component of the color.
        """
        return self.red

    def getGreen(self):
        """
        Returns the green component of the color.
        """
        return self.green

    def getBlue(self):
        """
        Returns the blue component of the color.
        """
        return self.blue

    def __str__(self):
        """
        Returns a string representation of the color in the form '(r, g, b)'.
        """
        return '(' + str(self.red) + ', ' + str(self.green) + ', ' + \
            str(self.blue) + ')'


# Predefined Color objects:

WHITE      = Colors(255, 255, 255)
BLACK      = Colors(0, 0, 0)

RED        = Colors(255, 0, 0)
GREEN      = Colors(0, 255, 0)
BLUE       = Colors(0, 0, 255)

CYAN       = Colors(0, 255, 255)
MAGENTA    = Colors(255, 0, 255)
YELLOW     = Colors(255, 255, 0)

DARK_RED   = Colors(128, 0, 0)
DARK_GREEN = Colors(0, 128, 0)
DARK_BLUE  = Colors(0, 0, 128)

GRAY       = Colors(128, 128, 128)
DARK_GRAY  = Colors(64, 64, 64)
LIGHT_GRAY = Colors(192, 192, 192)

# A very light shade of orange
ORANGE     = Colors(255, 200, 0)
# A very light shade of violet
VIOLET     = Colors(238, 130, 238)
# A very light shade of pink
PINK       = Colors(255, 175, 175)

# Shade of blue used in Introduction to Programming in Java.
# Approximately Pantone 300U.
BOOK_BLUE  = Colors(9, 90, 166)
BOOK_LIGHT_BLUE = Colors(103, 198, 243)

# Shade of red used in Algorithms 4th edition
BOOK_RED   = Colors(150, 35, 31)

def _main():
    """
    Test function.
    """
    c1 = Colors(0, 128, 255)
    print(c1)
    print(c1.getRed())
    print(c1.getGreen())
    print(c1.getBlue())

if __name__ == '__main__':
    _main()
