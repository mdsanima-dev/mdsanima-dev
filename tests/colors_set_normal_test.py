# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Testing colors module function for setting sytax mode variation."""


from __future__ import annotations

from mdsanima_dev.colors import _set_normal_syntax


def test_mode_normal_return():
    ret = _set_normal_syntax()
    assert ret == ("\x1b[38;5;", "\x1b[48;5;", "m", "\x1b[0m")


def test_mode_normal_asigning(capsys):
    fg, bg, xm, ex = _set_normal_syntax()
    out, _ = capsys.readouterr()
    assert out == ""
