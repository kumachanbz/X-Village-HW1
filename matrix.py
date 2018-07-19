
import random

from copy import deepcopy

class Matrix:
    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.num_row=nrows
        self.num_col=ncols
        self.data=[]
        for i in range(self.num_row):
            temp=[]
            for j in range(self.num_col):
                temp.append(random.randint(0,9))
            self.data.append(temp)
        pass

    def add(self, m):
        """return a new Matrix object after summation"""
        if(self.num_row==m.num_row and self.num_col==m.num_col):
            temp=Matrix(self.num_row,self.num_col)
            for i in range(self.num_row):
                for j in range(self.num_col):
                    temp.data[i][j]=self.data[i][j]+m.data[i][j]
            return temp
        else:
            print('add error!')
            return None
        pass

    def sub(self, m):
        """return a new Matrix object after substraction"""
        if(self.num_row==m.num_row and self.num_col==m.num_col):
            temp=Matrix(self.num_row,self.num_col)
            for i in range(self.num_row):
                for j in range(self.num_col):
                    temp.data[i][j]=self.data[i][j]-m.data[i][j]
            return temp
        else:
            print('sub error!')
            return None
        pass

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        if(self.num_col==m.num_row):
            temp=Matrix(self.num_row,m.num_col)
            for i in range(self.num_row):
                for j in range(m.num_col):
                    adder=0
                    for n in range(self.num_col):
                        adder+=self.data[i][n]*m.data[n][j]
                    temp.data[i][j]=adder              
            return temp
        else:
            print('mul error!')
            return None
        pass

    def transpose(self):
        """return a new Matrix object after transpose"""
        temp=Matrix(self.num_col,self.num_row)
        for i in range(self.num_row):
            for j in range(self.num_col):
                temp.data[j][i]=self.data[i][j]
        return temp
        pass
    
    def display(self):
        """Display the content in the matrix"""
        for i in self.data:
            for j in i:
                print(j,end=' ')
            print(end='\n')
        pass

input_Arow=input('Enter A matrix\'s row:')
input_Acol=input('Enter A matrix\'s col:')
matrixA=Matrix(int(input_Arow),int(input_Acol))
print('Matrix A('+input_Arow+','+input_Acol+'):')
matrixA.display()

input_Brow=input('Enter B matrix\'s row:')
input_Bcol=input('Enter B matrix\'s col:')
matrixB=Matrix(int(input_Brow),int(input_Bcol))
print('Matrix B('+input_Brow+','+input_Bcol+'):')
matrixB.display()

print('========== A + B ==========')
ADD=matrixA.add(matrixB)
ADD.display()

print('========== A - B ==========')
SUB=matrixA.sub(matrixB)
SUB.display()

print('========== A * B ==========')
MUL=matrixA.mul(matrixB)
MUL.display()

print('==========the transpose of A * B ==========')
TRA=MUL.transpose()
TRA.display()