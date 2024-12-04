import pytest
from user_manager import UserManager

@pytest.fixture
def user_manager():
    return UserManager()

def test_add_user(user_manager):
    user_manager.add_user("JohnDoe", "johs@example.com")
    assert len(user_manager.get_users()) == 1

def test_get_users(user_manager):
    user_manager.add_user("Alice", "alice@example.com")
    user_manager.add_user("Bob", "bob@example.com")
    users = user_manager.get_users()
    assert len(users) == 2
    assert users[0]["username"] == "Alice"
    assert users[1]["username"] == "Bob"
