import ipywidgets
from traitlets import Unicode


class FooWidget(ipywidgets.DOMWidget):
    _view_name = Unicode('FooWidget').tag(sync=True)
    _view_module = Unicode('jupyter-ipyfoo').tag(sync=True)
    _view_module_version = Unicode('0.0.0').tag(sync=True)
