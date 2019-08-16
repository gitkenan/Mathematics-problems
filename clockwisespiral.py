def matrix_spiral_print(M):
	spiral_set = []
	# to append the top row
	for i in range(0, len(M[0]) - 1):
		spiral_set.append(M[0][i])
	# append right-hand column
	for i in range(0, len(M) - 1):
		spiral_set.append(M[i][len(M[i]) - 1])
	# append bottom row
	for i in range(0, len(M[- 1])):	
		spiral_set.append(M[- 1][- 1 - i])
	
	first_column = []
	
	for i in range(0, len(M) - 2):
		first_column.append(M[i + 1][0])
	
	first_column = list(reversed(first_column))
	
	for i in first_column:
		spiral_set.append(i)
		
	print spiral_set
	
grid = [[1,  2,  3,  4,   5],
		[6,  7,  8,  9,  10],
		[11 ,12 ,13 ,14 ,15],
		[16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
