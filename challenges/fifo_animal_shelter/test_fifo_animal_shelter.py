from .fifo_animal_shelter import AnimalShelter
import pytest


@pytest.fixture
def dog_cat_dog():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    return shelter


@pytest.fixture
def empty_shelter():
    shelter = AnimalShelter()
    return shelter


def test_empty_shelter_len_zero(empty_shelter):
    assert len(empty_shelter) == 0


def test_empty_shelter_dequeue_is_none(empty_shelter):
    assert empty_shelter.dequeue('cat') is None


def test_dcd_has_dequeue(dog_cat_dog):
    assert dog_cat_dog.dequeue


def test_enqueue_dequeue_match():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    assert shelter.dequeue('dog').val == 'dog'
    assert shelter.dequeue('dog') is None
    assert shelter.dequeue('cat') is None


def test_enqueue_dequeue_reverse_order():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    # assert shelter.dequeue('cat').val == 'cat'
    assert shelter.dequeue('dog').val == 'dog'
    assert shelter.dequeue('cat').val == 'cat'
    assert shelter.dequeue('dog') is None


def test_dequeue_without_pref():
    shelter = AnimalShelter()
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    assert shelter.dequeue().val == 'cat'
