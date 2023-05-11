# mdsanima-dev

[![license-mdsanima][badge-01]][link-01]
[![latest-version-on-pypi][badge-02]][link-02]
[![github-top-language][badge-03]][link-01]
[![pypi-python-version][badge-04]][link-02]
[![code-style-black][badge-05]][link-03]

[![pype-total-downloads][badge-pe]][link-04]
[![github-repo-stars][badge-06]][link-01]
[![github-open-issues][badge-07]][link-05]
[![github-closed-issues][badge-08]][link-06]
[![github-deployments][badge-09]][link-07]
[![github-pages-documentation][badge-10]][link-08]

_Python_ package [mdsanima-dev][link-02] is for colorizing, adding emoji and making table on console shell print output.
You can find here _Python_ modules that's make coding easier and cooler, includes several useful modules that we're use
in various projects. In the future we're add more cool function on this package.

Docomentation available at [GitHub Pages][link-08], be sure to check it.

## Installation `Options`

Instructions how to install the _Python_ package [mdsanima-dev][link-02] on your system.

<!-- start help-installation -->

Options [PyPI](#using-pypi) allows you to install the package **globally** on your system. If you want to install the
package in an **isolated environment** on your system use the [virtualenv](#using-virtualenv) options.

<!-- end help-installation -->

### Using `PyPI`

<!-- start help-using-pypi -->

Install latest version:

```shell
python3 -m pip install mdsanima-dev
```

Install specific version:

```shell
python3 -m pip install mdsanima-dev==0.2.0
```

Upgrade package to latest version:

```shell
python3 -m pip install --upgrade mdsanima-dev
```

Reinstall package to latest version:

```shell
python3 -m pip install --force-reinstall msdsanima-dev
```

Uninstall package:

```shell
python3 -m pip uninstall mdsanima-dev
```

<!-- end help-using-pypi -->

### Using `virtualenv`

<!-- start help-on-virtualenv -->

Clone repository with all number of commits history using HTTPS:

```shell
git clone https://github.com/mdsanima-dev/mdsanima-dev.git
```

Clone repository with the specified number of commits history using SSH:

```shell
git clone --depth=1 git@github.com:mdsanima-dev/mdsanima-dev.git
```

Then go to the repository directory:

```shell
cd mdsanima-dev
```

Create isolated environment with specific package version then activate and install requirements, type in terminal:

```shell
virtualenv --setuptools 67.7.2 --wheel 0.40.0 --pip 23.1.2 .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -r requirements-doc.txt
```

Install build tools for creating distribution, then build package from source, type in terminal:

```shell
pip install --upgrade build
python -m build
```

Finnaly install the package in virtual environment, type in the terminal:

```shell
pip install --force-reinstall dist/mdsanima_dev-0.2.0-py3-none-any.whl
```

In this case I used the `--force-reinstall` option because I had an earlier version of this package already installed.

Also you can build Sphinx documentation, type in terminal:

```shell
python setup.py build_sphinx
cd build/dirhtml
python -m http.server 8080
```

Now open [localhost](http://localhost:8080) to see the documentation.

Deactivate virtual environment, type in the terminal:

```shell
deactivate
```

<!-- end help-on-virtualenv -->

## Develempent

Instruction for the _Python_ package development. Please check the [documentation][link-08] site for more information.

## Showcase

![mdsanima-dev-python-show](docs/_images/gif/mdsanima_dev_python_show.gif)

## Follow Me

These are my social media account, be sure to check it. Thanks!

[![github-followers-mdsanima][badge-11]][link-10]
[![twitter-follow-toudajew][badge-12]][link-12]
[![twitter-follow-str9led][badge-13]][link-13]
[![twitter-follow-mdsanima][badge-14]][link-14]

[![subreddit-subscribers-mdsanima][badge-15]][link-15]
[![youtube-subscribers-mdsanima][badge-16]][link-16]
[![youtube-views-mdsanima][badge-17]][link-16]
[![twitch-status-mdsanima][badge-18]][link-17]
[![discord-chat-mdsanima][badge-19]][link-09]

## License

Python package [mdsanima-dev][link-02] developed by [Marcin Różewski][link-10] is released under the terms of
[MIT License][link-11]

[badge-pe]: https://static.pepy.tech/personalized-badge/mdsanima-dev?period=total&units=none&left_color=grey&right_color=yellowgreen&left_text=downloads
[badge-01]: https://img.shields.io/github/license/mdsanima-dev/mdsanima-dev?style=flat
[badge-02]: https://img.shields.io/pypi/v/mdsanima-dev?style=flat&logo=pypi&logoColor=lightgray
[badge-03]: https://img.shields.io/github/languages/top/mdsanima-dev/mdsanima-dev?style=flat&logo=python&logoColor=lightgray
[badge-04]: https://img.shields.io/pypi/pyversions/mdsanima-dev?style=flat&logo=python&logoColor=lightgray
[badge-05]: https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=lightgray
[badge-06]: https://img.shields.io/github/stars/mdsanima-dev/mdsanima-dev?style=flat&logo=github
[badge-07]: https://img.shields.io/github/issues-raw/mdsanima-dev/mdsanima-dev?style=flat&logo=github
[badge-08]: https://img.shields.io/github/issues-closed-raw/mdsanima-dev/mdsanima-dev?style=flat&logo=github
[badge-09]: https://img.shields.io/github/deployments/mdsanima-dev/mdsanima-dev/github-pages?style=flat&logo=github
[badge-10]: https://img.shields.io/website?url=https%3A%2F%2Fmdsanima-dev.github.io%2Fmdsanima-dev%2F?style=flat&logo=github
[badge-11]: https://img.shields.io/github/followers/mdsanima?style=social
[badge-12]: https://img.shields.io/twitter/follow/toudajew?style=social
[badge-13]: https://img.shields.io/twitter/follow/str9led?style=social
[badge-14]: https://img.shields.io/twitter/follow/mdsanima?style=social
[badge-15]: https://img.shields.io/reddit/subreddit-subscribers/mdsanima?style=social
[badge-16]: https://img.shields.io/youtube/channel/subscribers/UCB5na2BRwrnwx00LCspbG5Q?style=social
[badge-17]: https://img.shields.io/youtube/channel/views/UCB5na2BRwrnwx00LCspbG5Q?style=social
[badge-18]: https://img.shields.io/twitch/status/mdsanima?style=social
[badge-19]: https://img.shields.io/discord/621477380359454742?style=social&logo=discord
[link-01]: https://github.com/mdsanima-dev/mdsanima-dev
[link-02]: https://pypi.org/project/mdsanima-dev
[link-03]: https://github.com/psf/black
[link-04]: https://pepy.tech/project/mdsanima-dev
[link-05]: https://github.com/mdsanima-dev/mdsanima-dev/issues?q=is%3Aopen+is%3Aissue
[link-06]: https://github.com/mdsanima-dev/mdsanima-dev/issues?q=is%3Aissue+is%3Aclosed
[link-07]: https://github.com/mdsanima-dev/mdsanima-dev/deployments/activity_log?environment=github-pages
[link-08]: https://mdsanima-dev.github.io/mdsanima-dev/
[link-09]: https://discord.gg/c3m7pTF
[link-10]: https://github.com/mdsanima
[link-11]: https://github.com/mdsanima-dev/mdsanima-dev/blob/master/LICENSE
[link-12]: https://twitter.com/intent/follow?toudajew&screen_name=toudajew
[link-13]: https://twitter.com/intent/follow?str9led&screen_name=str9led
[link-14]: https://twitter.com/intent/follow?mdsanima&screen_name=mdsanima
[link-15]: https://reddit.com/r/mdsanima/
[link-16]: https://youtube.com/mdsanima?sub_confirmation=1
[link-17]: https://twitch.tv/mdsanima/
