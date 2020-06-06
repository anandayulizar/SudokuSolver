import loader
import os

class Sudoku(object):
    def __init__(self, sudokuMatrix):
        self.sudokuMatrix = sudokuMatrix

    def printSudokuTable(self):
        # Inspirated by https://stackoverflow.com/questions/37952851/formating-sudoku-grids-python-3
        # Blckknght's answer
        print('-'*37)
        for i, row in enumerate(self.sudokuMatrix):
            print(('| {}   {}   {} '*3).format(*[x for x in row]) + "|")
            if (i == 8):
                print('-' * 37)
            elif (i % 3 == 2):
                # print('|' + '---+---+---+'*2 + '---+---+---|')
                print('|' + '-'*35 + '|')
            else:
                # print('|' + '   +   +   +'*2 + '   +   +   |')
                pass
        

    def checkCoordinateAvailability(self, num, x, y):
        # Check availability in Row
        if num in self.sudokuMatrix[x]:
            print('Already exists in row')
            return False
        
        # Check availability in Column
        for row in self.sudokuMatrix:
            if row[y] == num:
                print('Already exists in col')
                return False

        # Check availability in subgrid
        colSubgrid = x // 3
        rowSubgrid = y // 3
        for rowIdx in range(3 * rowSubgrid, 3 * rowSubgrid + 3):
            for colIdx in range(3 * colSubgrid, 3 * colSubgrid + 3):
                if self.sudokuMatrix[rowIdx][colIdx] == num:
                    print('Already exists in subgrid')
                    return False
        
        print('Doesn\'t exist yet')
        return True
        

if __name__ == "__main__":
    sudokuPath = os.path.join(os.getcwd(), os.pardir, 'test')
    sudoku = Sudoku(loader.loadSudokuText(os.path.join(sudokuPath, 'tc1.txt')))
    sudoku.printSudokuTable()

    a = sudoku.checkCoordinateAvailability('2', 1, 5)