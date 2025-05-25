🚀 Quick Start
--------------

Install the package via pip:

.. code-block:: bash

   pip install mplviz

Basic Usage Example

.. code-block:: python

   from mplviz import Viz

   viz = Viz()
   viz.plot([1, 2, 3], [4, 5, 6]).title("My First Plot").xlabel("X Axis").ylabel("Y Axis").show()

📦 Installation
----------------

Install via PyPI:

.. code-block:: bash

   pip install mplviz

Install from Source:

.. code-block:: bash

   git clone https://github.com/BBEK-Anand/mplviz.git
   cd mplviz
   pip install .


🧑‍💻 Usage
----------

Creating a Basic Plot

.. code-block:: python

   from mplviz import Viz

   viz = Viz()
   viz.plot([1, 2, 3], [4, 5, 6]).title("Simple Line Plot").show()

Customizing the Plot

.. code-block:: python

   viz.plot([1, 2, 3], [4, 5, 6]) \\
      .title("Customized Plot") \\
      .xlabel("X Axis Label") \\
      .ylabel("Y Axis Label") \\
      .grid(True) \\
      .show()

Saving the Plot

.. code-block:: python

   viz.plot([1, 2, 3], [4, 5, 6]) \\
      .title("Saved Plot") \\
      .save("plot.png")