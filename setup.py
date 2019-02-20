import setuptools

with open("README.md", "r") as 自述文件:
    长描述 = 自述文件.read()

setuptools.setup(
    name="test-package-name",
    version="0.0.4",
    author="小名",
    author_email="author@example.com",
    description="描述",
    long_description=长描述,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)