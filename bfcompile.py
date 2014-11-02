import os

filename = input("Please enter the filename: ")
f = open(filename, "r").read().splitlines()

source = ""

for line in f:
	for char in line:
		source += char

cells = [0] * 128
currentcell = 0
output = ""
currentchar = 0
loops = []

while currentchar < len(source):
	if (source[currentchar] == ">"):
		currentcell += 1
	elif (source[currentchar] == "<"): 
		currentcell -= 1
	elif (source[currentchar] == "+"):
		cells[currentcell] += 1
	elif (source[currentchar] == "-"):
		cells[currentcell] -= 1
	elif (source[currentchar] == "."): 
		output += chr(cells[currentcell])
	elif (source[currentchar] == ","):
		cells[currentcell] = ord(input("Type a char: "))
	elif (source[currentchar] == "["):
		loops.append([currentcell, currentchar])
	elif (source[currentchar] == "]"):
		if loops[-1]:
			if cells[currentcell] > 0:
				currentchar = loops[-1][1]
			else:
				loops.pop()
		
	currentchar += 1

print(output)