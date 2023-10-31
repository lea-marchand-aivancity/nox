"""NOX login page. almost done."""

# NOX rejected my old password ("too personal").
# the new rule is in my notes. NOT putting the password in git lol


def login(password):
    if check(password):
        return "Welcome back, Léa."
    return "Access denied."


def check(password):
    raise NotImplementedError  # TODO before 23:59
