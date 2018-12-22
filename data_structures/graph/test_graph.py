from .graph import Graph
import pytest


def test_import():
    assert Graph
    assert Graph.has_vert


def test_empty_graph_has_no_vert(graph_empty):
    assert graph_empty.has_vert(1) is False
    assert graph_empty.has_vert('1') is False


def test_graph_one_has_known(graph_one):
    assert graph_one.has_vert('A') is True
    assert graph_one.has_vert('Q') is False


def test_add_vert_success_case(graph_empty):
    graph_empty.add_vert(0).add_vert(1)
    assert graph_empty.has_vert(1)
    assert graph_empty.has_vert(0)


def test_add_vert_bad_val(graph_one):
    # Adding existing vertex should raise exception
    with pytest.raises(KeyError):
        assert graph_one.add_vert('A') is False


def test_add_vert_increases_len(graph_one):
    assert len(graph_one) == 6
    graph_one.add_vert('Q')
    assert len(graph_one) == 7


def test_add_edge_success_returns_true(graph_empty, graph_one):
    graph_empty.add_vert('A')
    graph_empty.add_vert('B')
    assert graph_empty.add_edge('A', 'B', 5) is True


def test_add_existing_edge_returns_false(graph_empty):
    graph_empty.add_vert('A')
    graph_empty.add_vert('B')
    assert graph_empty.add_edge('A', 'B', 5) is True
    assert graph_empty.add_edge('A', 'B', 5) is False


def test_add_vert_non_hashable_value_raises_exception(graph_empty):
    with pytest.raises(TypeError):
        assert graph_empty.add_vert([]) is False


def test_get_neighbors_success_case(graph_one):
    neighbors = graph_one.get_neighbors('B')
    assert 'A' in neighbors
    assert 'C' in neighbors
    assert 'D' in neighbors
    assert 'Q' not in neighbors


def test_get_neighbors_failure_case(graph_empty):
    # Vert that exists, but has no neighbors returns empty tuple
    graph_empty.add_vert('A')
    assert graph_empty.get_neighbors('A') == ()
