"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###
def linear_search(mylist, key):
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1
def binary_search(mylist, key):
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  if right >= left:
    mid = (left+right)//2
    if mylist[mid] == key:
      return mid
    elif mylist[mid] > key:
      return _binary_search(mylist, key, left, mid -1)
    else:
      return _binary_search(mylist, key, mid + 1, right)     
  else:
    return -1

def time_search(search_fn, mylist, key):
	start = time.time() * 1000
	search_fn(mylist,key)
	ms = time.time()* 1000
	return(ms-start)
def test_linear_search():
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1
def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	assert binary_search([1,2,3,4,5], 0) == -1
	assert binary_search([1,2,3,4,5], 3) == 2
def makeList(n1,n2):
	if n1 == n2:
		return n1
	else:
		res = []
		while n1<=n2:
			res.append(n1)
			n1+=1
		return res

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	mylist0 = makeList(0,sizes[0])
	mylist1 = makeList(0,sizes[1])
	mylist3 = makeList(0,sizes[2])
	mylistmax = makeList(0,sizes[3])


	n=["Binary 1e1:",time_search(binary_search,mylist0,-1),"Linear Search 1e1:", time_search(linear_search,mylist0,-1),"Binary search 1e2", time_search(binary_search,mylist1,-1),"Linear search 1e2", time_search(linear_search,mylist1,-1)]
	n.append("Binary search 1e3:")
	n.append(time_search(binary_search,mylist3,-1))
	n.append("Linear search 1e3:")
	n.append(time_search(binary_search,mylist3,-1))
	n.append("Binary search 1e7:")
	n.append(time_search(binary_search,mylistmax,-1))
	n.append("Linear search 1e7:")
	n.append(time_search(linear_search,mylistmax,-1))
	return n


def print_results(results):
	print(tabulate.tabulate(results, headers=['n', 'linear', 'binary'], floatfmt=".3f", tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

print(compare_search(sizes=[10,100,1000,10000000]))