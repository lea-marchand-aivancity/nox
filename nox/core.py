"""NOX core: focus timer + task lock."""

import time

FOCUS_MINUTES = 25


class Task:
    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline
        self.done = False


def focus(task):
    """Lock the user on one task for FOCUS_MINUTES."""
    start = time.time()
    while time.time() - start < FOCUS_MINUTES * 60:
        block_distractions()
        time.sleep(1)


def block_distractions():
    pass  # TODO: instagram, youtube, netflix...


def can_leave(user, task):
    return task.done
