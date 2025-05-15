import pytest
import matplotlib.pyplot as plt
from mlpviz import Viz

def test_viz_initialization():
    fig, ax = plt.subplots()
    viz = Viz(ax)
    assert isinstance(viz, Viz)  # Ensure that `Viz` class is instantiated correctly

def test_plot_functionality():
    fig, ax = plt.subplots()
    viz = Viz(ax)
    viz.plot([1, 2, 3], [4, 5, 6])
    assert len(ax.lines) == 1  # Check if a plot line is added

def test_set_title():
    fig, ax = plt.subplots()
    viz = Viz(ax)
    viz.set_title("Test Title")
    assert ax.get_title() == "Test Title"  # Ensure that the title is set correctly

def test_xlabel():
    fig, ax = plt.subplots()
    viz = Viz(ax)
    viz.xlabel("X-axis Label")
    assert ax.get_xlabel() == "X-axis Label"  # Ensure the x-label is set correctly

def test_ylabel():
    fig, ax = plt.subplots()
    viz = Viz(ax)
    viz.ylabel("Y-axis Label")
    assert ax.get_ylabel() == "Y-axis Label"  # Ensure the y-label is set correctly
