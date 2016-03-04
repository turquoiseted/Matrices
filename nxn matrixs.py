import math
# define an nxn matrixs

class Matrix(object):
    def __init__(self, row, col, data):
        self._no_of_row = row
        self._no_of_col = col
        self._data = data

    # print as a matrix
    def __str__(self):
        max_len = 1
        # find largest entry so can resize the print
        for x in range(len(self._data)):
            if max_len < len(str(round(self._data[x]))):
                max_len = len(str(round(self._data[x])))

        output = ""
        for height in range(self._no_of_row):
            output += self.print_row(height, max_len) + "\n"

        return output

    """
    returns a formatted copy of specified row    
    """
    def print_row(self, row_no, max_len):
        current_row = ""
        for length in range(self._no_of_col):
            addition = max_len - len(str(round(self._data[(row_no * self._no_of_col) + length])))
            current_row += str(round(self._data[(row_no * self._no_of_col) + length])) + " " * (1 + addition)

        return current_row

    def __repr__(self):
        return "Matrix: " + str(self._no_of_col) + "x" + str(self._no_of_row)

    # getters
    
    """
    returns the number of rows
    """
    def get_row(self):
        return self._no_of_row

    
    """
    returns the number of columns
    """
    def get_col(self):
        return self._no_of_col

    def get_raw_data(self):
        return self._data

    # define each row and column to easy calculation whilst still being easy to use
    def define_row(self, index):
        if index > self._no_of_row:
            raise ValueError("index out of range")
        else:
            current_row = []
            for x in range(self._no_of_col):
                current_row.append(self._data[x + index * self._no_of_col])
            return current_row

    def define_col(self, index):
        if index > self._no_of_col:
            raise ValueError("index out of range")
        else:
            current_col = []
            for x in range(self._no_of_row):
                current_col.append(self._data[x * self._no_of_col + index])
            return current_col



    def upper_triangular_form(self):
        rank = self._no_of_col
        new_data = self._data
        # goes throught the width of the lower triange
        for width in range(self._no_of_col):
            first_row = self.define_row(width)
            
            # take the first row and make first value 1
            divisor = first_row[width]
            # avoid division by 0
            if divisor != 0:
                for values in range(len(first_row)):
                    position = width*self._no_of_row+values
                    
                    del new_data[position]
                    new_data.insert(position, first_row[values] / divisor)
                    "this is fine"
                first_row = self.define_row(width)
                temp_row = []
                #x defines which row is being looked at
                for x in range(width+1, self._no_of_row):
                    temp_row = self.define_row(x)
                    multiplier = temp_row[width]
                    "multiplier is fine"
                    for item in range(width, self._no_of_col):
                        pos = x*self._no_of_col + item
                        "pos is fine now"
                        del new_data[pos]
                        "temprow is fine"
                        
                        new_value = temp_row[item] - (multiplier * first_row[item])
                        
                        new_data.insert(pos, new_value)
                else:
                    rank = width+1
        new_matrix = Matrix(self._no_of_row, self._no_of_row, new_data)
        print("rank:" + str(rank))
        return new_matrix

        # finish your slightly reduced matrix and cry

    def echelon_form(self):
        new_matrix = self.upper_triangular_form()
        return new_matrix

##    def get_det_echelon(self):
##        matrix = self.upper_triangular_form()
##        total = 1
##        for x in range(self._no_of_row):
##            print(matrix.define_row(x)[x])
##            total = total*matrix.define_row(x)[x]
##
##        return total

    def get_det_recur(self):
        if self._no_of_col != self._no_of_row:
            raise ValueError("Cannot have a det of a non square matrix")
        else:
            return self.det_recur()
             


    def det_recur(recur_matrix):
        """
    Recursive algorythm used to get the deteriminant of given matrix.
    The base case is when the size of the matrix is 1, the det of that is itself
    it then loops through adding or subtracting depending on the checkerboard
        """
        if recur_matrix.get_row() == 1:
            return recur_matrix.get_raw_data()[0]
        else:
            det = 0
            top_row = recur_matrix.define_row(0)
            for index in range(len(top_row)):
                
                start_data = recur_matrix.get_raw_data()
                row_data = recur_matrix.get_row()
                reduced_data = []
                for x in range(len(start_data)):
                    # tAGGHHhshh
                    if (x not in range(0,row_data)) and ((x%row_data) != index):
                        reduced_data.append(start_data[x])
                  
                reduced_matrix = Matrix(row_data - 1,row_data - 1, reduced_data)
                checkerboard = (-1)**index
                det = det + checkerboard*top_row[index]*reduced_matrix.det_recur()
            return det
        
    def invert_matrix_echelon(self):
        """
    Invert the matrix by reducing it to intentity and an indentity to the inverse
    start with upper trianglular form
        """
        if self.get_det_echelon() == 0:
            return False
        
        
     
    """
    Will calculate the eigen values of a 2x2 matrix
    """
    def eigenvalue(self):
        if (self._no_of_row != 2) or (self._no_of_col != 2):
            raise ValueError("Can only do 2x2 at present")
        else:
            equation = [1]
            data = self._data
            equation.append(-(data[0] + data[3]))
            equation.append(data[0] * data[3] - data[1] * data[2])
            
            return solve_quadratic(equation)

##    def eigenvector(self):
##        "tears"
##        eigenvalues = self.eigenvalue
##        for evalue in eigenvalues:
            
        
        
                

def add_matrix(mat1, mat2):
    """
    Adds two same sized matrices together
    """
    if (mat1.get_row() != mat2.get_row()) or (mat2.get_col() != mat2.get_col()):
        raise ValueError("Matrixes must have same dimensions to be added")
    else:
        new_matrix_data = []
        for length in range(mat1.get_row() * mat2.get_row()):
            new_matrix_data.append(mat1.get_raw_data()[length] + mat2.get_raw_data()[length])
            new_mat = Matrix(mat1.get_row(), mat1.get_col(), new_matrix_data)
        return new_mat


def sub_matrix(mat1, mat2):
    """
    Subtracts two same sized matrices together
    """
    if (mat1.get_row() != mat2.get_row()) or (mat2.get_col() != mat2.get_col()):
        raise ValueError("Matrixes must have same dimensions to be subtracted")
    else:
        new_matrix_data = []
        for length in range(mat1.get_row() * mat2.get_row()):
            new_matrix_data.append(mat1.get_raw_data()[length] - mat2.get_raw_data()[length])
            new_mat = Matrix(mat1.get_row(), mat1.get_col(), new_matrix_data)
        return new_mat


def multiply_matrix(mat1, mat2):
    """
    Multiplies two suitable matrices together
    """
    if mat1.get_row() != mat2.get_col():
        print(mat1.get_row())
        print(mat2.get_col())
        raise ValueError("Incompatible to be multiplied")
    else:
        final_mat = []
        for rows in range(mat1.get_row()):
            for cols in range(mat2.get_col()):
                # split into a column loop and row loop
                current = 0
                for index in range(mat1.get_col()):  # matching values
                    current += mat1.define_row(rows)[index] * mat2.define_col(cols)[index]
                final_mat.append(current)
        return final_mat

def solve_quadratic(equ):
    """
    Solves a given quadratic equation
    """
    a = equ[0]
    b = equ[1]
    c = equ[2]
    sols = []
    if (b**2 - 4*a*c) < 0:
        return False
    sols.append(((-b)+math.sqrt(b**2 - 4*a*c))/(2*a))
    sols.append(((-b)-math.sqrt(b**2 - 4*a*c))/(2*a))
    return sols
    

####TESTS####

mat_1 = Matrix(2, 2, [1, 2, 3, 4])
mat_2 = Matrix(2, 2, [5, 6, 7, 8])
mat_3 = Matrix(3, 2, [1, 2, 3, 4, 5, 6, 7, 8])
mat_4 = Matrix(2, 3, [1, 2, 3, 4, 5, 6, 7, 8])
mat_5 = Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
mat_6 = Matrix(4, 4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
mat_7 = Matrix(3, 3, [1, 2, 3, 4, 6, 5, 7, 8, 9])
mat_8 = Matrix(2, 2, [3, 2, 2, 0])
mat_9 = Matrix(2, 2, [-1, 0, 0, -1])


def tests():
    print(mat_1.get_det_recur())
    
    #quadratic equation tests
    assert solve_quadratic([1, 2, 1]) == [-1, -1]
    assert solve_quadratic([1, 2, -1]) == [-1 + math.sqrt(2), -1 - math.sqrt(2)]
    assert solve_quadratic([1, 2, 2]) == False

    #eigenvalue tests
    assert mat_9.eigenvalue() == ([-1, -1])
    assert mat_8.eigenvalue() == ([4, -1] or [-1, 4])

    #eigenvector tests
    #assert mat_8.eigenvalue() == ([[,],[,]])

    #inverse matrix tests
    assert mat_5.invert_matrix_echelon() == False

    #uppertriangle det tests
    #assert mat_1.get_det_echelon() == -2
    

tests()
