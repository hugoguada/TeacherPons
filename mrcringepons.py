import math
#Espero qu funcione este commit porque sino la camiseta se la va a llevar Piter
class Point3D:

    #A point is defined by 3 coordinates(x, y , z)
    #Commit 1: __init__(constructor), setters, getters and __str__ (tostring)
    def __init__(self, punt_x, punt_y, punt_z):
        self.punt_x = punt_x
        self.punt_y = punt_y
        self.punt_z = punt_z

    def __init__(self):
        pass

     def get_x(self):
        return self.punt_x

    def set_x(self, punt_x):
        self.punt_x = punt_x

    def get_y(self):
        return self.punt_y

    def set_y(self, punt_y):
        self.punt_y = punt_y

    def get_z(self):
        return self.punt_z

    def set_z(self, punt_z):
        self.punt_z = punt_z

    def __str__(self):
        return str(self.get_x) + ", " + str(self.get_y) + ", " + str(self.get_z) + "."
