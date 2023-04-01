# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Module :bdg-success-line:`colors` is for printing complex colors in the
console output with your own texts. This module is for also for showing example
colors output in the shell terminal window. You can use this output on your
future projects.

The core functionality is for replace default :bdg-primary-line:`print`
function to allow printing your string in colors on the terminal window. You
can use many default colors available on ``int`` values or you can use
a default color names scheme like ``blue`` or ``red`` options.
"""


from __future__ import annotations

import os
from typing import Union


INFO_KEY_ERROR = "Please choose a name from this default colors scheme"
INFO_OPT_ERROR = "Please choose from this 'number', 'name' or 'text' options"
DEFAULT_NAMES_NORMAL = {
    "cyan": 50,
    "sky": 39,
    "blue": 27,
    "indigo": 105,
    "violet": 99,
    "purple": 170,
    "fuchsia": 177,
    "pink": 206,
    "rose": 203,
    "red": 196,
    "orange": 208,
    "amber": 215,
    "yellow": 220,
    "lime": 148,
    "green": 118,
    "emerald": 122,
    "teal": 43,
    "graphe": 24,
    "giter": 30,
    "slate": 250,
    "gray": 245,
    "zinc": 238,
    "white": 255,
    "black": 16,
}


def _get_normal_default(color_name: str = "white") -> int:
    """Define default color scheme with several name variants for normal mode
    option that getting color number.

    .. warning:: Do not use this function in your code, it is needed to perform
        other functions.

    :param color_name: Choose a color name string instead of typing number,
        defaults to ``white``.
    :type color_name: str, optional
    :return: Color number for text foreground and background syntax output.
        Return type ``int``.
    """
    color_number = DEFAULT_NAMES_NORMAL[color_name]
    return color_number


def _set_normal_syntax() -> str:
    """Define colors variables foreground and background ``x1b`` syntax with
    normal mode for printing text with 256 colors.

    .. warning:: Do not use this function in your code, it is needed to perform
        other functions.

    :return: Color console literal variable for text foreground and background.
        Return type ``str``.
    """
    fg = "\x1b[38;5;"
    bg = "\x1b[48;5;"
    xm = "m"
    ex = "\x1b[0m"
    return fg, bg, xm, ex


def use_normal_mode(
    text: str = "mdsanima",
    fg_color: Union[str, int] = 255,
    bg_color: Union[str, int] = None,
) -> str:
    """This feature returning string with ``x1b`` syntax that allow to print
    the text with 256 colors normal mode on your output.

    :param text: The text foreground that's you want to print with colors,
        defaults to ``mdsanima``.
    :type text: str, optional
    :param fg_color: The color number or default name for text foreground.
        Choose a number from 0 to 255 or use color name, defaults to ``255``.
    :type fg_color: Union[str, int], optional
    :param bg_color: The color number or default name for background.
        Choose a number from 0 to 255 or use color name, defaults to ``None``.
    :type bg_color: Union[str, int], optional
    :return: Text string output with colors ``x1b`` systax.
        Return type ``str``.
    """
    fg, bg, xm, ex = _set_normal_syntax()
    try:
        if type(fg_color) == str:
            fg_color = _get_normal_default(fg_color)
        if type(bg_color) == str:
            bg_color = _get_normal_default(bg_color)
        if bg_color == None:
            foreground = fg + str(fg_color) + xm
            out_result = foreground + text + ex
        else:
            foreground = fg + str(fg_color) + xm
            background = bg + str(bg_color) + xm
            out_result = foreground + background + text + ex
        return out_result
    except KeyError:
        print(INFO_KEY_ERROR, DEFAULT_NAMES_NORMAL.keys())


def print_normal_mode(
    text: str = "mdsanima",
    fg_color: Union[str, int] = 255,
    bg_color: Union[str, int] = None,
    end=None,
) -> None:
    """This feature allows to print text and background with ``x1b`` syntax
    256 colors normal mode on your output. The function works the same like
    standard print function.

    :param text: The text foreground that's you want to print with colors,
        defaults to ``mdsanima``.
    :type text: str, optional
    :param fg_color: The color number or default name for text foreground.
        Choose a number from 0 to 255 or use color name, defaults to ``255``.
    :type fg_color: Union[str, int], optional
    :param bg_color: The color number or default name for background.
        Choose a number from 0 to 255 or use color name, defaults to ``None``.
    :type bg_color: Union[str, int], optional
    :param end: End of line print options, defaults to ``None``.
    :type end: None, optional
    :return: Printing colored string text foreground and background output.
        Return type ``None``.
    """
    out_result = use_normal_mode(text, fg_color, bg_color)
    return print(out_result, end=end)


def show_normal_colors(options: str = "number") -> str:
    """This function is for showing all available colors number or string
    example text output.

    :param options: What example will be show on print. Choose from this
        ``number``, ``name`` or ``text`` options, defaults to ``number``.
    :type options: str, optional
    :return: Printing all colors number, name or text example output.
        Return type ``str``.
    """
    fg, bg, xm, ex = _set_normal_syntax()

    # Setup colors for info print.
    colors = [196, 208, 70, 180, 0]

    # Setup unicode character.
    unicode_one = "\U0000005C"  # \
    unicode_two = "\U0000002F"  # /

    # Get terminal size columns for center info print.
    terminal = os.get_terminal_size()

    # Calculation terminal size based on 22 count string from info variables.
    calculate_befor = terminal.columns / 2 - 11
    calculate_after = terminal.columns / 2 - 11

    # Print across terminal size.
    befor = unicode_one * int(calculate_befor)
    after = unicode_two * int(calculate_after)

    # Setup colors info variables.
    cts = fg + str(colors[4]) + xm + bg + str(colors[0]) + xm + befor + ex
    cna = fg + str(colors[0]) + xm + "[" + ex
    csh = fg + str(colors[1]) + xm + " SHOW COLORS " + ex
    cdo = fg + str(colors[2]) + xm + " DONE COLORS " + ex
    cnu = fg + str(colors[3]) + xm + "NUMBER " + ex
    cnn = fg + str(colors[3]) + xm + " NAMES " + ex
    cmd = fg + str(colors[3]) + xm + " TEXTS " + ex
    cnc = fg + str(colors[0]) + xm + "]" + ex
    cte = fg + str(colors[4]) + xm + bg + str(colors[0]) + xm + after + ex

    # Print info colors options.
    if options == "number":
        print(cts + cna + csh + cnu + cnc + cte)
        done = "\n" + cte + cna + cdo + cnu + cnc + cts
    if options == "name":
        print(cts + cna + csh + cnn + cnc + cte)
        done = "\n" + cte + cna + cdo + cnn + cnc + cts
    if options == "text":
        print(cts + cna + csh + cmd + cnc + cte)
        done = "\n" + cte + cna + cdo + cmd + cnc + cts
    else:
        done = INFO_OPT_ERROR

    # Print all colors numbers.
    if options == "number" or options == "text":
        for i in range(256):
            if options == "number":
                show = "--> " + str(i).ljust(5)
            if options == "text":
                show = "mdsanima".ljust(9)
            color = fg + str(i) + xm + show + ex
            print(color, sep=" ", end="", flush=True)
    if options == "name":
        default_key = DEFAULT_NAMES_NORMAL.keys()
        for name in list(default_key):
            show = str(name) + " "
            color = fg + str(DEFAULT_NAMES_NORMAL[name]) + xm + show + ex
            print(color, sep=" ", end="", flush=True)

    return print(done)
