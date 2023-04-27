def trace(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(i == j):
                sum += matrix[i][j]
    return sum

def main():
    print("This program calculates the trace of a square matrix.")
    matrix = [[4,5,7,3,2], [7,5,8,5,6], [8,2,1,2,1], [3,3,6,4,7], [6,4,9,5,3]]
    #print(matrix)
    result = trace(matrix)
    print("The trace of the matrix is: " + str(trace(matrix)))

if __name__ == "__main__":
    main()