import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plotpub",
    version="0.0.4",
    author="Sam Cameron",
    author_email="samuel.j.m.cameron@gmail.com",
    description="For publication quality plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samueljmcameron/plotpub",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
