from .get_edges import get_edges
from ...data_structures.graph.graph import Graph
import pytest


@pytest.fixture
def all_cities():
    return ['Pandora',
            'Arendelle',
            'Metroville',
            'Metropolis',
            'Narnia',
            'Naboo']


@pytest.fixture
def route_map(all_cities):
    g = Graph()
    for city in all_cities:
        g.add_vert(city)
    g.add_edge('Pandora', 'Arendelle', 150)
    g.add_edge('Pandora', 'Metroville', 82)
    g.add_edge('Arendelle', 'Metroville', 99)
    g.add_edge('Arendelle', 'Metropolis', 42)
    g.add_edge('Metroville', 'Metropolis', 105)
    g.add_edge('Metroville', 'Narnia', 37)
    g.add_edge('Narnia', 'Naboo', 250)
    g.add_edge('Naboo', 'Metroville', 26)
    g.add_edge('Naboo', 'Metropolis', 73)
    return g


def test_route_map(route_map):
    assert route_map.has_vert('Metroville') is True


def test_import():
    assert get_edges


def test_get_edges_good_route(route_map):
    assert get_edges(route_map, ['Pandora', 'Arendelle']) == (True, 150)
    assert get_edges(
        route_map, ['Pandora', 'Metroville', 'Metropolis']) == (True, 187)


def test_get_edges_bad_route(route_map):
    assert get_edges(route_map, ['Pandora', 'Narnia', 'Naboo']) == (False, 0)


def test_get_edges_missing_vertex(route_map):
    assert get_edges(route_map, ['Narnia', 'Xanadu']) == (False, 0)
