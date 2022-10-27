class Gadjet:
    korobka = 'имеет коробку'

    def __init__(self, sost, model, name):
        self.sost = sost
        self.name = name
        self.model = model
    
    def apprat(self):
        pass

class Phone(Gadjet):
    

    def apprat(self, color, case):
        self.color = color
        self.case = case
        print(f'model: {self.model} sost: {self.sost} name:: {self.name} color: {self.color} case: {self.case}')

egor = Phone('б/у', 'x', 'iphone')

egor.apprat('white', 'netu')

print(egor)