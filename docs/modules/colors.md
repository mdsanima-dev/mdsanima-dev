# {octicon}`file-code;1em;sd-text-secondary` `COLORS`

```{eval-rst}
.. automodule:: mdsanima_dev.colors
.. versionadded:: 0.1.0
```

## FUNCTION `use_default`

```{eval-rst}
.. autofunction:: mdsanima_dev.colors.use_default


    This function is almost the same as
    `print_default_color <#function-print-default-color>`_ function but it
    differs in one specific detail.

    The difference is that the return is a sequence of unicode characters
    and to get the output in the terminal in a color you need to use the
    print function.

    :usage:

        Assigning a function to variable. After imports modules add this code
        ``color_text = use_default_color`` then in the next line type this
        pieces ``mdsanima = color_text("I love Python", 39)`` of code. Next you
        can simple type this ``print(mdsanima)`` code for printing color text
        string output in your shell terminal window. Also instead of typing
        color number you can us default colors name scheme like ``sky`` or
        ``blue`` color.

        Assigning a function by calling to a variable, use this example code:

        .. code:: python

            from mdsanima_dev.colors import use_default_color
            love = use_default_color("I love Python", 86)
            devs = use_default_color("App Development", "red")
            print(love, devs)

        You can also use `machine <../tools/#function-machine>`_ function with
        this example code:

        .. code:: python

            from mdsanima_dev.colors import use_default_color
            from mdsanima_dev.utils.tools import machine
            love = use_default_color("I love Python", 74)
            devs = use_default_color("App Development", "indigo")
            machine(love + " " + devs, 0.01)

  :screenshots:

    Want to see :bdg-warning-line:`Terminal Screenshots` from the sample code
    above along with cool show output that's we produced. See this examples
    `output use_colors <../../screenshots/colors/#examples-output-use-colors>`_
    link.

.. versionchanged:: 0.2.0
```

## FUNCTION `print_default`

```{eval-rst}
.. autofunction:: mdsanima_dev.colors.print_default


    :usage:

        Assigning a function to a ``mdsanima`` variable. Instead of typing
        ``mdsanima`` you can assign any string in these variable like
        ``my_print`` or something else. Then call this funtion to returning
        printing colored text on the same line or next line.

        You can simple create test function like this sample code:

        .. code:: python

            from mdsanima_dev.colors import print_default_color

            mdsanima = print_default_color

            def printing_color():
                mdsanima(color=42)
                mdsanima("example", 30, end=" ")
                mdsanima("colored text", 32, end=" ")
                mdsanima(text="development", color=38, end=" ")
                mdsanima("in one line", 86)
                mdsanima(color=50, text="your text", end=" ")
                mdsanima("example", color=80, end=" in ")
                mdsanima("colors", color=110, end=" ")
                mdsanima("more devs colors", color=140)
                mdsanima(color=48)

            printing_color()

  :screenshots:

    Want to see :bdg-warning-line:`Terminal Screenshots` from the sample code
    above along with cool show output that's we produced. See this examples
    `output print_colors <../../screenshots/colors/#examples-output-print-colors>`_
    link.

.. versionchanged:: 0.2.0
```

## FUNCTION `show_colors`

```{eval-rst}
.. autofunction:: mdsanima_dev.colors.show_colors


    :usage:

        This is a function call. Type this sample code in your console:

        .. code:: python

            from mdsanima_dev.colors import show_colors
            show_colors(True)
            show_colors(False)

  :screenshots:

    Want to see :bdg-warning-line:`Terminal Screenshots` from the sample code
    above along with cool show output that's we produced. See this examples
    `output show_colors <../../screenshots/colors/#examples-output-show-colors>`_
    link.

.. versionchanged:: 0.2.0
```
