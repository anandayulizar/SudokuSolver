import os

def loadSudokuText(filename):
    with open(filename) as f:
        sudokuMatrix = f.read().split('\n')
        for i in range(len(sudokuMatrix)):
            sudokuMatrix[i] = sudokuMatrix[i].split(' ')

    return sudokuMatrix






if __name__ == "__main__":
    sudokuPath = os.path.join(os.getcwd(), os.pardir, 'test')
    print(loadSudokuText(os.path.join(sudokuPath, 'tc1.txt')))