import sys, json

def read_in() :
	lines = sys.stdin.readline()
	return lines

def main() :
        while 1 :
                line = read_in()
                print line
"""
	total_sum_inArray = 0

	for item in lines :
		total_sum_inArray += item

	print total_sum_inArray
"""
if __name__ == '__main__':
	main()
