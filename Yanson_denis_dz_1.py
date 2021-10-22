class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.txt = ''
        for i in self.matrix:
            for v in i:
                self.txt += str(v) + '  '
            self.txt += '\n'
    def __str__(self):
        return self.txt
    def __add__(self, other):
        if len(other.matrix) > len(self.matrix):
            fst_mx = other.matrix
            scnd_mx =  self.matrix
        else:
            fst_mx = self.matrix
            scnd_mx = other.matrix
        big_mx = []
        for i, val in enumerate(fst_mx):
            lil_mx = []
            if len(val) > len(scnd_mx[i]):
                fst_list = val
                scnd_list = scnd_mx[i]
            else:
                fst_list = scnd_mx[i]
                scnd_list = val
            for i_2, v in enumerate(fst_list):
                if i_2 < len(scnd_list):
                    summary = v + scnd_list[i_2]
                else:
                    summary = v
                lil_mx.append(summary)
            big_mx.append(lil_mx)
        return Matrix(big_mx)


print(len([[31, 22], [37, 43], [51, 86]]))
print(Matrix([[31, 22], [37, 43], [51, 86]]))
print('\n\n')
print(Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]]))
print('\n\n')
print(Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])+Matrix([[3, 5, 8, 3], [8, 3, 7, 1]]))