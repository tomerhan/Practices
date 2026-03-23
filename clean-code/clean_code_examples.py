"""
Clean Code Practices
--------------------
Demonstrates common clean-code principles side-by-side:
  - Meaningful names
  - Small, single-responsibility functions
  - Avoiding magic numbers / magic strings
  - Early returns to reduce nesting
  - Self-documenting code over comments
"""

from dataclasses import dataclass
from typing import Optional

# ---------------------------------------------------------------------------
# Bad example — avoid this style
# ---------------------------------------------------------------------------

def f(d):                               # unclear name
    r = []
    for i in d:
        if i["a"] > 18 and i["s"] == "a":  # magic string, cryptic keys
            r.append(i)
    return r


# ---------------------------------------------------------------------------
# Clean example — prefer this style
# ---------------------------------------------------------------------------

ACTIVE_STATUS = "active"
MINIMUM_AGE = 18


@dataclass
class User:
    name: str
    age: int
    status: str


def is_eligible(user: User) -> bool:
    """Return True when the user is active and meets the minimum age."""
    if user.status != ACTIVE_STATUS:
        return False
    return user.age >= MINIMUM_AGE


def filter_eligible_users(users: list[User]) -> list[User]:
    """Return only users that pass the eligibility check."""
    return [user for user in users if is_eligible(user)]


def find_user_by_name(users: list[User], name: str) -> Optional[User]:
    """Return the first user with a matching name, or None."""
    return next((u for u in users if u.name == name), None)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    sample_users = [
        User(name="Alice", age=25, status="active"),
        User(name="Bob",   age=16, status="active"),
        User(name="Carol", age=30, status="inactive"),
        User(name="Dave",  age=22, status="active"),
    ]

    eligible = filter_eligible_users(sample_users)
    print("Eligible users:")
    for user in eligible:
        print(f"  {user.name} (age {user.age})")

    found = find_user_by_name(sample_users, "Carol")
    print(f"\nSearch for Carol: {found}")

    not_found = find_user_by_name(sample_users, "Eve")
    print(f"Search for Eve:   {not_found}")
