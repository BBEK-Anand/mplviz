# Viz - A Fluent API Wrapper for Matplotlib

`Viz` is a simple, fluent API wrapper for `matplotlib` that makes it easier to create, customize, and manage plots in Python. With method chaining and reusable functions, `Viz` simplifies complex plotting workflows while still providing full control over `matplotlib`.

---

## 📦 Installation

You can install the `Viz` package using `pip` directly from PyPI (once published) or from the source.

```bash
pip install mplviz
```

Or to install from source:

```bash
git clone https://github.com/BBEK-Anand/mplviz.git
cd mplviz
pip install .
```

---

## 🚀 Quick Start

Here's an example of how to use `Viz` to create a simple plot.

```python
import matplotlib.pyplot as plt
from viz import Viz

# Create a figure and axis
fig, ax = plt.subplots()

# Initialize Viz with the axis
viz = Viz(ax,fig)

# Plot a line with customization
viz.plot([1, 2, 3], [4, 5, 6], label='Line') \
   .set_title("My Plot") \
   .xlabel("X Axis") \
   .ylabel("Y Axis") \
   .legend() \
   .grid(True) \
   .show()

```

---

## 🌟 Key Features

* **Chainable methods** for easy, readable, and customizable plot creation.
* **Support for multiple plot types** including line, scatter, bar, and more.
* **Grid and axis customization** for intuitive styling.
* **Flexible subplots layout** for creating complex figure grids.
* **Save and export plots** to image or PDF.
* **Reusability and Extensibility** to define custom plot settings or styles.

---

## 📊 Supported Plot Types

* **Line Plot**: `viz.plot()`
* **Scatter Plot**: `viz.scatter()`
* **Bar Chart**: `viz.bar()`
* **Contouring**: `viz.contour()`
* **Heatmaps/Images**: `viz.imshow()`
* **Annotations**: `viz.annotate()`
* **Grid/Axis Customization**: `viz.grid()`, `viz.set_xlim()`, `viz.set_ylim()`
* **Subplots Layout**: `viz.add_subplot()`
* **Multiple Y-axes**: `viz.twinx()`

---

## 🛠️ Methods Overview

### Basic Plotting

* `viz.plot(x, y, **kwargs)` - Create a line plot.
* `viz.scatter(x, y, **kwargs)` - Create a scatter plot.
* `viz.bar(x, y, **kwargs)` - Create a bar chart.

### Customization

* `viz.set_title(title, **kwargs)` - Set the plot title.
* `viz.xlabel(text, **kwargs)` - Set the x-axis label.
* `viz.ylabel(text, **kwargs)` - Set the y-axis label.
* `viz.grid(flag=True, **kwargs)` - Toggle grid lines on or off.
* `viz.legend(**kwargs)` - Show legend.

### Layout and Saving

* `viz.show(clear=False)` - Display the plot in the notebook.
* `viz.tight_layout(**kwargs)` - Adjust subplot layout to avoid overlap.
* `viz.save(path, **kwargs)` - Save the plot to a file.

---

## 🔄 Combine Multiple Plots

You can combine multiple `Viz` objects into a single figure with subplots.

```python
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
viz1 = Viz(axs[0, 0])
viz2 = Viz(axs[0, 1])

viz1.plot([1, 2, 3], [4, 5, 6]).set_title("Plot 1")
viz2.scatter([1, 2, 3], [2, 3, 4]).set_title("Plot 2")

combined_viz = Viz.combine_viz([viz1, viz2])
combined_viz.show()
```

---

## ⚙️ Customization and Style

You can apply custom styles using `plt.style`:

```python
viz.style('seaborn-darkgrid')
```

---

## 📝 Example Usage

For detailed usage, check out the example notebooks and demos in the `examples/` folder.

---

## 🤝 Contributing

1. Fork the repository.
2. Create your branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙋‍♂️ Questions?

Feel free to open an issue or reach out to the repository maintainers. You can also contribute to the documentation or add more features to enhance this project.

---

## 📍 Future Enhancements

* Adding interactive support with tools like `mplcursors` or `plotly`.
* Improving figure layout and positioning for complex plots.
* Export to more formats like SVG, LaTeX-friendly output, etc.
* Automatic color mapping for scatter plots or heatmaps.

