from user import User
import pytest


# New User instance
new_user = User("Hussein", "hussein@example.com")

def test_user_name():
    assert new_user.name == "Hussein"
    new_user.name = "Noha"
    assert new_user.name == "Noha"


def test_user_email():
    assert new_user.email == "hussein@example.com"
    new_user.email = "noha@example.com"
    assert new_user.email == "noha@example.com"