class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list = []

    def run(self):
        for entity in self.entity_list:
            entity.move()


 #class Level:

 #   def __init__(self):
  #      self.window = None
   #     self.name = None
    #    self.entity_list = None
     #   self.entity_list = None

    #def run(self, ):
     #       pass
