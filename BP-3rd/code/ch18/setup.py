from setuptools import setup, Extension
setup(name="Hello",
      version="0.1",
      description="A simple example",
      author="Stephen CUI",
      author_email='cuixuanstephen@gmail.com',
      py_modules=['hello'])

setup(name='palindrome',
      version='.1',
      ext_modules=[
          Extension('palindrome', ['palindrome2.c'])
      ])
