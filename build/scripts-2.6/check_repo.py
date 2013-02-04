#!/Users/erikborgstrom/.virtualenvs/py2.7/bin/python

from borgstrom.session3 import *

indata = check_indata()

with repo_dir(indata.path):
    lastname = os.path.basename(os.getcwd())
    repo = CourseRepo(lastname)
    print repo.check()


