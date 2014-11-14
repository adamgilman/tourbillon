from codecs import open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='tourbillon',
      version='0.0.1',
      description="A pure python whirlwind data streaming service built on redis which ingests data and can replay it at any desired speed",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Adam Gilman',
      author_email='me@adamgilman.com',
      url='https://github.com/adamgilman/tourbillon',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          ''
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      """
      )