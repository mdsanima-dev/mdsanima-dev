# Copyritht © 2022 Marcin Różewski MDSANIMA


"""Testing colors module function for setting default colors scheme."""


from __future__ import annotations

import pytest

from mdsanima_dev.colors import _get_normal_default


def test_color_name_default():
    ret = _get_normal_default()
    assert ret == 255


def test_color_name_cyan():
    ret = _get_normal_default("cyan")
    assert ret == 50


def test_color_name_sky():
    ret = _get_normal_default("sky")
    assert ret == 39


def test_color_name_blue():
    ret = _get_normal_default("blue")
    assert ret == 27


def test_color_name_indigo():
    ret = _get_normal_default("indigo")
    assert ret == 105


def test_color_name_violet():
    ret = _get_normal_default("violet")
    assert ret == 99


def test_color_name_purple():
    ret = _get_normal_default("purple")
    assert ret == 170


def test_color_name_fuchsia():
    ret = _get_normal_default("fuchsia")
    assert ret == 177


def test_color_name_pink():
    ret = _get_normal_default("pink")
    assert ret == 206


def test_color_name_rose():
    ret = _get_normal_default("rose")
    assert ret == 203


def test_color_name_red():
    ret = _get_normal_default("red")
    assert ret == 196


def test_color_name_orange():
    ret = _get_normal_default("orange")
    assert ret == 208


def test_color_name_amber():
    ret = _get_normal_default("amber")
    assert ret == 215


def test_color_name_yellow():
    ret = _get_normal_default("yellow")
    assert ret == 220


def test_color_name_lime():
    ret = _get_normal_default("lime")
    assert ret == 148


def test_color_name_green():
    ret = _get_normal_default("green")
    assert ret == 118


def test_color_name_emerald():
    ret = _get_normal_default("emerald")
    assert ret == 122


def test_color_name_teal():
    ret = _get_normal_default("teal")
    assert ret == 43


def test_color_name_graphe():
    ret = _get_normal_default("graphe")
    assert ret == 24


def test_color_name_giter():
    ret = _get_normal_default("giter")
    assert ret == 30


def test_color_name_slate():
    ret = _get_normal_default("slate")
    assert ret == 250


def test_color_name_gray():
    ret = _get_normal_default("gray")
    assert ret == 245


def test_color_name_zinc():
    ret = _get_normal_default("zinc")
    assert ret == 238


def test_color_name_white():
    ret = _get_normal_default("white")
    assert ret == 255


def test_color_name_black():
    ret = _get_normal_default("black")
    assert ret == 16


def test_color_name_no_exist():
    with pytest.raises(KeyError):
        no_exist = _get_normal_default("no_exist_color_name")
