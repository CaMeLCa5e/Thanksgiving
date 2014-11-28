#!/usr/bin/python

class Guest:
   'Common base class for all guests'
   GuestCount = 0

   def __init__(self, name, turkeyConsumption):
      self.name = name
      self.turkeyConsumption = turkeyConsumption
      Guest.GuestCount += 1
   
   def displayCount(self):
     print "Total Guest %d" % Guest.empCount

   def displayGuest(self):
      print "Name : ", self.name,  ", Pounds of turkey eaten: ", self.turkeyConsumption

"This would create first object of Guest class"
gst1 = Guest("Jack", 6)
"This would create second object of Guest class"
gst2 = Guest("Joe", 5)
gst3 = Guest("Jayne(my sister)", 89)

gst1.displayGuest()
gst2.displayGuest()
gst3.displayGuest()

print "Total Guest %d" % Guest.GuestCount

print "Guest.__doc__:", Guest.__doc__
print "Guest.__name__:", Guest.__name__
print "Guest.__module__:", Guest.__module__
print "Guest.__bases__:", Guest.__bases__
print "Guest.__dict__:", Guest.__dict__