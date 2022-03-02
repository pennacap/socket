import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sockets-made-easy",
    version="0.0.1",
    author="tony-is-coding",
    description="A small and easy socket wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tony-is-coding/socket",
    project_urls={
        "Bug Tracker": "https://github.com/tony-is-coding/socket/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": ""},
    packages=setuptools.find_packages(where=""),
    python_requires=">=3.6",
)
