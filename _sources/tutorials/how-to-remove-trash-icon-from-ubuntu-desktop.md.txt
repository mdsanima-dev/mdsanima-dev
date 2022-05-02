# {octicon}`telescope;1em;sd-text-secondary` `HOW TO REMOVE THE TRASH ICON FROM UBUNTU DESKTOP`

By default, in `Ubuntu 18.04 LTS` and newer, the trash icon appears on the
desktop, but not everyone likes it.

In this tutorial, I will show you how to quickly remove the `trash icon` from
the Ubuntu desktop as well as from the `home folder` that shows up in newer
versions of the distribution.

## REMOVE `TRASH ICON FROM UBUNTU DESKTOP`

The quickest and easiest way to remove the trash icon from the desktop is to
type the command into the terminal.

If you want to remove the trash icon from the desktop on `Ubuntu 18.04 LTS`,
open a terminal and type this command:

```shell
gsettings set org.gnome.nautilus.desktop trash-icon-visible false
```

To remove the trash icon from the desktop on `Ubuntu 19.10` or leter, open a
terminal and type this command:

```shell
gsettings set org.gnome.shell.extensions.desktop-icons show-trash false
```

If you change your mind and would like to bring the trash icon back to the
desktop, just run the same commands in the terminal mentioned above, but
replace `false` at the end of the command with `true` value.

## REMOVE `HOME FOLDER FROM UBUNTU DESKTOP`

By default, in `Ubuntu 18.04 LTS` only shows a trash icon on the desktop, but
in the later version the developers decided that a home folder icon will also
appear on the desktop by default.

If you want to remove the home folder icon from the desktop on `Ubuntu 19.10`
or later, open a terminal and type this command:

```shell
gsettings set org.gnome.shell.extensions.desktop-icons show-home false
```

Just like before, if you want to restore the icon just replace `false` with
`true` and everything will be the way you want.
