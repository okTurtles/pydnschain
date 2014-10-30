from setuptools import setup, find_packages

import dnschain

setup(
    name="dnschain",
    version=dnschain.__version__,
    url='https://github.com/okturtles/pydnschain',
    license='MPL',
    description="A Python DNSChain library",
    author='Greg Slepak',
    author_email='hi@okturtles.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Environment :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography',
    ],
)
