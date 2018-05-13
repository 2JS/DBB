import random
import time

def initialPrint():
	"""docstring for initialPrint"""
	print("""-- Digit Baseball --
-- by 2JS of Meta Studio --
-- This program is open source --

'When you answer me, please answer like (balls),(strikes). There must be no space or dot. For example, when answer is 'one ball one strike'\n1,1\nAnd for this vesion, you cannot correct your past answer, \nso please answer CORRECTLY'""")

def log(string):
	"""docstring for log"""
	print(str(n) + " : " + string)

def keyGen(n):
	"""docstring for keyGenerator"""
	standard = [1,2,3,4,5,6,7,8,9]
	key = ""
	n = int(n)
	for x in xrange(9, 9-n, -1) :
		rand = random.randrange(x)
		key = key + str(standard.pop(rand))
	return key

def keyGenInList(lst):
	"""docstring for keyGenInList"""
	return lst[random.randrange(len(lst))]

def compare(n, arg1, arg2):
	"""Compare : Check Strikes and Balls
	args are string"""
	
	a, b = set(arg1), set(arg2)
	Strikes = 0
	BallsAndStrikes = len(a & b)
	
	for x in xrange(n):
		if arg1[x] == arg2[x]:
			Strikes = Strikes + 1
	
	return BallsAndStrikes - Strikes, Strikes


def listGen(n):
    lst = [x for x in range(10**n)]
    lst2 = [x for x in range(10**n)]
    for element in lst :
        if (len(set(str(element))) < n) or (set(str(element)) & set("0")):
            lst2.remove(element)
    return lst2
	
def listFilt(n, lst, myask, ball, strike):
	lst2 = []

	for element in lst:
		if compare(n,str(element),str(myask)) == (int(ball), int(strike)) :
			lst2.append(element)
	return lst2