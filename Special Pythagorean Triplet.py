
def pythagorean():
	d = 0
	for a in range(1,500):
		if d!=0:
			break
		else:
			for b in range(a,500):
				c = 1000 -a -b
				print(a, " + ", b, " = ", c)
				if (a**2 + b**2)==c**2 :
					d = a*b*c
					print(a," + ",b," = ",c)
					print("Their product is ",d)
					break

def main():
	pythagorean()

if __name__=="__main__":
	main()