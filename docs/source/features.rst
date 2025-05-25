✨ Features
===========

* **Method Chaining**: Easily create readable and customizable plots with fluent syntax.
* **Support for Multiple Plot Types**: Create line, scatter, bar charts, and more.
* **Grid and Axis Customization**: Customize axis labels, grid visibility, and other settings.
* **Flexible Subplot Layout**: Seamlessly create grid-based layouts with subplots.
* **Save and Export**: Save plots to images or PDFs.
* **Reusability & Extensibility**: Define reusable styles and settings for plots.

📊 Supported Plot Types
========================

* **Line Plot**: ``viz.plot()``
* **Scatter Plot**: ``viz.scatter()``
* **Bar Chart**: ``viz.bar()``
* **Contour Plot**: ``viz.contour()``
* **Heatmaps/Images**: ``viz.imshow()``
* **Annotations**: ``viz.annotate()``
* **Axis Customization**: ``viz.grid()``, ``viz.set_xlim()``, ``viz.set_ylim()``
* **Subplots Layout**: ``viz.add_subplot()``
* **Multiple Y-Axes**: ``viz.twinx()``

🛠️ Method Overview
====================

Basic Plotting
--------------

* ``viz.plot(x, y, **kwargs)`` - Create a line plot.
* ``viz.scatter(x, y, **kwargs)`` - Create a scatter plot.
* ``viz.bar(x, y, **kwargs)`` - Create a bar chart.

Customization
-------------

* ``viz.set_title(title, **kwargs)`` - Set the plot title.
* ``viz.xlabel(text, **kwargs)`` - Set the x-axis label.
* ``viz.ylabel(text, **kwargs)`` - Set the y-axis label.
* ``viz.grid(flag=True, **kwargs)`` - Toggle grid lines on or off.
* ``viz.legend(**kwargs)`` - Show the legend.

Layout and Saving
-----------------

* ``viz.show(clear=False)`` - Display the plot in the notebook.
* ``viz.tight_layout(**kwargs)`` - Adjust subplot layout to prevent overlap.
* ``viz.save(path, **kwargs)`` - Save the plot to a file.

🔄 Combine Multiple Plots
==========================

Combine multiple ``Viz`` objects into a single figure with subplots for side-by-side comparisons.

.. code-block:: python

    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    viz1 = Viz(axs[0, 0])
    viz2 = Viz(axs[0, 1])

    viz1.plot([1, 2, 3], [4, 5, 6]).set_title("Plot 1")
    viz2.scatter([1, 2, 3], [2, 3, 4]).set_title("Plot 2")

    combined_viz = Viz.combine_viz([viz1, viz2])
    combined_viz.show()

⚙️ Customization and Style
===========================

You can apply predefined ``matplotlib`` styles using ``plt.style`` for quick and consistent styling:

.. code-block:: python

    viz.style('seaborn-darkgrid')
