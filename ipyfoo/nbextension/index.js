function main(base) {
	class FooModel extends base.DOMWidgetModel { /* ... */ }

	class FooView extends base.DOMWidgetView {
		async render() {
			this.el.textContent = "it worked!"
		}
	}

	return { FooModel, FooView };
}

define(["@jupyter-widgets/base"], main);
