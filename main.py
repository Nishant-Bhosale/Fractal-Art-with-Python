from turtle import *

shape('turtle')
speed(0)

def tree(size, levels, angle):
   if levels == 0:
      color('green')
      dot(size)
      color('black')
      return
   forward(size)
   right(angle)

   tree(size * 0.8, levels - 1, 30 )

   left(angle * 2)
   tree(size * 0.8, levels - 1, angle)

   right(angle)
   backward(size)

def snowflake_side(length, levels):
   if levels == 0:
      forward(length)
      return 
   
   length /= 3.0
   snowflake_side(length, levels -1)
   left(60)
   snowflake_side(length, levels -1)
   right(120)
   snowflake_side(length, levels -1)
   left(60)
   snowflake_side(length, levels -1)

def create_snowflake():
   pass

# left(90)
# tree(70, 5, 30)

snowflake_side(200, 3)
mainloop()