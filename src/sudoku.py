import fileHandler
import os
import time

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
        colSubgrid = y // 3
        rowSubgrid = x // 3
        for rowIdx in range(3 * rowSubgrid, 3 * rowSubgrid + 3):
            for colIdx in range(3 * colSubgrid, 3 * colSubgrid + 3):
                subgrid.append(self.sudokuMatrix[rowIdx][colIdx])

        return subgrid

    def getCoordinatesOf(self, num):
        coordinatesList = []
        for i, row in enumerate(self.sudokuMatrix):
            for j, square in enumerate(row):
                if square == num:
                    coordinatesList.append((i, j))
        coordinatesList.sort()

        return coordinatesList
        

    def checkCoordinateAvailability(self, num, x, y):
        # Check availability in Row
        if num in self.getRow(x):
            return False
        
        # Check availability in Column
        if num in self.getColumn(y):
            return False

        # Check availability in subgrid
        if num in self.getSubGrid(x, y):
            return False
        
        return True

    
    def preProcessing(self):
        # Naked single strategy
        for key, value in self.candidateMap.items():
            if len(value) == 1:
                self.sudokuMatrix[key[0]][key[1]] = value[0]

    def processing(self):
        # Inspired by Ajinkya Sonawane
        # https://medium.com/daily-python/solving-sudoku-puzzle-using-backtracking-in-python-daily-python-29-99a825042e
        for coordinate in self.candidateMap:
            if self.sudokuMatrix[coordinate[0]][coordinate[1]] == '#':
                for digit in self.candidateMap[coordinate]:
                    if self.checkCoordinateAvailability(digit, coordinate[0], coordinate[1]):
                        self.sudokuMatrix[coordinate[0]][coordinate[1]] = digit
                        check = self.solve()
                        if (check):
                            return True
                        self.sudokuMatrix[coordinate[0]][coordinate[1]] = '#' # Backtrack
                # Kalo for-nya abis, berarti salah di sebelum-sebelumnya
                return

        return True     

    def solve(self):
        self.preProcessing()
        result = self.processing()

        return result     

if __name__ == "__main__":
    sudokuPath = os.path.join(os.getcwd(), os.pardir, 'test')
    sudoku = Sudoku(fileHandler.loadSudokuText(os.path.join(sudokuPath, 'tc2.txt')))
    sudoku.printAsGrid()
    sudoku.printCandidatesMap()

    start = time.perf_counter_ns()
    sudoku.solve()
    end = time.perf_counter_ns()
    print(f'Time: {(end - start) / 1000000000} s')

    sudoku.printAsGrid()
    coordinatesList = sudoku.getCoordinatesOf('5')

    resultPath = os.path.join(os.getcwd(), os.pardir, 'result')
    fileHandler.writeCoordinatesToFile(coordinatesList, os.path.join(resultPath, 'tc2coordinates5.txt'))
    fileHandler.writeSudokuToFile(sudoku.sudokuMatrix, os.path.join(resultPath, 'tc2Solved.txt'))
    

    # print(sudoku.checkCoordinateAvailability('5', 4, 4))
    # print(sudoku.getColumn(5))
    # print(sudoku.getRow(4))
    # print(sudoku.getSubGrid(2, 4))

    