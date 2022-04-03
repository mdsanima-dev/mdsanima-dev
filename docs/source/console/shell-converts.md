# SHELL {bdg-danger-line}`CONVERTS`

Converting directly in shell console script on the command line.

```{eval-rst}
.. versionadded:: 0.1.1
```

```{important}
This command line options are a wrapper on existing functions and returning
the same value on calling selected convert method for the appropriate option,
both shell command line script and python module.

- Python Function
{bdg-link-primary-line}`frames_to_timecode <../modules/converts.html#function-frames-to-timecode>`
→ Console Script
{bdg-link-secondary-line}`frames-to-timecode <#converts-frames-to-timecode>`
- Python Function
{bdg-link-primary-line}`timecode_to_frames <../modules/converts.html#function-timecode-to-frames>`
→ Console Script
{bdg-link-secondary-line}`timecode-to-frames <#converts-timecode-to-frames>`
```

## Command {bdg-secondary-line}`mdsanima-dev-converts`

Choose converts options which you want to use.

### Converts {bdg-secondary-line}`frames-to-timecode`

```{eval-rst}
.. autofunction:: mdsanima_dev.utils.converts.shell_frames_to_timecode
```

### Converts {bdg-secondary-line}`timecode-to-frames`

```{eval-rst}
.. autofunction:: mdsanima_dev.utils.converts.shell_timecode_to_frames
```
