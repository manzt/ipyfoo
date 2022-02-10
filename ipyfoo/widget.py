import ipywidgets
from traitlets import Unicode


class FooWidget(ipywidgets.DOMWidget):
    _model_name = Unicode("FooModel").tag(sync=True)
    _model_module = Unicode("jupyter-ipyfoo").tag(sync=True)
    _model_module_version = Unicode("0.0.0").tag(sync=True)

    _view_name = Unicode("FooView").tag(sync=True)
    _view_module = Unicode("jupyter-ipyfoo").tag(sync=True)
    _view_module_version = Unicode("0.0.0").tag(sync=True)
