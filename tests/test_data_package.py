#!/usr/bin/python3

# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Testing loading data package from ``package.json`` file and printing output.

:usage: ``./test_data_package.py``
"""


import json


def test_data_package():
    with open("../package.json") as dt:
        data_package = json.load(dt)

    name = data_package["name"]
    version = data_package["version"]
    author = data_package["author"]["name"]
    author_email = data_package["author"]["email"]
    description = data_package["description"]
    url = data_package["homepage"]
    project_urls = data_package["project_urls"]
    classifiers = data_package["classifiers"]
    license = data_package["license"]
    extras_require = data_package["extra_require"]
    keywords = data_package["keywords"]

    print(name)
    print(version)
    print(author)
    print(author_email)
    print(description)
    print(url)
    print(project_urls)
    print(classifiers)
    print(license)
    print(extras_require)
    print(keywords)


def main():
    test_data_package()


if __name__ == "__main__":
    raise SystemExit(main())
