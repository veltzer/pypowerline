import setuptools


def get_readme():
    with open("README.rst") as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pypowerline",
    version="0.0.32",
    packages=[
        "pypowerline",
    ],
    # from here all is optional
    description="sane powerline",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        "powerline",
        "powerline-shell",
        "shell",
    ],
    url="https://veltzer.github.io/pypowerline",
    download_url="https://github.com/veltzer/pypowerline",
    license="MIT",
    platforms=[
        "python3",
    ],
    install_requires=[
        "pytconf",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.12",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"console_scripts": [
        "pypowerline=pypowerline.main:main",
    ]},
)
