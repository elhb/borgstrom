# cProfile
python -m cProfile scripts/pyecm.py 100000000000000000000000000000000000000000000000000 > scripts/pyecm.py.cProfile

# then add "@profile" to lines 76 430 536 and run:
python -m plop.collector scripts/pyecm.py 100000000000000000000000000000000000000000000000000
cp /tmp/plop.out scripts/pyecm.py.plop
python -m plop.viewer --port=9876 --datadir=/tmp

# do the line by line profiling
kernprof.py --line-by-line scripts/pyecm.py 100000000000000000000000000000000000000000000000000
mv pyecm.py.lprof scripts/
python -m line_profiler scripts/pyecm.py.lprof > scripts/pyecm.py.lprof.output.txt

# do memory profiling
python -m memory_profiler scripts/pyecm.py 10000000000000000000000000000000000000 > scripts/pyecm.py.memory_profiler
