"""
# Table Module

Making a cool table.
"""

from mdsanima_dev import colors


class table:
    def __init__(self):
        self.mds = colors.get_complex_color

    def colors(self, color:int=255) -> int:
        self.tab_color = color

    def connect(self, top: bool, length: int, bot: bool) -> str:
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
            tcolor: int = 255) -> str:
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
            tcolor: int = 255) -> str:
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
    def __init__(self, color: int) -> str:
        self.mds = colors.get_complex_color
        self.color = color

    def top(self, length: int) -> str:
        self.header = ('\u250c' + ('\u2500' * length) + '\u2510')
        self.mds(self.header, self.color)

    def mid(self, length: int) -> str:
        self.middle = ('\u251c' + ('\u2500' * length) + '\u2524')
        self.mds(self.middle, self.color)

    def bot(self, length: int) -> str:
        self.bottom = ('\u2514' + ('\u2500' * length) + '\u2518')
        self.mds(self.bottom, self.color)

    def hed(self, length: int, text: str, text_color: int) -> str:
        self.text = text.ljust(length-1)
        self.mds('\u2502', self.color, '')
        self.mds(' ' + self.text.upper(), text_color, '')
        self.mds('\u2502', self.color)

    def con(self, length: int, key: str, val: str,
            k_clr: int, v_clr: int) -> str:
        self.con_key = key
        self.con_val = val
        k_len = len(key)
        v_len = len(val)
        ajst = k_len + v_len + 5
        self.mds('\u2502', self.color, '')
        self.mds(' ' + self.con_key.upper(), k_clr, ' ->')
        self.mds(' ' + self.con_val.upper(), v_clr, ' '.ljust(length-ajst))
        self.mds('\u2502', self.color)
