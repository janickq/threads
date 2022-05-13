class objtest:

    def __init__(self, obj1 =2, obj2 =2):
        self.obj1 = obj1
        self.obj2 = obj2
    
    def increment_obj1(self, arg):
        self.obj1 = self.obj1 + arg
        return self.obj1
    def multiply_obj2(self, arg):
        self.obj2 = self.obj2*arg
        return self.obj2