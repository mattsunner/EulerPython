"""
prob11.py

In the 20 x 20 grid in the prob11.csv, four numbers along a diagonal line have been marked in red (26, 63, 78, 14).

The product of these numbers is 26 * 63 * 78 * 14 = 1,788,696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid?


"""
import csv


class MatrixSolver:

    def __init__(self, csv_path):
        self.csv_path = csv_path


    def _matrix_generator(self) -> list:    
        full_matrix = []

        with open(self.csv_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader: 
                full_matrix.append(row)
        
        return full_matrix


    def max_sums_generator(self):
        matrix = self._matrix_generator()
        mat = [[int(num) for num in row] for row in matrix]      
        max_product = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if j <= len(mat[i]) - 4:
                    product = mat[i][j] * mat[i][j + 1] * mat[i][j + 2] * mat[i][j + 3]
                    max_product = max(max_product, product)

                if i <= len(mat) - 4:
                    product = mat[i][j] * mat[i + 1][j] * mat[i + 2][j] * mat[i + 3][j]
                    max_product = max(max_product, product)

                if i <= len(mat) - 4 and j <= len(mat[i]) - 4:
                    product = mat[i][j] * mat[i + 1][j + 1] * mat[i + 2][j + 2] * mat[i + 3][j + 3]
                    max_product = max(max_product, product)

                if i <= len(mat) - 4 and j >= 3:
                    product = mat[i][j] * mat[i + 1][j - 1] * mat[i + 2][j - 2] * mat[i + 3][j - 3]
                    max_product = max(max_product, product)
        
        return max_product

if __name__ == '__main__':
    file_name = 'prob11.csv'
    
    mat = MatrixSolver(csv_path=file_name)

    max_product = mat.max_sums_generator() 

    print(f"The greatest product of four adjacent numbers in the grid is: {max_product}")

