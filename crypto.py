'''
purpose
	encrypt P using Caesar cipher with key K
preconditions
	P: string of A..Z
	K in 0..25
'''
def caesar_encrypt(P,K):
	C = ''
	for i in P:
		C += toLet((toNum(i) + K)%26)
	
	return C

'''
purpose
	decrypt C using Caesar cipher with key K
preconditions
	C: string of A..Z
	K in 0..25
'''
def caesar_decrypt(C,K):
	P = ''
	for i in C:
		P += toLet((toNum(i) - K)%26)
		
	return P

# --------------------------------------------------------------

'''
purpose
	encrypt P using substitution cipher with key K
preconditions
	P: string of A..Z
	K: permutation of A..Z
'''
def substitution_encrypt(P,K):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	C = ''
	for i in P:
		ind = alphabet.index(i)
		C += K[ind]
	return C

'''
purpose
	decrypt C using substitution cipher with key K
preconditions
	C: string of A..Z
	K: permutation of A..Z
'''
def substitution_decrypt(C,K):
	P = ''
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for i in C:
		ind = K.index(i)
		P += alphabet[ind]
	return P

# --------------------------------------------------------------

'''
purpose
	encrypt P using Vernam cipher with key K
	if len(P) > len(K) then repeat the key as needed
preconditions
	P: string of A..Z
	K: non-empty list of int in 0..25
'''
def vernam_encrypt(P,K):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	C = ''

	for i in range(0, len(P)):

		ind = alphabet.index(P[i])

		final = ( (ind + K[i%len(K)]) % 26 )
		C +=  alphabet[final]
	return C

'''
purpose
	decrypt C using Vernam cipher with key K
	if len(C) > len(K) then repeat the key as needed
preconditions
	C: string of A..Z
	K: non-empty list of int in 0..25
'''
def vernam_decrypt(C,N):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	P = ''
	for i in range(0, len(C)):

		ind = alphabet.index(C[i])

		final = ( (ind - N[i%len(N)]) % 26 )
		P +=  alphabet[final]
	return P

# --------------------------------------------------------------

'''
purpose
	encrypt P using book cipher with key K
	if len(P) > len(K) then repeat the key as needed
preconditions
	P: string of A..Z
	K: non-empty string of A..Z
'''
def book_encrypt(P,K):
	C = ''
	for i in range(0, len(P)):
		a = toNum(P[i])
		b = toNum(K[i%len(K)])
		c = a + b
		if c > 25:
			c -= 26
		C += toLet(c)
	return C

'''
purpose
	decrypt C using book cipher with key K
	if len(C) > len(K) then repeat the key as needed
preconditions
	C: string of A..Z
	K: non-empty string of A..Z
'''
def book_decrypt(C,K):
	P = ''
	for i in range(0, len(C)):
		a = toNum(C[i])
		b = toNum(K[i%len(K)])
		c = a - b
		if c < 0:
			c += 26
		P += toLet(c)
	return P

# --------------------------------------------------------------

'''
purpose
	encrypt P using columnar transposition cipher with key K
preconditions
	P: string of A..Z
	K > 0
'''
def columnar_encrypt(P,K):
	i = 0
	j = 0
	C = ''
	while len(C) < len(P):
		C += P[i]
		i += K
		if i >= len(P):
			i = j + 1
			j += 1
	
	return C

'''
purpose
	decrypt C using columnar transposition cipher with key K
preconditions
	P: string of A..Z
	K > 0
'''
def columnar_decrypt(C,K):
	i = 0
	j = 0
	r = len(C)%K
	P = ''
	while len(P) < len(C):
		P += C[i]
		i += len(C)/K
		if r > 0:
			r -= 1
			i += 1
		
		if i >= len(C):
			i = j + 1
			j += 1
			r = len(C)%K
	
	return P
			

# --------------------------------------------------------------

'''
purpose
	encrypt P using RSA encryption with key K e,n
preconditions
	P: list of positive integers
	e,n selected according to the RSA requirements
'''
def rsa_encrypt(P,e,n):
	C = []
	for i in P:
		C.append((i**e)%n)
	return C

'''
purpose
	decrypt C using RSA encryption with key K d,n
preconditions
	C: list of positive integers
	d,n selected according to the RSA requirements
'''
def rsa_decrypt(C,d,N):
	P = []
	for i in C:
		P.append((i**d)%N)
	return P

# --------------------------------------------------------------

'''
purpose
	return a list L where
		len(L) = 26
		L[i] contains the number of occurrences in S of the ith
			letter in the alphabet
preconditions
	S is a string of A..Z
'''
def count_letters(S):
	
	L = [0]*26
	for a in S:
		L[toNum(a)] += 1
	return L
	

'''
purpose
	convert a letter in A-Z to the corresponding number in 0-25
	or vice versa
preconditions
	a is a letter in A-Z
	i is an integer in 0-25
'''
def toNum(a):
	letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	return letters.index(a)
	
def toLet(i):
	letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	return letters[i]

# --------------------------------------------------------------

'''
purpose
	return a dictionary D where
		D.keys contains all of the digrams in S
		D[d] is the number of occurrences of digram d in S
preconditions
	S is a string of A..Z
'''
def count_digrams(S):
	digrams = dict()

	for s in range(0,len(S)-1):
		digram = ''
		digram = S[s]
		digram += (S[s+1])
		digrams[digram] = digrams.get(digram, 0) + 1
	return digrams
	
	
	
#TEST CODE REMOVE THIS BEFORE SUBMITTING
#IF THIS IS HERE AND YOU ARE MARKING THE ASSIGNMENT, YOU CAN DELETE EVERYTHING BELOW THIS LINE

def transposed_caesar_encrypt(P,K):
	C1 = columnar_encrypt(P,K)
	return caesar_encrypt(C1,K)

def transposed_caesar_decrypt(C,K):
	P1 = caesar_decrypt(C,K)
	return columnar_decrypt(P1,K)
	
	
P = 'VCMNNOTPRETENDTOZEELVAPMRTVMLMXOUTTHECOLOURS'
K = 'MXCDEZGHVJKLANOPQRSTUIWBYF'
Q = 'EZQBMGWCZTIABVIUMQVZMDMZAM'
for a in range(0,25):
	print(caesar_decrypt(Q,a))



