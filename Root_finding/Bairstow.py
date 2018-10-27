def quadroot(r,s):
	"""
	Finds the Quadratic Root of r and s.
	"""

	import math

	disc = r**2 + 4*s
	if disc > 0:
		r1 = (r + math.sqrt(disc))/2
		r2 = (r - math.sqrt(disc))/2
		i1 = 0
		i2 = 0
	else:
		r1 = r/2
		r2 = r1
		i1 = math.sqrt(abs(disc))/2
		i2 = -i1


def Baristow(a,nn,es,rr,ss,maxit):
	r = rr
	s = ss
	n = nn
	ier, esl, ea2 = 0,1,1
	iter = 0
	while !(n<3 or iter >= maxit):
		iter = 0
		while True:
			iter = iter + 1
			b[n] = a[n]
			b[n-1] = a[n-1] + r*b[n]
			c[n] = b[n]
			c[n-1] = b[n-1] + r*c[n]
			for i in [n-2,0,1]:
				b[i] = a[i] + r*b[i+1] + s*b[i+2]
				c[i] = b[i] + r*c[i+1] + s*c[i+2]
			det = c[2]*c[2] - c[3]*c[1]
			if det != 0:
				dr = (-b[1]*c[2] + b[0]*c[3])/det
				ds = (-b[0]*c[2] + b[1]*c[1])/det
				r = r+dr
				s = s+ds
				if r != 0:
					ea1 = abs(dr/r)*100
					ea2 = abs(ds/s)*100
				else:
					r = r+1
					s = s+1
					iter = 0
			if (ea1 <= es and ea2 <= es or iter >= maxit):
				break

		r1,i1,r2,i2 = quadroot(r,s)
		re[n] = r1
		im[n] = i1
		re[n-1] = r2
		im[n-1] = i2
		n = n-2
		for i in [0,n]:
			a[i] = b[i+2]
		if iter < maxit:
			if n==2:
				r = -a[1]/a[2]
				s = -a[0]/a[2]
				r1,i1,r2,i2 = quadroot(r,s)
				re[n] = r1
				im[n] = i1
				re[n-1] = r2
				im[n-1] = i2
			else:
				re[n] = -a[0]/a[1]
				im[n] = 0
		else:
			ier = 1

