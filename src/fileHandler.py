import os
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def loadSudokuText(filename):
    with open(filename) as f:
        sudokuMatrix = f.read().split('\n')
        for i in range(len(sudokuMatrix)):
            sudokuMatrix[i] = sudokuMatrix[i].split(' ')

    return sudokuMatrix

def loadSudokuImage(filename):
    img = Image.open(filename)

    maxWidth = img.size[0]
    maxHeight = img.size[1]

    sudokuMatrix = []
    numbers = [str(x) for x in range(1, 10)]

    for i in range(9):
        sudokuMatrix.append([])
        for j in range(9):
            top = maxWidth * i / 9
            bottom = maxWidth * (i + 1) / 9
            left = maxHeight * j / 9
            right = maxHeight * (j + 1) / 9

            square = img.crop((left + 4, top + 2.5, right - 2, bottom - 2)) 
            text = pytesseract.image_to_string(square, config='--psm 7 -c tessedit_char_whitelist=0123456789')
            if text not in numbers:
                text = '#' # Symbol for blank
            sudokuMatrix[i].append(text)

    return sudokuMatrix

def writeSudokuToFile(sudokuMatrix, filename):
    with open(filename, 'w') as f:
        f.write('Solved Puzzle:\n')
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
    with open(filename, 'a') as f:
        f.write('\nCoordinate of 5:\n')
        for coordinate in coordinatesList:
            f.write(f'{coordinate}\n')

if __name__ == "__main__":
    sudokuPath = os.path.join(os.getcwd(), os.pardir, 'test')
    print(loadSudokuText(os.path.join(sudokuPath, 'tc1.txt')))
    matrix = loadSudokuImage(os.path.join(sudokuPath, 'image1.png'))
    print(matrix)