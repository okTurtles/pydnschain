from setuptools import setup, find_packages

import dnschain

setup(
    name="dnschain",
    version=dnschain.__version__,
    url='https://github.com/okturtles/pydnschain',
    license='MPL 2.0',
    description="Python library to perform DNSChain lookups",
    author='okTurtles Foundation',
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
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    ],
)
