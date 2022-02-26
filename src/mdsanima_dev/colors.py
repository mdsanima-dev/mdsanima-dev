# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Complex colors printed in the console output with your own text."""


def set_complex_color() -> str:
    """Define color console variables.

    :return: Color console literal variable.
    :rtype: str

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable:*

    .. code:: python

        sx, xm, ex = complex_color()
        start_c, middle_c, end_c = complex_color()

    .. admonition:: WARNING
        :class: warning

        Do not use this function in your code, it is needed to perform other
        functions.
    """
    sx = "\x1b[38;5;"
    xm = "m"
    ex = "\x1b[0m"

    return sx, xm, ex


def get_color(text: str = "mdsanima", color: int = 255) -> str:
    """This function is almost the same as
    `get_complex_color <#function-get-complex-color>`_ function.

    The difference is that the return is a sequence of unicode characters
    and to get the output in the terminal in a color you need to use the
    print function.

    :param text: The text you want to use for color output in the console,
        defaults to ``mdsanima``.
    :type text: str, optional
    :param color: The color number you want to use for color output in the
        console, defaults to 255.
    :type color: int, optional
    :return: Colored text output in the console.
    :rtype: str

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function by* `calling <#code-calling>`_ *to variable.*
        `Assigning <#code-assigning>`_ *a function to a variable.*
        *Also you can use* `machine <../modules/tools.html#function-machine>`_
        *function on this* `code example <#code-machine>`_ *block:*

    .. _code-calling:
    .. code:: python

        mds_a = get_color("I love Python", 86)
        mds_b = get_color("mdsanima", 186)
        print(mds_a, mds_b)

    .. _code-assigning:
    .. code:: python

        mds = get_color
        mds_a = mds("I love Python", 86)
        mds_b = mds("mdsanima", 186)
        print(mds_a, mds_b)

    .. _code-machine:
    .. code:: python

        from mdsanima_dev.utils.tools import machine
        mds = get_color
        mds_a = mds("I love Python", 86)
        mds_b = mds("mdsanima", 186)
        machine(mds_a + " " + mds_b, 0.01)
    """
    sx, xm, ex = set_complex_color()

    return sx + str(color - 1) + xm + text + ex


def get_complex_color(
    text: str = "mdsanima", color: int = 255, end=None
) -> str:
    """
    This feature allows you to print colored text to the output of the console.
    Now the function works the same like print function.

    :param text: The text you want to use for color output in the console,
        defaults to ``mdsanima``.
    :type text: str, optional
    :param color: The color number you want to use for color output in the
        console, defaults to 255.
    :type color: int, optional
    :param end: End of line print, defaults to ``None``.
    :type end: str, optional
    :return: Colored text output in the console.
    :rtype: str

    .. admonition:: USAGE PYTHON
        :class: hint

        *Assigning a function to a variable* `mds` then *function calling*
        returning printing colored text on the same line:

    .. code:: python

        mds = get_complex_color
        mds(color=44)
        mds("mdsa", 160, " ")
        mds("mds", 88, " ")
        mds(text="mds", color=99, end=" ")
        mds("mds", 86)
        mds(end="mdsanima-dev", color=85, text="mds")
    """
    sx, xm, ex = set_complex_color()
    print(sx + str(color - 1) + xm + text + ex, end=end)

    return str


def show_complex_color(number: bool = False) -> str:
    """Function prints all available colors with a number or only text.

    :param number: Show color number, defaults to ``False``.
    :type number: bool, optional
    :return: Show all colors in the console output.
    :rtype: str

    .. admonition:: USAGE PYTHON
        :class: hint

        *Function calling:*

    .. code:: python

        show_complex_color(False)
        show_complex_color(True)
    """
    sx, xm, ex = set_complex_color()
    col = [251, 246, 243, 197, 161]
    cna = sx + str(col[0] - 1) + xm + "[" + ex
    cnb = sx + str(col[0] - 1) + xm + "\n\n[" + ex
    csh = sx + str(col[1] - 1) + xm + "SHOW COMPLEX COLOR " + ex
    cdo = sx + str(col[2] - 1) + xm + "DONE COMPLEX COLOR " + ex
    cmd = sx + str(col[3] - 1) + xm + "MDSANIMA" + ex
    cnu = sx + str(col[4] - 1) + xm + "NUMBER" + ex
    cnc = sx + str(col[0] - 1) + xm + "]" + ex
    cne = sx + str(col[0] - 1) + xm + "]\n" + ex

    # Print info options.
    if number == False:
        show = "mdsanima".ljust(9)
        print(cna + csh + cmd + cne)
        done = cnb + cdo + cmd + cnc
    else:
        print(cna + csh + cnu + cne)
        done = cnb + cdo + cnu + cnc

    # Print all colors.
    for i in range(255):
        if number == True:
            show = "--> " + str(i + 1).ljust(5)
        color = sx + str(i) + xm + show + ex
        print(color, sep=" ", end="", flush=True)

    return print(done)
