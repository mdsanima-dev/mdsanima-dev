# WORKFLOW

Instruction steps how to implement the release version and documentation site.

## Add New Module

Write a new module to an existing package. Commit changes based on
`conventional-commits` messages.

## Add Documentation

Write `shpinx` documentation for this module in a `.py` file and in the
`docs/source` folder.

## Add Changelog

First run this command:

```shell
standard-version release-test
```

If everything is ok run this command:

```shell
standard-version --skip.commit --skip.tag
```

After run this command you will create a new version in the `package.json` file,
bump it in `__init __.py` and you will automatically create `CHANGELOG.md`
based on commit messages.

## Building Documentation

Then build the documentation by typing this command:

```shell
sudo python3 setup.py install build_sphinx
```

By executing this command you will create `html` documentation in `docs/html`.

## Commit Changes

Now you just need to execute this command:

```shell
standard-version --skip.bump --skip.changelog --commit-all --sign
```

After executing this command all documentation files and other changed files
will be committed and a new tag with the current version will be created.
Commit `package.json`,`__init__.py` and `CHANGELOG.md` with signed GPG keys.
Create tagging release and signed approval with GPG keys.

## Build Pacage

We’re almost done. We just need to put commands in to terminal and which will
create an installable Python Package from your `code` and send it to `PyPi`.

Build Setpu:

```shell
sudo python3 setup.py install
sudo python3.7 setup.py install
sudo python3.8 setup.py install
```

It created some new directories for us, such as `dist`, `build`
and `your_package.egg-info`.

Check the Build:

```shell
twine check dist/*
```

Send to Test PyPi:

```shell
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Go to [test.pypi.org](https://test.pypi.org) and check if everything is ok,
if yes, we can finally send our package to [PyPi](https://pypi.org/).

Finally Send To PyPi:

```shell
twine upload dist/*
```
