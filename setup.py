import setuptools
setuptools.setup(
    author="shawngmy, yanjlee",
    author_email="shawngmy@gmail.com, yanjlee@163.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    install_requires=["httpx", "pynacl"],
    name="suiutils-py",
    packages=["suiutils_py"],
    url="https://github.com/satisfywithmylife/sui_python_sdk",
    python_requires=">=3.7",
    version="1.0.8",
)
