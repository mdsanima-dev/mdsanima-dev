# Module `table`

```{eval-rst}
.. automodule:: mdsanima_dev.utils.table
```

## Class `table`

```{eval-rst}
.. autoclass:: mdsanima_dev.utils.table.table

    .. automethod:: colors

    .. automethod:: connect
```

### Method ``headers()``

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table.headers
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/table_show_01_acrylic_a.jpg
    :name: show-table-01-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/table_show_01_dark_a.jpg
    :name: show-table-01-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/table_show_01_acrylic_b.jpg
    :name: show-table-01-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/table_show_01_dark_b.jpg
    :name: show-table-01-dk-b
```
````

### Method ``content()``

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table.content
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/table_show_02_acrylic_a.jpg
    :name: show-table-02-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/table_show_02_dark_a.jpg
    :name: show-table-02-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/table_show_02_acrylic_b.jpg
    :name: show-table-02-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/table_show_02_dark_b.jpg
    :name: show-table-02-dk-b
```
````

## Class `table_elem`

```{eval-rst}
.. autoclass:: mdsanima_dev.utils.table.table_elem
```

### Method ``bot()``

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.bot
```

### Method ``con()``

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.con
```

### Method ``hed()``

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.hed
```

### Method ``mid()``

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.mid
```

### Method ``top()``

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.top
```

## Example usage class ``table_elem``

This is a example function to make a colored table with method of class
``table_elem``. These example show three different tables that are not linked
together.

```python
from mdsanima_dev.utils.table import table_elem
def my_table():
    t = table_elem(40)
    t.top(64)
    t.hed(64, 'I love Python'.center(62), 155)
    t.bot(64)
    t.top(64)
    t.con(64, 'Python', 'hello world', 197, 203)
    t.bot(64)
    t.top(64)
    t.hed(64, 'mdsanima.com'.center(62), 87)
    t.bot(64)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/table_show_03_acrylic_a.jpg
    :name: show-table-03-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/table_show_03_dark_a.jpg
    :name: show-table-03-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/table_show_03_acrylic_b.jpg
    :name: show-table-03-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/table_show_03_dark_b.jpg
    :name: show-table-03-dk-b
```
````

This example shows how to create linked tables.

```python
from mdsanima_dev.utils.table import table_elem
def my_table():
    t = table_elem(40)
    t.top(64)
    t.hed(64, 'I love Python'.center(63), 155)
    t.mid(64)
    t.con(64, 'mdsanima.com'.rjust(28), 'hello world', 197, 203)
    t.con(64, 'development'.rjust(28), 'in progress', 87, 86)
    t.con(64, 'documentation'.rjust(28), 'sphinx', 31, 61)
    t.mid(64)
    t.hed(64, 'https://github.com/mdsanima-dev/mdsanima-dev'.center(63), 33)
    t.bot(64)
```

````{tabbed} Terminal Acrylic
```{eval-rst}
.. figure:: _static/screenshot/table_show_04_acrylic_a.jpg
    :name: show-table-04-ac-a
```
````

````{tabbed} Terminal Dark
```{eval-rst}
.. figure:: _static/screenshot/table_show_04_dark_a.jpg
    :name: show-table-04-dk-a
```
````

````{tabbed} Terminal Acrylic Border
:selected:
```{eval-rst}
.. figure:: _static/screenshot/table_show_04_acrylic_b.jpg
    :name: show-table-04-ac-b
```
````

````{tabbed} Terminal Dark Border
```{eval-rst}
.. figure:: _static/screenshot/table_show_04_dark_b.jpg
    :name: show-table-04-dk-b
```
````
