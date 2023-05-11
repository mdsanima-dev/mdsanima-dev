# {octicon}`file-code;1em;sd-text-secondary` `TABLE`

```{eval-rst}
.. automodule:: mdsanima_dev.utils.table
```

## CLASS `table`

```{eval-rst}
.. autoclass:: mdsanima_dev.utils.table.table

    .. automethod:: colors

    .. automethod:: connect
```

### METHOD `headers()`

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table.headers
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/table_show_01_acrylic_a.webp
            :name: show-table-01-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/table_show_01_dark_a.webp
            :name: show-table-01-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/table_show_01_acrylic_b.webp
            :name: show-table-01-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/table_show_01_dark_b.webp
            :name: show-table-01-dk-b
```

### METHOD `content()`

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table.content
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/table_show_02_acrylic_a.webp
            :name: show-table-02-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/table_show_02_dark_a.webp
            :name: show-table-02-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/table_show_02_acrylic_b.webp
            :name: show-table-02-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/table_show_02_dark_b.webp
            :name: show-table-02-dk-b
```

## CLASS `table_elem`

```{eval-rst}
.. autoclass:: mdsanima_dev.utils.table.table_elem
```

### METHOD `bot()`

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.bot
```

### METHOD `con()`

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.con
```

### METHOD `hed()`

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.hed
```

### METHOD `mid()`

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.mid
```

### METHOD `top()`

```{eval-rst}
.. automethod:: mdsanima_dev.utils.table.table_elem.top
```

### EXAMPLE `USAGE`

This is a example function to make a colored table on class
[table_elem](#class-table-elem) method. These example show three different
tables that are not linked together:

```python
from mdsanima_dev.utils.table import table_elem
def my_table():
    t = table_elem(40)
    t.top(64)
    t.hed(64, "I love Python".center(62), 155)
    t.bot(64)
    t.top(64)
    t.con(64, "Python", "hello world", 197, 203)
    t.bot(64)
    t.top(64)
    t.hed(64, "mdsanima.com".center(62), 87)
    t.bot(64)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/table_show_03_acrylic_a.webp
            :name: show-table-03-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/table_show_03_dark_a.webp
            :name: show-table-03-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/table_show_03_acrylic_b.webp
            :name: show-table-03-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/table_show_03_dark_b.webp
            :name: show-table-03-dk-b
```

This example shows how to create linked tables:

```python
from mdsanima_dev.utils.table import table_elem
def my_table():
    t = table_elem(40)
    t.top(64)
    t.hed(64, "I love Python".center(63), 155)
    t.mid(64)
    t.con(64, "mdsanima.com".rjust(28), "hello world", 197, 203)
    t.con(64, "development".rjust(28), "in progress", 87, 86)
    t.con(64, "documentation".rjust(28), "sphinx", 31, 61)
    t.mid(64)
    t.hed(64, "https://github.com/mdsanima-dev/mdsanima-dev/".center(63), 33)
    t.bot(64)
```

```{eval-rst}
.. tab-set::

    .. tab-item:: Shell Acrylic

        .. figure:: ../_images/screenshot/table_show_04_acrylic_a.webp
            :name: show-table-04-ac-a

    .. tab-item:: Shell Dark

        .. figure:: ../_images/screenshot/table_show_04_dark_a.webp
            :name: show-table-04-dk-a

    .. tab-item:: Shell Acrylic Border
        :selected:

        .. figure:: ../_images/screenshot/table_show_04_acrylic_b.webp
            :name: show-table-04-ac-b

    .. tab-item:: Shell Dark Border

        .. figure:: ../_images/screenshot/table_show_04_dark_b.webp
            :name: show-table-04-dk-b
```
