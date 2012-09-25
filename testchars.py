import time
import types
import json
import Adafruit_8x8


a = Adafruit_8x8.EightByEight()
a.clear();

# load the alphbet definition
fp = open('chars.json', 'r')
chars = json.load(fp);

def showMatrix(matrix):
	idx = 0
	for num in matrix:
		a.writeRowRaw(idx, ((num&1)<<7) + (num>>1));
		idx += 1


# traverse the whole alphabet one char at a time
while True:
	for symbol, matrix in chars.iteritems():
		if isinstance(matrix[0], types.ListType):
			# animation detected! play it!
			for m in matrix:
				showMatrix(m)
				time.sleep(0.1)
		else:
			showMatrix(matrix)

		time.sleep(0.25)
