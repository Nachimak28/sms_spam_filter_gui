# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

data_files = [('spam_sms_identifier', ['spam_sms_identifier/logo_spamFilter.png']),]

setup(
    name="SPAM SMS ID",
    version="1.0.0",
    description="Detecting SPAM SMS based on text",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Nachimak28/sms_spam_filter_gui",
    author="Nachiket Makwana",
    author_email="nachimak28@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    data_files = data_files,
    packages=["spam_sms_identifier"],
    include_package_data=True,
    install_requires=[
        "dearpygui==1.3.1",
        "nltk==3.6.7",
        "pandas==1.3.5"
    ],
    entry_points={"console_scripts": ["sms_spam_filter_gui=spam_sms_identifier.app:main"]},
)