# {octicon}`telescope;1em;sd-text-secondary` `HOW TO INSTALL PYTHON 3.10 ON UBUNTU 20.04 LTS`

There are two methods you can use to install *Python 3.10* on
`Ubuntu 20.04 LTS`. The first method is install from the **deadsnakes PPA**.
The second method of installation is to manually build from **source code**.
This also works on `Ubuntu 18.04 LTS` or later.

Before starting the installation, make sure your system is up-to-date and the
required packages are installed, type in the terminal:

```shell
sudo apt update && sudo apt upgrade -y
```

## INSTALL `PYTHON 3.10 FROM THE DEADSNAKES PPA`

Make sure you ran the previous command to upgrade the system.

The first option to install *Python 3.10* on `Ubuntu 20.04 LTS` is to install
using the custom repository
[deadsnakes PPA {octicon}`link-external;0.8em`][deadsnake]. A big thanks to
[Anthony Sottile {octicon}`link-external;0.8em`][asottile]
who is the lead developer of this repository, you can also see Open Source
*Python* Software live programming with
[anthonywritescode {octicon}`link-external;0.8em`][anthonywritescode] on
Twitch.

This allows you to easily and quickly install *Python* on Ubuntu and receive
continuous updates, bug fixes, and security updates.

First step is make sure to install the required dependency for adding custom
PPA repository, type in the terminal:

```shell
sudo apt install software-properties-common -y
```

Then proceed and add the **deadsnakes PPA** to the APT package manager sources
list, type in the terminal:

```shell
sudo add-apt-repository ppa:deadsnakes/ppa
```

After adding the repository to your system, now you can install it as usual by
typing in the terminal:

```shell
sudo apt install python3.10
```

It's everything installed now, you can enjoy the new version of *Python* on
your system and create amazing code.

You can verify the installation by checking the installed version by typing in
terminal:

```shell
python3.10 --version
```

## BUILD `PYTHON 3.10 FROM THE SOURCE CODE`

Make sure you ran the previous command to upgrade the system.

The second option to install *Python 3.10* on `Ubuntu 20.04 LTS` is to build it
from source code. By installing this way you will not be able to receive
further updates, bug fixes and security updates as was the case with
[deadsnakes PPA](#install-python-310-from-the-deadsnakes-ppa) installation, but
you will be sure you have the latest *Python* version.

The first step to build *Python 3.10* from source is to install the required
dependencies by typing in the terminal:

```shell
sudo apt update
sudo apt install \
    build-essential \
    libbz2-dev \
    libffi-dev \
    libgdbm-dev \
    libreadline-dev \
    libncurses5-dev \
    libnss3-dev \
    libssl-dev \
    libsqlite3-dev \
    wget \
    zlib1g-dev
```

Now you can check the latest release version of *Python* from
[Official Release {octicon}`link-external;0.8em`][pythonsource] page, copy the
link to use it for download with `wget` in the terminal.

Create a temporary folder in your home directory where you save the tarball of
the selected *Python* version, go in to the folder then download it using
`wget` by typing in the terminal:

```shell
mkdir ~/tmp && cd ~/tmp
wget https://www.python.org/ftp/python/3.10.4/Python-3.10.4.tgz
```

When the file is downloaded, unpack it by typing in a terminal:

```shell
tar -xf Python-3.10.4.tgz
```

After extracting the directory where the *Python* `source code` is located,
navigate to it and run configuration scripts to check the required
dependencies. The `--enable-optimizations` flag optimizes a binary by running
multiple tests.

```shell
cd Python-3.10.4/
./configure --enable-optimizations
```

Now you can check the number of cores on your system with the `nproc` command
to control how fast you want to initiate the build process.

Now all that's left to do is initiate the *Python* build process using the
maximum number of cores on your system by typing in terminal:

```shell
make -j $(nproc)
```

If you don't want to use the maximum number of cores just type `nproc` in the
terminal to find out the number of cores available on your system and enter the
value you want, for example `make -j 4`. In my case, I have 8 cores on my
system.

After the build process is complete, now you can install *Python* by typing in
terminal:

```shell
sudo make altinstall
```

To keep the default *Python* binary path in `/usr/bin/python` we used
`altinstall` options instead of `install`.

That is it. Now you can verify the installation by checking the installed
version by typing in the terminal:

```shell
python3.10 --version
```

Now you can install *Python* modules using Python Package Manager, you need to
have **PIP** installed on your system by typing in the terminal:

```shell
sudo apt install python3-pip
```

Then finally install a *Python* package:

```shell
pip install mdsanima-dev
```

I hope it will be useful to you.

[deadsnake]: https://github.com/deadsnakes/
[asottile]: https://github.com/asottile
[anthonywritescode]: https://www.twitch.tv/anthonywritescode
[pythonsource]: https://www.python.org/downloads/source/
