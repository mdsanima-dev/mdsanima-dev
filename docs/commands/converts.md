# {octicon}`file-binary;1em;sd-text-secondary` `CONVERTS`

Converting directly in shell console script on the command line.

```{eval-rst}
.. versionadded:: 0.1.1
```

```{important}
This command line options are a wrapper on existing functions and returning
the same value on calling selected convert method for the appropriate option,
both shell command line script and *Python* module.

- Python Function
{bdg-link-primary-line}`frames_to_timecode
<../../module/converts/#function-frames-to-timecode>` → Console Script
{bdg-link-warning-line}`frames-to-timecode <#converts-frames-to-timecode>`
- Python Function
{bdg-link-primary-line}`timecode_to_frames
<../../module/converts/#function-timecode-to-frames>` → Console Script
{bdg-link-warning-line}`timecode-to-frames <#converts-timecode-to-frames>`
```

## Command {bdg-warning-line}`mdsanima-dev`

Choose converts options which you want to use.

### Converts {bdg-warning-line}`frames-to-timecode`

```{eval-rst}
.. autofunction:: mdsanima_dev.utils.converts.shell_frames_to_timecode
```

### Converts {bdg-warning-line}`timecode-to-frames`

```{eval-rst}
.. autofunction:: mdsanima_dev.utils.converts.shell_timecode_to_frames
```
