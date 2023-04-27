def copy_1d_to_2dlist(onedlist, twodlist):
    n = len(onedlist)
    j = len(twodlist)
    k = len(twodlist[0])

    if n != j * k:
        print("Error: they are not compatible!")
        return

    r = 0
    for i in range(0, j):
        for l in range(0, k):
            twodlist[i][l] = onedlist[r]
            r += 1
    
    return

def main():
    print("This program copies a 1-dimensional list into a 2-dimensional list.")
    onedlist = [1,2,3,4,5,6]
    twodlist = [[0,0,0],[0,0,0]]
    copy_1d_to_2dlist(onedlist,twodlist)
    #print(twodlist)

if __name__ == '__main__':
    main()
