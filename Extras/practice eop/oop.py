class Lion:
    def __init__(self, name, ht, wt):
        self.name = name
        self.ht = ht
        self.wt = wt

    def tell_your_data(self):
        print(f"Hello my name is {self.name} and my weight is {self.wt}")

    def eat(self, foodwt=1):
        self.wt += foodwt

    def __len__(self):
        return self.wt

    def __add__(self, other):
        return Lion(self.name, self.ht + other.ht, self.wt + other.wt)

    def __repr__(self):
        return f"lion <{self.name}, {self.ht}, {self.wt}>"


l = Lion("Jerry", 2, 120)
j = Lion("terry", 12, 30)
l.tell_your_data()
print(l.add(j))
print(l)
