import loader
import os

class Sudoku(object):
    def __init__(self, sudokuMatrix):
        self.sudokuMatrix = sudokuMatrix
        self.candidateMap = {}
        for i, row in enumerate(self.sudokuMatrix):
            for j, square in enumerate(row):
                candidates = [str(x) for x in range(1, 10)]
                if square == '#':
                    # Delete candidates present in a row
                    for num in self.getRow(i):
                        if num in candidates and num != '#':
                            candidates.remove(num)
                    
                    # Delete candidates present in a column
                    for num in self.getColumn(j):
                        if num in candidates and num != '#':
                            candidates.remove(num)

                    # Delete candidates present in a subgrid
                    for num in self.getSubGrid(i, j):
                        if num in candidates and num != '#':
                            candidates.remove(num)

                    self.candidateMap[(i, j)] = candidates


    # Print Function
    def printCandidatesMap(self):
        for key, value in self.candidateMap.items():
            print(f'{key}: {value}')

    def printAsGrid(self):
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

    # Getter

    def getColumn(self, y):
        return [row[y] for row in self.sudokuMatrix]

    def getRow(self, x):
        return self.sudokuMatrix[x]

    def getSubGrid(self, x, y):
        subgrid = []
        colSubgrid = x // 3
        rowSubgrid = y // 3
        for rowIdx in range(3 * rowSubgrid, 3 * rowSubgrid + 3):
            for colIdx in range(3 * colSubgrid, 3 * colSubgrid + 3):
                subgrid.append(self.sudokuMatrix[rowIdx][colIdx])

        return subgrid
        

    def checkCoordinateAvailability(self, num, x, y):
        # Check availability in Row
        if num in self.getRow(x):
            print('Already exists in row')
            return False
        
        # Check availability in Column
        if num in self.getColumn(y):
            print('Already exists in col')
            return False

        # Check availability in subgrid
        if num in self.getSubGrid(x, y):
            print('Already exists in subgrid')
            return False
        
        print('Doesn\'t exist yet')
        return True

    def preProcessing(self):
        pass

    # def nakedSingle(self):
    #     for key, value in self.sudokuMatrix:
    #         if len(value) == 1:
    #             self.sudokuMatrix[key[0]][key[1]] = value[0]
    #             del self.candidateMap[key]

    


        
if __name__ == "__main__":
    sudokuPath = os.path.join(os.getcwd(), os.pardir, 'test')
    sudoku = Sudoku(loader.loadSudokuText(os.path.join(sudokuPath, 'tc1.txt')))
    sudoku.printAsGrid()

    print(sudoku.checkCoordinateAvailability('5', 4, 4))
    # sudoku.printCandidatesMap()
    # print(sudoku.getColumn(5))
    # print(sudoku.getRow(4))
    # print(sudoku.getSubGrid(4,5))

    