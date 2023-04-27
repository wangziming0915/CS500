def search_first_squareblock( matrix : list[ list[int] ] ) -> tuple[int, int, int]:
    indexX = -1
    indexY = -1
    size = 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            if(matrix[i][j] != 0 and not matrix[i - 1][j] == 0  and not matrix[i - 1][j - 1] == 0 and not matrix[i][j - 1] == 0):
                matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                if(matrix[i][j] >= 3):
                    if indexX == -1 and indexY == -1:
                        indexX = i - matrix[i][j] + 1
                        indexY = j - matrix[i][j] + 1
                        size = matrix[i][j]
                    else:
                        curX = i - matrix[i][j] + 1
                        curY = j - matrix[i][j] + 1
                        if(curX == indexX and curY == indexY):
                            size = matrix[i][j]
    return [indexX, indexY, size]

def main():
    matrix: list[ list[int] ] = []
    matrixSize = int(input("Please enter the size of your matrix: "))
    if matrixSize < 5:
        print("Rows should be at least 5.")
    else:
        print("Enter the matrix row by row: ")
        for i in range(matrixSize):
            inputString = input().split(" ")
            intList: list = []
            for j in range(len(inputString)):
                intList.append(int(inputString[j]))
            matrix.append(intList)
            
        ResultTuple  = search_first_squareblock(matrix)
        print(f"The first square submatrix is at ({ResultTuple[0]}, {ResultTuple[1]}) with size {ResultTuple[2]}")

if __name__ == "__main__":
    main()
