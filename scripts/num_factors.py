#

def main():
	indata = check_indata()

	lowest_number = 2
	highest_number = 1000#500000

	if indata.mode == 's' or 'all':
		timer = Timer(verbose=True)
		counter = Counter()
		with timer:
			for i in xrange(lowest_number,highest_number+1): counter.add(factorize(i))
			print 'Result from single process:      ', counter, '\t',
	if indata.mode == 'm' or 'all':
		timer = Timer(verbose=True)
		counter = Counter()
		import multiprocessing
		with timer:
			WorkerPool = multiprocessing.Pool(2)
			results = WorkerPool.imap_unordered(factorize,xrange(lowest_number,highest_number+1),chunksize=10)
			for factors in results: counter.add(factors)
			print 'Result from multiprocessing.Pool:', counter, '\t',
	if indata.mode == 'p' or 'all':
		timer = Timer(verbose=True)
		counter = Counter()
		with timer:
			from IPython.parallel import Client
			cli = Client()
			dview = cli[:]
#			print zip(cli.ids,dview.apply_sync(get_pid))
	
			@dview.parallel(block=True)
			def factorizeIPP(n): # function from Valentin
				if n < 2:
					return []
				factors = []
				p = 2
				while True:
					if n == 1:
						return factors
					r = n % p
					if r == 0:
						factors.append(p)
						n = n / p
					elif p * p >= n:
						factors.append(n)
						return factors
					elif p > 2:
						p += 2
					else:
						p += 1
	
			for factors in factorizeIPP.map(xrange(lowest_number,highest_number+1)):
				counter.add(factors)
			print 'Result from IPython.parallel:    ', counter, '\t',

def get_pid(): # just for testing
    import os
    return os.getpid()

def check_indata():
	import argparse
	argparser = argparse.ArgumentParser(description='Script for counting uniqe factors.',formatter_class=argparse.RawTextHelpFormatter,)
	argparser.add_argument('-mode',dest='mode',metavar='X',type=str,required=True,default='s',help='s, m, p or all (default is s).')
	indata = argparser.parse_args()
	if indata.mode not in ['s','m','p', 'all']: raise ValueError, ' mode has to be s m, p or all!!'
	return indata

def factorize(n): # function from Valentin
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1

class Counter(object):
	
    def __init__(self):
        self.counter = {}

    def add(self,factors):
	factors.sort()
	uniq = f7(factors)
	#print product(factors), factors, str(len(uniq))
	try: self.counter[len(uniq)] += 1
	except KeyError: self.counter[len(uniq)] = 1
	
    def __str__(self):
	return str(self.counter)

import time
class Timer(object): # stole the timer from http://www.huyng.com/posts/python-performance-analysis/ thanks to Huy!!
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs

def product(factors):
	product=1
	for i in factors:
		product = product * i
	return product
    
def f7(seq): # stolen from http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order thanks to Markus Jarderot!
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

if __name__ == "__main__":
    main()
