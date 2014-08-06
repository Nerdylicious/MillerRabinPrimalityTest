import math

def SquareAndMultiply(x, c, n):

	c = '{0:b}'.format(c)
	z = 1
	l = len(c)

	for i in range(0, l):
		z = (math.pow(z, 2)) % n
		if (c[i] == "1"):
			z = (z*x) % n
	z = int(z)
	return z

def MillerRabin(a, n, k, m):
	
	b = SquareAndMultiply(a, m, n)
	if (b % n == 1):
		return False
	for i in range(0, k):
		if ((b % (-n)) == -1):
			return False
		else:
			b = SquareAndMultiply(b, 2, n)
	return True

#main	
n = 777777 
k = 4
m = 48611

count_fw = 0

print "\nStrong False Witnesses:"
for a in range(2, n-1):
	result = MillerRabin(a, n, k, m)
	#if MillerRabin returned "no" then a is a strong false witness
	if (result == False):
		print a
		count_fw = count_fw + 1
print "There are %d strong false witnesses for n = %d" % (count_fw, n)
