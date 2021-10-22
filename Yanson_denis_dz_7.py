class ComplexNumber:
    def __init__(self, numb1, oper, numb2):
        self.numb1 = numb1
        self.numb2 = numb2
        self.oper = oper
    def __str__(self):
        strin=f'{self.numb1}{self.oper}{self.numb2}i'
        return strin
    def __add__(self, other):
        numb1 = self.numb1 + other.numb1
        if self.oper == other.oper:
            numb2 = self.numb2 + other.numb2
            oper = self.oper
        else:
            numb2 = self.numb2 - other.numb2
            if numb2<0:
                if self.oper == '-':
                    oper = '+'
                else:
                    oper = '-'

                numb2 = ~numb2+1
            else:
                if self.oper == '-':
                    oper = '-'
                else:
                    oper = '+'
                    print(self.numb1)
        return ComplexNumber(numb1,oper,numb2)
    def __mul__(self, other):
        if self.oper == '-':
            numb2_1 = ~self.numb2 + 1
        else:
            numb2_1 = self.numb2
        if other.oper == '-':
            numb2_2 = ~other.numb2 + 1
        else:
            numb2_2 = other.numb2
        numb1 = (self.numb1*other.numb1) - (numb2_1*numb2_2)
        numb2 = (self.numb1*numb2_2)+(other.numb1*numb2_1)
        if numb2<0:
            oper = '-'
            numb2 = ~numb2 + 1
        else:
            oper = '+'
        return ComplexNumber(numb1, oper, numb2)





compnumb_1=ComplexNumber(3, "+", 1)
compnumb_2=ComplexNumber(2, "-", 3)
compnumb_3=compnumb_1+compnumb_2
print(compnumb_3)
compnumb_3=compnumb_1*compnumb_2
print(compnumb_3)
