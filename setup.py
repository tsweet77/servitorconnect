from setuptools import setup, find_packages

setup(
    name="servitorconnect",
    version="1.0.0",
    author="AnthroHeart (Thomas Sweet)",
    author_email="healing@intentionrepeater.com",
    description="A tool to repeat intentions hourly from a file or direct input.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tsweet77/servitorconnect",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "servitorconnect=servitorconnect.cli:main",
        ],
    },
)
