from setuptools import setup, find_packages

setup(
    name="dnschain",
    version='0.1.0',
    url='https://github.com/okturtles/pydnschain',
    license='MPL',
    description=
    "A Python DNSChain library"
    author='Greg Slepak',
    author_email='hi@okturtles.com',
    packages=find_packages(),
    classifiers=[
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Environment :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Security :: Cryptography',
    ],
)
