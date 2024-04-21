import StdDraw # the stddraw module is used as a basic graphics library
from Colors import Colors # used for coloring the tile and the number on it
from Point import Point # used for representing the position of the tile
import copy as cp # the copy module is used for copying tile positions
import math # math module that provides mathematical functions
import random
import numpy as np

# Class used for representing numbered tiles as in 2048
class tile:
   # Class attributes shared among all Tile objects
   # ---------------------------------------------------------------------------
   # value used for the thickness of the boxes (boundaries) around the tiles
   boundary_thickness = 0.004
   # font family and size used for displaying the tile number
   font_family, font_size = "Arial", 14

   # Constructor that creates a tile at a given position with 2 as its number
   def __init__(self, position = Point(0, 0)): # (0, 0) is the default position
      # Assigns the random number of the tile 2 or 4 for initial
      numbers = [2, 4]
      # Sets a background color for each possible number
      self.colors = [Colors(239, 230, 221), Colors(239, 227, 205), Colors(247, 178, 123), Colors(247, 150, 99), Colors(247, 124, 90),
                     Colors(247, 93, 59), Colors(239, 205, 115), Colors(239, 206, 99), Colors(239, 198, 82), Colors(238, 198, 66), Colors(239, 194, 49), Colors(60, 58, 51)]
      self.num = int(np.random.choice(numbers, 1))
      self.number = self.num
      # set the colors of the tile
      self.background_color = self.colors[int(math.log2(self.num))-1] # background (tile) color
      self.foreground_color = Colors(0, 100, 200) # foreground (number) color
      self.boundary_color = Colors(0, 100, 200) # boundary (box) color
      # set the position of the tile as the given position
      self.position = Point(position.x, position.y)

   # Setter method for the position of the tile
   def set_position(self, position):
      # set the position of the tile as the given position
      self.position = cp.copy(position)

   # Getter method for the position of the tile
   def get_position(self):
      # return the position of the tile
      return cp.copy(self.position)

   # Method for moving the tile by dx along the x axis and by dy along the y axis
   def move(self, dx, dy):
      self.position.translate(dx, dy)

   # Method for drawing the tile
   def draw(self, position = None):
      if position is None:
          position = self.position
      # draw the tile as a filled square
      StdDraw.setPenColor(self.background_color)
      StdDraw.filledSquare(self.position.x, self.position.y, 0.5)
      # draw the bounding box of the tile as a square
      StdDraw.setPenColor(self.boundary_color)
      StdDraw.setPenRadius(tile.boundary_thickness)
      StdDraw.square(self.position.x, self.position.y, 0.5)
      StdDraw.setPenRadius()  # reset the pen radius to its default value
      # draw the number on the tile
      StdDraw.setPenColor(self.foreground_color)
      StdDraw.setFontFamily(tile.font_family)
      StdDraw.setFontSize(tile.font_size)
      StdDraw.boldText(self.position.x, self.position.y, str(self.number))

   # Updates the background of the tile according to tile's number
   def updateColor(self, num):
      self.background_color = self.colors[int(math.log2(num)) - 1]