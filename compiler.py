import os

filename = input("Please enter the filename: ")
f = open(filename, "r").read().splitlines()

cells = [0] * 128
currentcell = 0
loopnum = 0
loops = []
output = ""

for line in f:
	for char in line:

		if (char == ">"):
			currentcell += 1
		elif (char == "<"): 
			if currentcell > 0:
				currentcell -= 1
			else:
				currentcell = 0
		elif (char == "+"):
			cells[currentcell] += 1
		elif (char == "-"):
			cells[currentcell] -= 1
		elif (char == "."): 
			output += chr(cells[currentcell])
		elif (char == ","):
			cells[currentcell] = ord(input("Type a char: "))
		elif (char == "["):
			loops[loopnum] = [currentcell, ""]
			loopnum += 1
		elif (char == "]"):
			print("Nothing yet")


print(output)