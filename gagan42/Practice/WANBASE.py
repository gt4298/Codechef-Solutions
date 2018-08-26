t=int(input())
for i in range(t):
	n, k = map(int, input().split())
	a = map(int, input().split())
	b = []
	d = {}
	for i in a:
		b.append((int(str(i), 8), 8))
		b.append((int(str(i), 16), 16))
		d[(int(str(i), 8), 8)] = i
		d[(int(str(i), 16), 16)] = i
 
	b.sort()
	print (d[b[k - 1]], b[k - 1][1] )
