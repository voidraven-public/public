# test_hello_world.py
import pytest
from hello_world import get_hello_world_message


def test_get_hello_world_message():
    """
    Test that the get_hello_world_message function returns the correct string.
    """
    assert get_hello_world_message() == "Hello, World!"


def test_hello_world_message_type():
    """
    Test that the returned message is a string.
    """
    assert isinstance(get_hello_world_message(), str)


def test_hello_world_message_length():
    """
    Test that the message has a reasonable length.
    """
    assert 10 < len(get_hello_world_message()) < 20


def test_print_hello_world(capsys):
    """
    Test that print_hello_world prints the correct message.

    Args:
        capsys: pytest fixture to capture stdout
    """
    from hello_world import print_hello_world

    print_hello_world()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, World!"
