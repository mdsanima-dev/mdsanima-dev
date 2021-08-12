"""
Printing a colored table in the terminal console output.
"""

from mdsanima_dev import colors


class table:
    """
    This class create template table with colors, headers and content.
    """
    def __init__(self):
        self.mds = colors.get_complex_color

    def colors(self, color:int=255) -> int:
        """
        Initial color table. Only use for this class.

        :param color: color of the table, defaults to 255
        :type color: int, optional
        :return: number of colors from ``colors`` module
        :rtype: int
        """
        self.tab_color = color

    def connect(self, top: bool, length: int, bot: bool) -> str:
        """
        Checking for connectiong table.

        :param top: top element of the table
        :type top: bool
        :param length: length of the table
        :type length: int
        :param bot: bottom element of the table
        :type bot: bool
        :return: element printing of the table in unicode value
        :rtype: str
        """
        header = ('\u250c' + ('\u2500' * length) + '\u2510')
        conect = ('\u251c' + ('\u2500' * length) + '\u2524')
        bottom = ('\u2514' + ('\u2500' * length) + '\u2518')
        self.top = conect if top else header
        self.bot = conect if bot else bottom
        self.con_top = '' if top else header
        self.con_bot = '' if bot else bottom

    def headers(self,
            header: str, hcolor: int = 255,
            top: bool = False, bot: bool = False,
            tcolor: int = 255
        ) -> str:
        """
        Headers of the template table.

        :param header: headers text
        :type header: str
        :param hcolor: color of text, defaults to 255
        :type hcolor: int, optional
        :param top: check connecting top, defaults to ``False``
        :type top: bool, optional
        :param bot: check connecting bootom, defaults to ``False``
        :type bot: bool, optional
        :param tcolor: table color, defaults to 255
        :type tcolor: int, optional
        :return: headers element of template table
        :rtype: str
        :usage:

            assigning function calling to a variable

            .. code:: python

                from mdsanima_dev.utils.table import table
                t = table()
                t.headers('I Love Python mdsanima.com')
                t.headers('I Love Python mdsanima.com', hcolor=50)
                t.headers('I Love Python mdsanima.com', hcolor=197, tcolor=203)
                t.headers('I Love Python mdsanima.com'.center(40),
                            hcolor=34, tcolor=220)
        """
        self.header = header
        self.color = hcolor
        head_len = len(self.header) + 2

        # Init colors and conect function.
        self.connect(top, head_len, bot)
        self.colors(tcolor)

        # Table top.
        self.mds(self.top, self.tab_color)

        # Table midle.
        self.mds('\u2502', self.tab_color, '')
        self.mds(' ' + self.header.ljust(head_len-2), self.color, ' ')
        self.mds('\u2502', self.tab_color)

        # Table bottom.
        self.mds(self.bot, self.tab_color)

    def content(self,
            content_key: str, content_val: str,
            key_color: int = 255, val_color: int = 255,
            top: bool = False, bot: bool = False,
            tcolor: int = 255
        ) -> str:
        """
        Content of the template table. This table constrain two text value.

        :param content_key: first text value in the left
        :type content_key: str
        :param content_val: second text value in the right
        :type content_val: str
        :param key_color: text color content key, defaults to 255
        :type key_color: int, optional
        :param val_color: text color content value, defaults to 255
        :type val_color: int, optional
        :param top: check connecting top, defaults to ``False``
        :type top: bool, optional
        :param bot: check connecting bootom, defaults to ``False``
        :type bot: bool, optional
        :param tcolor: table color, defaults to 255
        :type tcolor: int, optional
        :return: content element of template table
        :rtype: str
        :usage:

            assigning function calling to a variable

            .. code:: python

                from mdsanima_dev.utils.table import table
                t = table()
                t.content('I Love Python', 'mdsanima.com')
                t.content('I Love Python', 'mdsanima.com', tcolor=197)
                t.content('I Love Python', 'mdsanima.com',
                            tcolor=227, key_color=86, val_color=76)
                t.content('I Love Python'.rjust(20), 'mdsanima.com'.ljust(20),
                            tcolor=31, key_color=32, val_color=33)
        """
        self.key = content_key
        self.val = content_val
        self.key_col = key_color
        self.val_col = val_color
        key_len = len(self.key)
        val_len = len(self.val)
        tab_len = key_len + val_len + 6

        # Init colors and conect function.
        self.connect(top, tab_len, bot)
        self.colors(tcolor)

        # Checking end value.
        top_end = '' if top else '\n'
        bot_end = '' if bot else '\n'

        # Table top.
        self.mds(self.con_top, self.tab_color, top_end)

        # Table big head.
        self.mds('\u2502', self.tab_color, '')
        self.mds(' ' + self.key.ljust(key_len), self.key_col, ' ->')
        self.mds(' ' + self.val.ljust(val_len), self.val_col, ' ')
        self.mds('\u2502', self.tab_color)

        # Table bottom.
        self.mds(self.con_bot, self.tab_color, bot_end)


class table_elem:
    """
    Element of the table to create your own, what you want.
    """
    def __init__(self, color: int) -> str:
        """
        Initial function element of the table.

        :param color: number of color from ``colors`` module
        :type color: int
        :return: color value
        :rtype: str
        """
        self.mds = colors.get_complex_color
        self.color = color

    def top(self, length: int) -> str:
        """
        Top element of the table.

        :param length: length of the table element
        :type length: int
        :return: unicode top element printing in one line
        :rtype: str
        """
        self.header = ('\u250c' + ('\u2500' * length) + '\u2510')
        self.mds(self.header, self.color)

    def mid(self, length: int) -> str:
        """
        Midle element of the table.

        :param length: length of the table element
        :type length: int
        :return: unicode midle element printing in one line
        :rtype: str
        """
        self.middle = ('\u251c' + ('\u2500' * length) + '\u2524')
        self.mds(self.middle, self.color)

    def bot(self, length: int) -> str:
        """
        Bootom element of the table.

        :param length: length of the table element
        :type length: int
        :return: unicode bootom element printing in one line
        :rtype: str
        """
        self.bottom = ('\u2514' + ('\u2500' * length) + '\u2518')
        self.mds(self.bottom, self.color)

    def hed(self, length: int, text: str, text_color: int) -> str:
        """
        Header element of the table on text value.

        :param length: length of the table element
        :type length: int
        :param text: text printing inside table
        :type text: str
        :param text_color: text color value
        :type text_color: int
        :return: unicode header element printing in one line
        :rtype: str
        """
        self.text = text.ljust(length-1)
        self.mds('\u2502', self.color, '')
        self.mds(' ' + self.text.upper(), text_color, '')
        self.mds('\u2502', self.color)

    def con(self,
            length: int, key: str, val: str, k_clr: int, v_clr: int
        ) -> str:
        """
        Content element of the table two text value.

        :param length: length of the table element
        :type length: int
        :param key: text printing inside table in the left
        :type key: str
        :param val: text printing inside table in the right
        :type val: str
        :param k_clr: text color key
        :type k_clr: int
        :param v_clr: text color value
        :type v_clr: int
        :return: unicode content element printing in one line
        :rtype: str
        """
        self.con_key = key
        self.con_val = val
        k_len = len(key)
        v_len = len(val)
        ajst = k_len + v_len + 5
        self.mds('\u2502', self.color, '')
        self.mds(' ' + self.con_key, k_clr, ' ->')
        self.mds(' ' + self.con_val, v_clr, ' '.ljust(length-ajst))
        self.mds('\u2502', self.color)
