import math
class Rectangle:
  '''
  When a Rectangle object is created, it should be initialized with width and height
  attributes. 

  '''
  def __init__(self,w,h):
    self.width = w
    self.height = h

  def __str__(self):
    #Rectangle(width=5, height=10)
    return (f"{__class__.__name__}(width={self.width}, height={self.height})")
    
  def set_width(self, w):
    self.width = w

  def set_height(self,h):
    self.height = h

  def get_area(self):
    #get_area: Returns area (width * height)
    return (self.width*self.height)

  def get_perimeter(self):
    #get_perimeter: Returns perimeter (2 * width + 2 * height)
    return (2*self.width+2*self.height)

  def get_diagonal(self):
    #get_diagonal: Returns diagonal ((width ** 2 + height ** 2) ** .5)
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    '''
    get_picture: Returns a string that represents the shape using lines of "*". 
    The number of lines should be equal to the height and the number of "*"
    in each line should be equal to the width. There should be a new line (\n)
    at the end of each line. If the 
    width or height is larger than 50, this should return the string: "Too big for picture."
    '''
    pic = ""
    if (self.width > 50 or self.height > 50):
      return "Too big for picture."
    for row in range(self.height):
      pic = pic + self.width*"*" + "\n"
    return pic

  def get_amount_inside(self, other_shape):
    '''
    get_amount_inside: Takes another shape (square or rectangle) as an argument.
    Returns the number of times the passed in shape could fit inside the shape
    (with no rotations). For instance, a 
    rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
    '''
    # diag_counter = 0
    # w_counter = 0
    # h_counter = 0
    # counter = 0
    # temp_shape = Rectangle(self.width, self.height)

    # #diagaonal measure to reduce down to where no diagonal possible, then w and h measures
    # while (temp_shape.width >= 2*other_shape.width and temp_shape.height >= 2*other_shape.height):
    #   diag_counter = diag_counter+4
    #   temp_shape.set_width( temp_shape.width-other_shape.width )
    #   temp_shape.set_height(temp_shape.height-other_shape.height)

    # while (temp_shape.width >= other_shape.width and temp_shape.height >= other_shape.height):
    #   counter = counter+1
    #   temp_shape.set_width( temp_shape.width-other_shape.width )
    #   temp_shape.set_height(temp_shape.height-other_shape.height)
    counter = math.floor(self.width/other_shape.width) * math.floor(self.height/other_shape.height)
    
    
    return counter



class Square(Rectangle):
  '''
  In this project you will use object oriented programming to create a 
  Rectangle class and a Square class. The Square class should be a 
  subclass of Rectangle and inherit methods and attributes.
  
  The Square class should be a subclass of Rectangle. 
  When a Square object is created, a single side length is passed in.
  The __init__ method should store the side length in both the width
  and height attributes from the Rectangle class.
  
  The Square class should be able to access the Rectangle class methods 
  but should also contain a set_side method. 
  If an instance of a Square is represented as a string, 
  it should look like: Square(side=9)
  
  Additionally, the set_width and set_height methods on the Square class 
  should set both the width and height.
  
  '''
  def __init__(self,side):
    self.width=side
    self.height=side

  def set_side(self, side):
    self.width=side
    self.height=side

  def __str__(self):
    #If an instance of a Square is represented as a string, it should look like: Square(side=9)
    return (f"{__class__.__name__}(side={self.width})")

  def set_width(self, side):
    self.set_side(side)

  def set_height(self,side):
    self.set_side(side)

  
    
