"""
# Table Module

Making a cool table.
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
        Initial color table.

        Args:
            color (int, optional): Color of the table. Defaults to 255.
        Returns:
            int: Number of colors from `colors` module.
        """
        self.tab_color = color

    def connect(self, top: bool, length: int, bot: bool) -> str:
        """
        Checking for connecting table.

        Args:
            top (bool): Top element of the table.
            length (int): Length of the table.
            bot (bool): Bottom element of the table.
        Returns:
            str: Element printing of the table in unicode value.
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

        Args:
            header (str): Headers with connectiog or nor.
            hcolor (int, optional): Color of text. Defaults to 255.
            top (bool, optional): Check connecting top. Defaults to False.
            bot (bool, optional): Check connection bootom. Defaults to False.
            tcolor (int, optional): Table color. Defaults to 255.
        Returns:
            str: Headers element of tempalte table.
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
        self.mds(' ' + self.header.ljust(head_len-2).upper(), self.color, ' ')
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
        Content of the tempalte table. This table constrain two text value.

        Args:
            content_key (str): First text value in the left.
            content_val (str): Second text value in the right.
            key_color (int, optional): Text color content key. Defaults to 255.
            val_color (int, optional): Text color content val. Defaults to 255.
            top (bool, optional): Check connecting top. Defaults to False.
            bot (bool, optional): Check connecting bootom. Defaults to False.
            tcolor (int, optional): Table color. Defaults to 255.
        Returns:
            str: Content elemento of template table.
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
        Initial finction.

        Args:
            color (int): Number of colors from `colors` module.
        Returns:
            str: Color value.
        """
        self.mds = colors.get_complex_color
        self.color = color

    def top(self, length: int) -> str:
        """
        Top element of the table.

        Args:
            length (int): Length of the table element.
        Returns:
            str: Unicode top element printing in one line.
        """
        self.header = ('\u250c' + ('\u2500' * length) + '\u2510')
        self.mds(self.header, self.color)

    def mid(self, length: int) -> str:
        """
        Midle element of the table.

        Args:
            length (int): Length of the table element.
        Returns:
            str: Unicode midle element printing in one line.
        """
        self.middle = ('\u251c' + ('\u2500' * length) + '\u2524')
        self.mds(self.middle, self.color)

    def bot(self, length: int) -> str:
        """
        Bootom element of the table.

        Args:
            length (int): Length of the table element.
        Returns:
            str: Unicode bootom element printing in one line.
        """
        self.bottom = ('\u2514' + ('\u2500' * length) + '\u2518')
        self.mds(self.bottom, self.color)

    def hed(self,
            length: int, text: str, text_color: int
        ) -> str:
        """
        Header element of the table one text value.

        Args:
            length (int): Length of the table element.
            text (str): Text printing inside table.
            text_color (int): Text color.
        Returns:
            str: Unicode header element printing in one line.
        """
        self.text = text.ljust(length-1)
        self.mds('\u2502', self.color, '')
        self.mds(' ' + self.text.upper(), text_color, '')
        self.mds('\u2502', self.color)

    def con(self,
            length: int, key: str, val: str,
            k_clr: int, v_clr: int
        ) -> str:
        """
        Content element of the table two text value.

        Args:
            length (int): Length of the table element.
            key (str): Text printing inside table in the left.
            val (str): Text printing inside table in the right.
            k_clr (int): Text color key.
            v_clr (int): Text color val.
        Returns:
            str: Unicode content element printing in one line.
        """
        self.con_key = key
        self.con_val = val
        k_len = len(key)
        v_len = len(val)
        ajst = k_len + v_len + 5
        self.mds('\u2502', self.color, '')
        self.mds(' ' + self.con_key.upper(), k_clr, ' ->')
        self.mds(' ' + self.con_val.upper(), v_clr, ' '.ljust(length-ajst))
        self.mds('\u2502', self.color)
