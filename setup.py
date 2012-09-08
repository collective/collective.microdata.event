from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='collective.microdata.event',
      version=version,
      description="Add microdata (scheda.org) support to Plone events",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        ],
      keywords='plone microdata schema.org html5 event',
      author='keul',
      author_email='luca@keul.it',
      url='http://plone.org/products/collective.microdata.event',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.microdata'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.microdata.core',
          'isodate',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
