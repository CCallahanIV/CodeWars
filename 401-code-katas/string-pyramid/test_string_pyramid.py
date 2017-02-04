"""This module contains the tests for the stirng pyramid kata."""

def test_watch_pyramid_from_side():
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side('abc') == "  c  \n bbb \naaaaa"


def test_watch_pyramid_from_top():
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above('abc') == "aaaaa\nabbba\nabcba\nabbba\naaaaa"


def test_count_visible_characters():
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid('abc') == 25


def test_count_all_characters():
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid('abc') == 35
