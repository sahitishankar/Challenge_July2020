def prisonCellsNdays(cells,N):
    #cells have 8 elements these tend to repeat AFTER every 14 days
    # The cell on 0th day will same as 15th day
    if N>14:
        N = N%14

    if N%14 == 0:
        N = 14

    for _ in range(1,N+1):
        temp=[0]*len(cells)
        for i in range(1,len(cells)-1):
            if cells[i-1] == cells[i+1]:
                temp[i] = 1
            else:
                temp[i] = 0
        cells = temp
    print(cells)
prisonCellsNdays([0,1,0,1,1,0,0,1],7)
        



