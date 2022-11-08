import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def get_row(matrix, row):
        return matrix[row]  
    
def get_column(matrix, column_number):
        column = []
        for r in range(len(matrix)):
            column.append(matrix[r][column_number])

        return column
    
def dot_product(vector_one, vector_two):
        result = 0
    
        for i in range(len(vector_one)):
            result += vector_one[i] * vector_two[i]

        return result    

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here    
        #determinant for matrix of size 1
        if self.h==1:
            result=self.g[0][0]
            
        #determinant for matrix size 2    
        else:
            a=self.g[0][0]
            b=self.g[0][1]
            c=self.g[1][0]
            d=self.g[1][1]
            result = a*d - b*c
        
        return result        
        

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        result=0
        for i in range(self.h):
            for j in range(self.w):
                if i==j:
                    result=result+self.g[i][j]
                    
      
            
        return result  
          

        
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
            
        # TODO - your code here
        
        #inverse for matrix of size 1x1
        if self.h==1:
            if self.g[0][0]!=0:
                result=[[1/self.g[0][0]]]
            else:
                raise (RuntimeError,'Given 1x1 matrix is non-invertible')
        
        #inverse for matrix of size 2x2
        else:
            det_matrix=self.determinant()
            if (det_matrix)==0:
                raise (RuntimeError,'Given 2x2 matrix is non-invertible')
            else:
                a=self.g[0][0]
                b=self.g[0][1]
                c=self.g[1][0]
                d=self.g[1][1]
                result = [[d/det_matrix,-b/det_matrix],[-c/det_matrix,a/det_matrix]]
                
        return Matrix(result)    

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        #Transpose of matrix of size 1x1
        if self.h==1:
            result=self.g
            
        #Transpose of matrix of size 2x2    
        else:
            #start with a zero matrix of same size as self and later change zeroes with correct entries of self transposed
            result=[]
            
            for j in range(self.h):
                new_row=[]
                for i in range(self.w):
                    element=self.g[i][j]
                    new_row.append(element)
                result.append(new_row)    
        return Matrix(result)            

            
            
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #start with a zero matrix of same size
        result=zeroes(self.h,self.w).g
        for i in range(self.h):
            for j in range(self.w):
                result[i][j]=self[i][j] + other[i][j]
                
        return Matrix(result)        
        #

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        result=zeroes(self.h,self.w).g
        for i in range(self.h):
            for j in range(self.w):
                result[i][j]= -1*self[i][j]
                
        return Matrix(result)        
        #

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
              
        #start with a zero matrix of same size
        result=self.g
        for i in range(self.h):
            for j in range(self.w):
                result[i][j]=self[i][j]-other[i][j]
                
        return Matrix(result)
        #

        
        

        
        
        
        
        
        
        
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        result=[]
        for i in range(self.h):
            row_result=[]
            for j in range(other.w):
                row=get_row(self.g,i)
                column=get_column(other.g,j)
                element=dot_product(row,column)
                row_result.append(element)
            result.append(row_result)
            
        return Matrix(result)    

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            
            result=self.g
            for i in range(self.h):
                for j in range(self.w):
                    result[i][j]=other*self[i][j]
            return Matrix(result)        
            