import platform
import sys

import setuptools

with open("README.md") as f:
    long_description = f.read()

with open("./src/dns/__init__.py") as f:
    for line in f.readline():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            version = line.split(delim)[1]
            break
    else:
        print("Can't find version! Stop Here!")
        sys.exit(1)

package_data = {}

setuptools.setup(
    name="dns",
    version=version,
    author="Criss Wang",
    author_email="zhenlinw@cs.cmu.edu",
    description="A DNS simulation that runs on local machine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/criss-wang/DNS_in_Python",
    packages=setuptools.find_packages("src"),
    package_dir={"":"src"},
    package_data=package_data,
    python_requires=">=3.7",
    ext_modules=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
    ],
    
)