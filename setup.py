from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="msnyd-helper-functions",
    version="1.2",
    author="M Snyder",
    author_email="msnyder97@gmail.com",
    description="Helps with splitting data",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="",
    url="https://github.com/msnyd/my-lambdata-package",
    keywords="data-split-test",
    packages=find_packages() # ["game_utils"]
)