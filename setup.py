import setuptools
setuptools.setup(
    author="shawngmy, yanjlee",
    author_email="shawngmy@gmail.com, yanjlee@163.com",
    include_package_data=True,
    install_requires=["httpx", "pynacl", "inflect", "pick","path","GuDory2","configparser","pypandoc","python-slugify","vb-console"],
    name="suiutils-py",
    long_description=open(r'README.md', encoding='utf-8').read(),  # 读取readme自述文件
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),     # 自动列出项目下的包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",   # 开源许可证
        "Operating System :: OS Independent",      # 这里的定义是系统无关（全平台兼容），如果你的包只能在部分特定系统上运行，需要修改。
    ],
    url="https://github.com/satisfywithmylife/sui_python_sdk",
    python_requires=">=3.7",
    version="1.0.9",
)
