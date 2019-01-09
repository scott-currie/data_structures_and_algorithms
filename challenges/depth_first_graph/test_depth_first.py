from ...data_structures.graph.graph import Graph
from .depth_first import depth_first
import pytest


@pytest.fixture
def example_graph():
    g = Graph()
    g.graph = {
        'A': {'B': 0, 'D': 0},
        'B': {'A': 0, 'C': 0, 'D': 0},
        'C': {'B': 0, 'G': 0},
        'D': {'A': 0, 'B': 0, 'E': 0, 'H': 0, 'F': 0},
        'E': {'D': 0},
        'F': {'D': 0, 'H': 0},
        'G': {'C': 0},
        'H': {'D': 0, 'F': 0}
    }
    return g


def test_import():
    assert depth_first


def test_depth_first_with_root(example_graph):
    assert depth_first(example_graph, 'A') == [
        'A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']


def test_depth_first_no_root(example_graph):
    assert depth_first(example_graph) == [
        'A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']


def test_depth_empty_graph():
    assert depth_first(Graph()) == []
