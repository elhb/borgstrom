from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='borgstrom',
      version=version,
      description="For the pyhton course @ scilifelab.",
      long_description="""\
NA""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='NA',
      author='erik',
      author_email='erik.borgstrom@scilifelab.se',
      url='NA',
      license='NA',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      scripts = ['scripts/getting_data.py'],
      include_package_data=True,
      zip_safe=True,
      install_requires=['untangle'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
