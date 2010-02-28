from distutils.core import setup, Extension

setup(name="entropy",
	version="0.0.1",
	description="Shannon entropy calculations for Python",
	author="Jesse Kempf",
	author_email="jessekempf@gmail.com",
	url="http://py-entropy.googlecode.com",
	packages = ['entropy'],
	ext_package = 'entropy',
	ext_modules = [Extension('_entropy', sources = ['entropy/_entropy.c'])]
)
