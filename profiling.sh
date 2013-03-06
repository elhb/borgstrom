# cProfile
python -m cProfile scripts/pyecm.py 123456789123456789123456789123456789123456789 > scripts/pyecm.py.cProfile

# do plop profiling
python -m plop.collector scripts/pyecm.py 123456789123456789123456789123456789123456789
cp /tmp/plop.out scripts/pyecm.py.plop
python -m plop.viewer --port=9876 --datadir=/tmp

# then add "@profile" to lines 76 430 536 and
# do the line by line profiling
kernprof.py --line-by-line scripts/pyecm.py 123456789123456789123456789123456789123456789
mv pyecm.py.lprof scripts/
python -m line_profiler scripts/pyecm.py.lprof > scripts/pyecm.py.lprof.output.txt

# comment "#" line 1483 and uncomment line 1484 then do memory profiling
python -m memory_profiler scripts/pyecm.py 123456789123456789123456789123456789 > scripts/pyecm.py.memory_profiler

mkdir profile_results -p
mv scripts/pyecm.py.* profile_results/
