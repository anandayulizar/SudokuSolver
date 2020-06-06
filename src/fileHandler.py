import os

def loadSudokuText(filename):
    with open(filename) as f:
        sudokuMatrix = f.read().split('\n')
        for i in range(len(sudokuMatrix)):
            sudokuMatrix[i] = sudokuMatrix[i].split(' ')

    return sudokuMatrix

def loadSudokuImage(filename):
    pass

def writeSudokuToFile(sudokuMatrix, filename):
    with open(filename, 'w') as f:
        f.write('-'*37 + '\n')
        for i, row in enumerate(sudokuMatrix):
            f.write(('| {}   {}   {} '*3).format(*[x for x in row]) + "|\n")
            if (i == 8):
                f.write('-' * 37 + '\n')
            elif (i % 3 == 2):
                # f.write('|' + '---+---+---+'*2 + '---+---+---|')
                f.write('|' + '-'*35 + '|\n')
            else:
                # f.write('|' + '   +   +   +'*2 + '   +   +   |')
                pass

def writeCoordinatesToFile(coordinatesList, filename):
    with open(filename, 'w') as f:
        for coordinate in coordinatesList:
            f.write(f'{coordinate}\n')






if __name__ == "__main__":
    sudokuPath = os.path.join(os.getcwd(), os.pardir, 'test')
    print(loadSudokuText(os.path.join(sudokuPath, 'tc1.txt')))