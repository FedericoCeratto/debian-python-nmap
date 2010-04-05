
from distutils.core import setup, Extension

nmap = Extension('nmap',
                 sources = ['nmap/nmap.py'])

# Install : python setup.py install
# Register : python setup.py register

#  platform = 'Unix',
#  download_url = 'http://xael.org/norman/python/python-nmap/',


setup (
    name = 'python-nmap',
    version = '0.1.1',
    author = 'Alexandre Norman',
    author_email = 'norman@xael.org',
    license ='gpl-3.0.txt',
    keywords="nmap, portscanner, network, sysadmin",
    packages=['nmap'],
    url = 'http://xael.org/norman/python/python-nmap/',
    description = 'This is a python class to use nmap and access scan results from python',
    long_description=open('README.txt').read(),
)
