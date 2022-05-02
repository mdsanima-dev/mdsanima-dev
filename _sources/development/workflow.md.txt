# {octicon}`workflow;1em;sd-text-secondary` `WORKFLOW`

Instruction steps how to implement the release version and documentation site.

## CODING `PYTHON PACKAGE`

For [Python {octicon}`link-external;0.8em`][python] coding we're using
[Visual Studio Code {octicon}`link-external;0.8em`][vscode] and we love this
editor so much. Editor configuration setup is defined in `.editorconfig` and
`pyproject.toml` file, we use `black` and `isort` configuration defined in this
file.

Before starting writing code make sure to create **isolated environment** in
your local system typing `virtualenv .venv` and activating
`source .venv/bin/activate` then install requirements dependencies typing
`pip install -r docs/requirements-dev.txt` in the terminal.

### ADD `NEW MODULE`

Write a new module to an existing package. Use the
[black {octicon}`link-external;0.8em`][black] code formatter. We always try to
write *Python* code with limit all lines to a **maximum of 79 characters**. In
addition, we try to keep the documentation and the `.md` markdown files
according to this specification, not to exceed this limit as well. In some
cases, unfortunately, this cannot be avoided, such as pasting long links.

```{important}
Please check the official
[PEP 8 - Style Guide for Python Code {octicon}`link-external;0.8em`][pep]
specification on section maximum line length.
```

### ADD `DOCUMENTATION`

After writing the new module, write documentation in the `.py` file and in the
`docs` folder, add the appropriate `.md` files along with the **Sphinx**
directives for generate documentation site.

### BUILD `PACKAGE`

We just need to create an installable *Python* package, type in to terminal:

```shell
python3 setup.py sdist bdist_wheel
```

The package build creates new directories where the installation files are
located the `build` and `dist` directories. Then install the package, type in
the terminal:

```shell
pip install --force-reinstall dist/mdsanima_dev-0.1.1-py3-none-any.whl
```

In this case I used the `--force-reinstall` option because I had an earlier
version of this package already installed.

Now you're ready to [Build Documentation](#build-documentation) site localy
and upload your distributions to [PyPI](#send-to-pypi) using `Twine`.

```{tip}
If you have trouble, please check
[Packaging Python Projects {octicon}`link-external;0.8em`][pack] tutorial and
[Packaging and Distributing Projects {octicon}`link-external;0.8em`][dist]
guides on official *Python* site.
```

## BUILD `DOCUMENTATION`

Documentation are created automatically using
[Sphinx {octicon}`link-external;0.8em`][sphinx] based on
[Python {octicon}`link-external;0.8em`][python] files and the information they
contain written in comments.

```{warning}
This options build documentaiton localy only for testing. Directory
`build/dirhtml` is not pushing on this repository. We're using *GitHub Action*
for build documentation deployments.
```

The first thing you need to do is [Add New Module](#add-new-module) along
with the documentation. Then install it using the [wheel](#build-package)
option and finally build the documentation typing in the terminal:

```shell
python3 setup.py build_sphinx
```

You can also use the `easy install` options typing
`python3 setup.py install build_sphinx` in the terminal, but this is not
recommended.

The documentation build creates in `build/dirhtml` directory, check the
`docs/conf.py` file for the configuration settings.

The documentation build HTML pages with a single directory per document. Makes
for prettier URLs no `.html` in documentation pages address.

To see the documentation site in your local environment, just enter the command
in the terminal:

```shell
python3.7 -m http.server 8080 --directory build/dirhtml/
```

To use the `--directory` option you must use *Python 3.7* or later, but if you
don't have one, you can just go to the above-mentioned directory and type
`python3 -m http.server 8080` in the terminal. If you want to listen to a
specific interface use the `--bind 127.0.0.1` options.

Now just go to your browser and enter the
[localhost:8080](http://localhost:8080/) address.

## AUTOMATE `RELEASE`

Automate versioning and CHANGELOG generation, with
[Semantic Versioning {octicon}`link-external;0.8em`][semver] and
[Conventional Commits {octicon}`link-external;0.8em`][convcommits].
Generate changelogs and release notes from a project's commit messages and
metadata.

Added a `standard-version` npm package to automatically create `CHANGELOG.md`
files and tracking version. This option allow to generate automatically
changelog file for the project and tracking version on the *Python* package
based on commit messages.

```{important}
Please check the [Commit Guide {octicon}`link-external;0.8em`][convcommits]
site for proper commit message to generate CHANGELOG file.
```

For some reason that features are only for the development mode not allow
and access for the *Python* package.

Now in `package.json` file on section `standard-version` we're configure to
skip commit and tag, only bump version and changelog are active because when
generate changelog typing in the terminal `standard-version release-test`
labels are broken and we're manually fixing it.

Make release version and changelog, type in the terminal:

```shell
standard-version release
```

Command above for create release run script defined in `package.json` file on
script section `standard-version --commit-all --sign` which means bumping
version, adding changes in changelog, commiting all files and adding tag with
[Signing Commits {octicon}`link-external;0.8em`][gpg] using GPG keys.

For checking if everything is ok, type in the terminal:

```shell
standard-version release-test
```

Command above for checking run script defined in `package.json` file on script
section `standard-version --dry-run` which means only printing in the terminal,
no bumping version, not adding changes in changelog and no commit and tag.
This option is only for checking if everything is ok and we recommend using
this option first.

Also you can checking if everything is ok, type in the terminal:

```shell
standard-version --skip.commit --skip.tag
```

After run this command you will create a new version in the `package.json`
file, bumping version in `__init __.py` and automatically create `CHANGELOG.md`
based on commit messages.

Now you just need to execute this command in the terminal:

```shell
standard-version --skip.bump --skip.changelog --commit-all --sign
```

After executing this command all changed files will be committed with the
current version and new tag will be created. Commiting `package.json`,
`__init__.py`, `CHANGELOG.md` and other file with
[Signed Commits {octicon}`link-external;0.8em`][gpg] approval with GPG keys.

## SEND `TO PYPI`

We're almost done. If all steps is done, finally you can uploading your project
to [PyPI {octicon}`link-external;0.8em`][pypi].

When you ran the command to create your distribution, a new directory `dist`
was created under your project's root directory. That's where you'll find your
distribution files to upload.

Firs you should check the build are valid, type in the terminal:

```shell
twine check dist/*
```

Before releasing on main PyPI repo, you might prefer training with the
[TestPyPI {octicon}`link-external;0.8em`](https://test.pypi.org) which is
cleaned on a semi regular basis.

Send to `TestPyPI` using `Twine`, type in the terminal:

```shell
twine upload --repository pypi-test dist/*
```

Then go to [test.pypi.org {octicon}`link-external;0.8em`][pypitest] site and
check the package, if everything is ok, install it using `TestPyPI` with `pip`.
You can tell `pip` to download packages from `TestPyPI` instead of `PyPI` by
specifying the `--index-url` flag, type in the terminal:

```shell
python3 -m pip install --index-url https://test.pypi.org/simple/ mdsanima-dev
```

Finally we can send our package to
[pypi.org {octicon}`link-external;0.8em`](https://pypi.org/) main site.

Send to `PyPI` using `Twine`, type in the terminal:

```shell
twine upload dist/*
```

```{tip}
If you have trouble, please check
[Using TestPyPI {octicon}`link-external;0.8em`][testpypi] guides and
[Uploading your Project to PyPI {octicon}`link-external;0.8em`][sendpypi]
guides on official *Python* site.
```

[python]: https://www.python.org/
[vscode]: https://code.visualstudio.com/
[black]: https://github.com/psf/black
[pep]: https://peps.python.org/pep-0008/#maximum-line-length
[pack]: https://packaging.python.org/en/latest/tutorials/packaging-projects/
[dist]: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
[sphinx]: https://www.sphinx-doc.org/
[semver]: https://semver.org/
[convcommits]: https://conventionalcommits.org
[gpg]: https://docs.github.com/en/github-ae@latest/authentication/managing-commit-signature-verification/signing-commits
[testpypi]: https://packaging.python.org/en/latest/guides/using-testpypi/
[sendpypi]: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#uploading-your-project-to-pypi
[pypi]: https://pypi.org/project/mdsanima-dev
[pypitest]: https://test.pypi.org/project/mdsanima-dev
