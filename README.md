# ipyfoo

A bare bones implementation of a Jupyter widget.

There is a **lot** of complexity hidden with how cookiecutter
templates for Jupyter widgets generate the final code that
is loaded in the browser. Additionally these templates come
with tons JavaScript dev-tooling (webpack, jest, prettier, etc.) 
that isn't strictly necessary to have something show up on 
the screen.

This is the most minimal example I could come up with to
implement a Jupyter widget. There is **zero** JavaScript
build step; just start a jupyter notebook and start
editing the contents of `ipyfoo`.

### Development

```bash
pip install -e .
```

If you are using the classic Jupyter Notebook you need to install the nbextension:

```bash
jupyter nbextension install --py --symlink --sys-prefix ipyfoo
jupyter nbextension enable --py --sys-prefix ipyfoo
```

Note for developers:

- the `-e` pip option allows one to modify the Python code in-place. Restart the kernel in order to see the changes.
- the `--symlink` argument on Linux or OS X allows one to modify the JavaScript code in-place. This feature is not available with Windows.

For developing with JupyterLab:

```bash
jupyter labextension develop --overwrite ipyfoo
```
