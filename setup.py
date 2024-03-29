import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

print(setuptools.find_packages())
setuptools.setup(
    name="plotpub",
    version="0.0.8",
    author="Sam Cameron",
    author_email="samuel.j.m.cameron@gmail.com",
    description="For publication quality plots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samueljmcameron/plotpub",
    packages=["plotpub"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['matplotlib']
)
