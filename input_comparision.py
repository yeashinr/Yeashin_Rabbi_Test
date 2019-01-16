class compareInputs:
    
    def __init__(self, value1, value2):
        self.value1 = float(value1)
        self.value2 = float(value2)

    def greater_than(self):
        return f'{self.value1} is greater than {self.value2}' if self.value1 > self.value2 else \
               f'{self.value2} is greater than {self.value1}'
    
    def equal(self):
        return f'{self.value1} is equal to {self.value2}' if self.value1 == self.value2 else \
               f'{self.value1} is not equal to {self.value2}'
    
    def less_than(self):
        return f'{self.value1} is less than {self.value2}' if self.value1 < self.value2 else \
               f'{self.value2} is less than {self.value1}'


if __name__ == "__main__":
    str1 = input('Please, enter a string number:')
    str2 = input('Please, enter an another string number:')
    
    campare_values = compareInputs(str1,str2)
    print(campare_values.greater_than())
    print(campare_values.equal())
    print(campare_values.less_than())