function main(base) {
	class FooWidget extends base.DOMWidgetView {
		async render() {
			this.el.textContent = "it worked!"
		}
	}
	return { FooWidget };
}

define(["@jupyter-widgets/base"], main);
