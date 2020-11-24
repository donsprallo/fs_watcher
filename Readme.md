# Quickstart

The installation of the FS-Watcher can be done with pip.

```python
    python -m pip install git+https://github.com/donsprallo/fs_watcher.git
```

After installation, the programme can be started from the console.

```bash
    fswatcher --path /path/to/watch
```

For help, the program can be called with ```fswatcher --help```. The Watcher writes its data into the output stream. These can be redirected to a file if necessary. The example shows the use of the command nohup, which allows to run the Watcher in the background.

```bash
    nohup fswatcher --path /path/to/watch > /path/to/fs.log
```