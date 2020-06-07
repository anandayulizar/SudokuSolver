import os
import fileHandler
from sudoku import Sudoku

if __name__ == "__main__":
    print('Welcome to sudoku solver Mr.Khun!\nSolve one of the puzzle of your choosing and find the coordinates of the crystal to pass the test!')
    sudokuPath = os.path.join(os.getcwd(), os.pardir, 'test')
    fileList = os.listdir(sudokuPath)
    print('Available test cases:')
    for i, file in enumerate(fileList):
        print(f'{i + 1}. {file}')

    tcInput = int(input('Choose a test case: '))
    while (tcInput > len(fileList) or tcInput < 1):
        tcInput = int(input('Please input a valid test case: '))
    tcChosen = fileList[tcInput - 1]
    
    tcSplit = tcChosen.split('.')
    # tcType = tcChosen.split('.')[1]

    if (tcSplit[1] == 'txt'):
        sudoku = Sudoku(fileHandler.loadSudokuText(os.path.join(sudokuPath, tcChosen)))
    else:
        print('Please wait a moment to read the image')
        sudoku = Sudoku(fileHandler.loadSudokuImage(os.path.join(sudokuPath, tcChosen)))
    
    print('Before: ')
    sudoku.printAsGrid()
    userInput = input('Can you solve it? (type anything here) ')
    print('Solving puzzle...')
    isSolved = sudoku.solve()
    if (isSolved):
        print('After:')
        sudoku.printAsGrid()
        userInput = input('Congratulations! You solved the puzzle!\nDo you know where the crystal is located then? (type anything here)')
        coordinatesList = sudoku.getCoordinatesOf('5')
        print('List of crystal (5) coordinates:')
        for coordinate in coordinatesList:
            print(coordinate)

        resultPath = os.path.join(os.getcwd(), os.pardir, 'result')
        
        fileHandler.writeSudokuToFile(sudoku.sudokuMatrix, os.path.join(resultPath, tcSplit[0] + 'solved.txt'))
        fileHandler.writeCoordinatesToFile(coordinatesList, os.path.join(resultPath, tcSplit[0] + 'solved.txt'))

        print('Thank you for coming! Come again another time!')
    else:
        print('Hmm... Something\'s not right here... Try again another time!')

    