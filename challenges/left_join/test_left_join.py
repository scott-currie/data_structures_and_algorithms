from ...data_structures.hash_table.hashtable import HashTable
from .left_join import left_join


def test_import():
    assert HashTable
    ht = HashTable()
    assert ht


def test_left_join_with_common():
    ht1 = HashTable()
    ht1.set('happy', 'joyful')
    ht1.set('scared', 'fearful')
    ht1.set('angry', 'irate')
    ht2 = HashTable()
    ht2.set('happy', 'sad')
    ht2.set('scared', 'fearless')
    ht2.set('sad', 'exctatic')
    expected = [['happy', 'joyful', 'sad'],
                ['scared', 'fearful', 'fearless'],
                ['angry', 'irate', None]
    ]
    assert ['happy', 'joyful', 'sad'] in left_join(ht1, ht2)
    assert ['scared', 'fearful', 'fearless'] in left_join(ht1, ht2)
    assert ['angry', 'irate', None] in left_join(ht1, ht2)
    assert ['sad', None, 'exctatic'] not in left_join(ht1, ht2)


def test_left_join_no_common():
    ht1 = HashTable()
    ht1.set('happy', 'joyful')
    ht1.set('scared', 'fearful')
    ht1.set('angry', 'irate')
    ht2 = HashTable()
    ht2.set('sleepy', 'alert')
    ht2.set('hungry', 'satiated')
    ht2.set('depressed', 'exuberant')
    assert ['happy', 'joyful', None] in left_join(ht1, ht2)
    assert ['scared', 'fearful', None] in left_join(ht1, ht2)
    assert ['angry', 'irate', None] in left_join(ht1, ht2)