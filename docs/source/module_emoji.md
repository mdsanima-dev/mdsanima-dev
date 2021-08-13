# Module `emoji`

```{eval-rst}
.. automodule:: mdsanima_dev.emoji
```

```{eval-rst}
.. figure:: _static/gif/emoji_show_d_04_optymize.gif
    :name: show-emoji-04-gif-d
```

## Function `emoji_get_url_data`

```{eval-rst}
.. autofunction:: mdsanima_dev.emoji.emoji_get_url_data
```

## Function `emoji_clean_url_data`

```{eval-rst}
.. autofunction:: mdsanima_dev.emoji.emoji_clean_url_data
```

## Function `emoji_load_json_data`

```{eval-rst}
.. autofunction:: mdsanima_dev.emoji.emoji_load_json_data
```

```{eval-rst}
.. figure:: _static/gif/emoji_show_c_04_optymize.gif
    :name: show-emoji-04-gif-c
```

## Class `emoji`

```{eval-rst}
.. autoclass:: mdsanima_dev.emoji.emoji
    :members:
```

## Class `show`

```{eval-rst}
.. autoclass:: mdsanima_dev.emoji.show
    :members:
```

```{admonition} Note
Now I will show you how to use ``class show(emoji)`` to find out what number
each emoji has so that you can use in your code.
Check first method
[``emo_stat()``](#method-emo-stats) and so on
[``emo_big_head()``](#method-emo-big-head),
[``emo_medium_head()``](#method-emo-medium-head),
[``emo_all()``](#method-emo-all),
[``emo_head()``](#method-emo-head),
[``emoji()``](#method-emoji) and
[``all method``](#all-method).
```

```{eval-rst}
.. figure:: _static/gif/emoji_show_a_04_optymize.gif
    :name: show-emoji-04-gif-a
```

### Method ``emo_stats()``

This method show statistic about emoji published on json which was retrieved
with the function [``emoji_clean_url_data``](#function-emoji-clean-url-data).
You can use ``emoji_list`` or ``emoji_modifiers`` only.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emo_stats()
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_01_acrylic_a.jpg
    :name: show-emoji-01-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_01_dark_a.jpg
    :name: show-emoji-01-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_01_acrylic_b.jpg
    :name: show-emoji-01-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_01_dark_b.jpg
    :name: show-emoji-01-dk-b
```
````

### Method ``emo_big_head()``

This method shows all available big heads from the list you selected.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emo_big_head()
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_02_acrylic_a.jpg
    :name: show-emoji-02-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_02_dark_a.jpg
    :name: show-emoji-02-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_02_acrylic_b.jpg
    :name: show-emoji-02-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_02_dark_b.jpg
    :name: show-emoji-02-dk-b
```
````

### Method ``emo_medium_head()``

This method shows all available medium heads from the list you selected.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emo_medium_head()
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_03_acrylic_a.jpg
    :name: show-emoji-03-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_03_dark_a.jpg
    :name: show-emoji-03-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_03_acrylic_b.jpg
    :name: show-emoji-03-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_03_dark_b.jpg
    :name: show-emoji-03-dk-b
```
````

### Method ``emo_all()``

This method will display all the available emojis from the list you have
selected. All emojis in the given group will be displayed on one line.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emo_all()
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_04_acrylic_a.jpg
    :name: show-emoji-04-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_04_dark_a.jpg
    :name: show-emoji-04-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_04_acrylic_b.jpg
    :name: show-emoji-04-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_04_dark_b.jpg
    :name: show-emoji-04-dk-b
```
````

#### ``emo_all(True, False)``

The first argument is true so it will show us all the emojis and a number that
is assigned to the emoji. All emojis in the given group will be displayed on
one line.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emo_all(True, False)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_05_acrylic_a.jpg
    :name: show-emoji-05-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_05_dark_a.jpg
    :name: show-emoji-05-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_05_acrylic_b.jpg
    :name: show-emoji-05-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_05_dark_b.jpg
    :name: show-emoji-05-dk-b
```
````

#### ``emo_all(False, True)``

The second argument is true so it will show us all the emojis and a name thats
is assigned to the emoji. All emoticons in a given group will be displayed
individually, each on a separate line.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emo_all(False, True)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_06_acrylic_a.jpg
    :name: show-emoji-06-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_06_dark_a.jpg
    :name: show-emoji-06-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_06_acrylic_b.jpg
    :name: show-emoji-06-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_06_dark_b.jpg
    :name: show-emoji-06-dk-b
```
````

#### ``emo_all(True, True)``

Both arguments are true so I will show us the number assigned to the emoji
and its name. All emoticons in a given group will be displayed individually,
each on a separate line.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emo_all(True, True)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_07_acrylic_a.jpg
    :name: show-emoji-07-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_07_dark_a.jpg
    :name: show-emoji-07-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_07_acrylic_b.jpg
    :name: show-emoji-07-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_07_dark_b.jpg
    :name: show-emoji-07-dk-b
```
````

### Method ``emo_head()``

This method displays all emojis from a given big head and medium head.
You always need to enter these two arguments ``big_head`` and ``medium_head``.
The next two arguments are for displaying emoji numbers and their names.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emo_head('objects', 'music')
s.emo_head('objects', 'music', True, False)
s.emo_head('objects', 'music', True, True)
s.emo_head('objects', 'music', False, True)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_08_acrylic_a.jpg
    :name: show-emoji-08-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_08_dark_a.jpg
    :name: show-emoji-08-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_08_acrylic_b.jpg
    :name: show-emoji-08-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_08_dark_b.jpg
    :name: show-emoji-08-dk-b
```
````

### Method ``emoji()``

Now you know what numbers each emoji has, so you can use this method for your
code. If you want to print on a new line use this argument ``end = '\n'``
or just simple ``show('emoji_list').emoji(86, '\n')`` thats it.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
s.emoji(1132)
s.emoji(14, '\n')
s.emoji(86, end='\n')
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_09_acrylic_a.jpg
    :name: show-emoji-09-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_09_dark_a.jpg
    :name: show-emoji-09-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_09_acrylic_b.jpg
    :name: show-emoji-09-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_09_dark_b.jpg
    :name: show-emoji-09-dk-b
```
````

#### ``emoji()`` for loop ``emoji_list`` fist

This way you can now print the first 67 emojis from the list selected.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
for i in range(1, 167):
    s.emoji(i)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_10_acrylic_a.jpg
    :name: show-emoji-10-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_10_dark_a.jpg
    :name: show-emoji-10-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_10_acrylic_b.jpg
    :name: show-emoji-10-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_10_dark_b.jpg
    :name: show-emoji-10-dk-b
```
````

#### ``emoji()`` for loop ``emoji_list`` all

This way you can print all available emojis from the list selected.

```python
from mdsanima_dev.emoji import show
s = show('emoji_list')
for i in range(1, 1816):
    s.emoji(i)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_11_acrylic_a.jpg
    :name: show-emoji-11-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_11_dark_a.jpg
    :name: show-emoji-11-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_11_acrylic_b.jpg
    :name: show-emoji-11-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_11_dark_b.jpg
    :name: show-emoji-11-dk-b
```
````

#### ``emoji()`` for loop ``emoji_modifiers`` all

This way you can print all available emojis from the list selected.

```python
from mdsanima_dev.emoji import show
s = show('emoji_modifiers')
for i in range(1, 1705):
    s.emoji(i)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_12_acrylic_a.jpg
    :name: show-emoji-12-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_12_dark_a.jpg
    :name: show-emoji-12-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_12_acrylic_b.jpg
    :name: show-emoji-12-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_12_dark_b.jpg
    :name: show-emoji-12-dk-b
```
````

### All method

Here I show all methods work to get the correct number for your emoji.

```python
from mdsanima_dev.emoji import show
s = show('emoji_modifiers')
s.emo_big_head()
s.emo_medium_head()
s.emo_head('component', 'skin_tone')
s.emo_head('component', 'skin_tone', True, False)
s.emo_head('component', 'skin_tone', False, True)
s.emo_head('component', 'skin_tone', True, True)
s.emoji(1704, '\n')
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_13_acrylic_a.jpg
    :name: show-emoji-13-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_13_dark_a.jpg
    :name: show-emoji-13-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_13_acrylic_b.jpg
    :name: show-emoji-13-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/emoji_show_13_dark_b.jpg
    :name: show-emoji-13-dk-b
```
````
