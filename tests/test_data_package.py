#!/usr/bin/python3

# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Testing loading package data from ``package.json`` file and printing output.

:usage: ``./test_package_data.py``
"""


import json


def test_package_data():
    with open("../package.json") as dt:
        package_data = json.load(dt)

    name = package_data["name"]
    version = package_data["version"]
    author_name = package_data["author"]["name"]
    author_email = package_data["author"]["email"]
    description = package_data["description"]
    homepage = package_data["homepage"]
    project_urls = package_data["project_urls"]
    classifiers = package_data["classifiers"]
    license = package_data["license"]
    extras_require = package_data["extra_require"]
    keywords = package_data["keywords"]

    print(name)
    print(version)
    print(author_name)
    print(author_email)
    print(description)
    print(homepage)
    print(project_urls)
    print(classifiers)
    print(license)
    print(extras_require)
    print(keywords)


def main():
    test_package_data()


if __name__ == "__main__":
    raise SystemExit(main())
