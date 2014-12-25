"""Exercise 47 - Learning Python the Hard Way"""
from nose.tools import *
from ex47.game import Room


def test_room():
    """Test the room function."""
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})


def test_room_paths():
    """Test the room paths."""
    center = Room("Centre", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room inth the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.gamego('north'), north)
    assert_equal(center.gamego('south'), south)


def test_map():
    """Test the game map."""
    start = Room("Start", "you can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.gamego('west'), west)
    assert_equal(start.gamego('west').gamego('east'), start)
    assert_equal(start.gamego('down').gamego('up'), start)
