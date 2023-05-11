# {octicon}`file-code;1em;sd-text-secondary` `EMOJI`

```{eval-rst}
.. automodule:: mdsanima_dev.emoji
```

```{eval-rst}
.. figure:: ../_images/gif/mdsanima_dev_python_emoji_a.gif
    :name: show-python-emoji-a
```

## FUNCTION `emoji_get_url_data`

```{eval-rst}
.. autofunction:: mdsanima_dev.emoji.emoji_get_url_data
```

## FUNCTION `emoji_clean_url_data`

```{eval-rst}
.. autofunction:: mdsanima_dev.emoji.emoji_clean_url_data
```

## FUNCTION `emoji_load_json_data`

```{eval-rst}
.. autofunction:: mdsanima_dev.emoji.emoji_load_json_data
```

```{eval-rst}
.. figure:: ../_images/gif/mdsanima_dev_python_emoji_b.gif
    :name: show-python-emoji-b
```

## CLASS `emoji`

```{eval-rst}
.. autoclass:: mdsanima_dev.emoji.emoji
    :members:
```

## CLASS `show`

```{eval-rst}
.. autoclass:: mdsanima_dev.emoji.show
    :members:
```

Now I will show you how to use class [show(emoji)](#class-show) method to find
out what number each emoji has so that you can use in your code:

```{eval-rst}
.. figure:: ../_images/gif/mdsanima_dev_python_emoji_c.gif
    :name: show-python-emoji-c
```

### METHOD `emo_stats()`

This method show statistic about emoji published on _.json_ files which was
retrieved on the [emoji_clean_url_data](#function-emoji-clean-url-data)
function. You can use _emoji_list_ or _emoji_modifiers_ only:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emo_stats()
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_01_acrylic_a.webp
            :name: show-emoji-01-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_01_dark_a.webp
            :name: show-emoji-01-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_01_acrylic_b.webp
            :name: show-emoji-01-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_01_dark_b.webp
            :name: show-emoji-01-dk-b
```

### METHOD `emo_all()`

This method will display all the available emoji from the list you have
selected. All emoji in the given group will be displayed on one line:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emo_all()
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_04_acrylic_a.webp
            :name: show-emoji-04-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_04_dark_a.webp
            :name: show-emoji-04-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_04_acrylic_b.webp
            :name: show-emoji-04-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_04_dark_b.webp
            :name: show-emoji-04-dk-b
```

#### METHOD `emo_all(True, False)`

The first argument is true so it will show us all the emoji and a number that
is assigned to the emoji. All emoji in the given group will be displayed on
one line:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emo_all(True, False)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_05_acrylic_a.webp
            :name: show-emoji-05-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_05_dark_a.webp
            :name: show-emoji-05-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_05_acrylic_b.webp
            :name: show-emoji-05-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_05_dark_b.webp
            :name: show-emoji-05-dk-b
```

#### METHOD `emo_all(False, True)`

The second argument is true so it will show us all the emojis and a name thats
is assigned to the emoji. All emoticons in a given group will be displayed
individually, each on a separate line:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emo_all(False, True)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_06_acrylic_a.webp
            :name: show-emoji-06-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_06_dark_a.webp
            :name: show-emoji-06-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_06_acrylic_b.webp
            :name: show-emoji-06-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_06_dark_b.webp
            :name: show-emoji-06-dk-b
```

#### METHOD `emo_all(True, True)`

Both arguments are true so I will show us the number assigned to the emoji
and its name. All emoticons in a given group will be displayed individually,
each on a separate line:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emo_all(True, True)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_07_acrylic_a.webp
            :name: show-emoji-07-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_07_dark_a.webp
            :name: show-emoji-07-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_07_acrylic_b.webp
            :name: show-emoji-07-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_07_dark_b.webp
            :name: show-emoji-07-dk-b
```

### METHOD `emo_big_head()`

This method shows all available big heads from the list you're selected:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emo_big_head()
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_02_acrylic_a.webp
            :name: show-emoji-02-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_02_dark_a.webp
            :name: show-emoji-02-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_02_acrylic_b.webp
            :name: show-emoji-02-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_02_dark_b.webp
            :name: show-emoji-02-dk-b
```

### METHOD `emo_head()`

This method displays all emojis from a given big head and medium head.
You always need to enter these two arguments _big_head_ and _medium_head_.
The next two arguments are for displaying emoji numbers and their names:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emo_head("objects", "music")
s.emo_head("objects", "music", True, False)
s.emo_head("objects", "music", True, True)
s.emo_head("objects", "music", False, True)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_08_acrylic_a.webp
            :name: show-emoji-08-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_08_dark_a.webp
            :name: show-emoji-08-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_08_acrylic_b.webp
            :name: show-emoji-08-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_08_dark_b.webp
            :name: show-emoji-08-dk-b
```

### METHOD `emo_medium_head()`

This method shows all available medium heads from the list you're selected:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emo_medium_head()
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_03_acrylic_a.webp
            :name: show-emoji-03-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_03_dark_a.webp
            :name: show-emoji-03-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_03_acrylic_b.webp
            :name: show-emoji-03-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_03_dark_b.webp
            :name: show-emoji-03-dk-b
```

### METHOD `emoji()`

Now you know what numbers each emoji has, so you can use this method for your
code. If you want to print on a new line use this argument `end = "\n"`
or just simple `show("emoji_list").emoji(86, "\n")` thats it:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
s.emoji(1132)
s.emoji(14, "\n")
s.emoji(86, end="\n")
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_09_acrylic_a.webp
            :name: show-emoji-09-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_09_dark_a.webp
            :name: show-emoji-09-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_09_acrylic_b.webp
            :name: show-emoji-09-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_09_dark_b.webp
            :name: show-emoji-09-dk-b
```

#### METHOD `emoji()` FOR LOOP `emoji_list` FIRST

This way you can now print the first 67 emojis from the list selected:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
for i in range(1, 167):
    s.emoji(i)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_10_acrylic_a.webp
            :name: show-emoji-10-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_10_dark_a.webp
            :name: show-emoji-10-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_10_acrylic_b.webp
            :name: show-emoji-10-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_10_dark_b.webp
            :name: show-emoji-10-dk-b
```

#### METHOD `emoji()` FOR LOOP `emoji_list` ALL

This way you can print all available emojis from the list selected:

```python
from mdsanima_dev.emoji import show
s = show("emoji_list")
for i in range(1, 1816):
    s.emoji(i)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_11_acrylic_a.webp
            :name: show-emoji-11-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_11_dark_a.webp
            :name: show-emoji-11-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_11_acrylic_b.webp
            :name: show-emoji-11-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_11_dark_b.webp
            :name: show-emoji-11-dk-b
```

#### METHOD `emoji()` FOR LOOP `emoji_modifiers` ALL

This way you can print all available emojis from the list selected:

```python
from mdsanima_dev.emoji import show
s = show("emoji_modifiers")
for i in range(1, 1705):
    s.emoji(i)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_12_acrylic_a.webp
            :name: show-emoji-12-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_12_dark_a.webp
            :name: show-emoji-12-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_12_acrylic_b.webp
            :name: show-emoji-12-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_12_dark_b.webp
            :name: show-emoji-12-dk-b
```

### ALL `METHOD`

Show all methods to get the correct number for your emoji:

```python
from mdsanima_dev.emoji import show
s = show("emoji_modifiers")
s.emo_big_head()
s.emo_medium_head()
s.emo_head("component", "skin_tone")
s.emo_head("component", "skin_tone", True, False)
s.emo_head("component", "skin_tone", False, True)
s.emo_head("component", "skin_tone", True, True)
s.emoji(1704, "\n")
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/emoji_show_13_acrylic_a.webp
            :name: show-emoji-13-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/emoji_show_13_dark_a.webp
            :name: show-emoji-13-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/emoji_show_13_acrylic_b.webp
            :name: show-emoji-13-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/emoji_show_13_dark_b.webp
            :name: show-emoji-13-dk-b
```
