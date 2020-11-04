import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="davil",
    version="0.0.1",
    author="David Kolb",
    author_email="david_kolb@t-online.de",
    description="Various Utils for no specific purpose.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Treiblesschorle/davil",
    packages=setuptools.find_packages(where='src'),
    package_dir={
        '': 'src',
    },
    install_requires=[
        'numpy',
        'scipy',
        'sty',
        'matplotlib'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
