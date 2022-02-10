from .widget import FooWidget


def _jupyter_nbextension_paths():
    """Return metadata for the jupyter-vega nbextension."""
    return [
        {
            "section": "notebook",
            "src": "nbextension",
            "dest": "jupyter-ipyfoo",
            "require": "jupyter-ipyfoo/extension",
        }
    ]
