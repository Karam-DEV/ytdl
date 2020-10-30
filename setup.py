import setuptools

LONG_DESCRIPTION = "library to extract youtube videos data"

# Get the version from ytdl/version.py without importing the package
exec(compile(open('ytdl/version.py').read(),'ytdl/version.py', 'exec'))

REQUIREMENTS = open("requirements.txt").read().split("\n")

setuptools.setup(
    name="ytdl",
    version=__version__,
    author="Karam Alhamada",
    author_email="krmhmade1@gmail.com",
    description="Youtube videos data extractor",
    long_description=LONG_DESCRIPTION,
    packages=['ytdl'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    python_requires='>=3.6',
)