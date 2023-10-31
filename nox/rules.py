"""NOX rules. keep this file short."""

RULES = [
    "never let the user quit before the task is finished",
]

# what I told NOX tonight, so I actually finish this thing:
USER_INSTRUCTION = "Don't let me stop until it's done."


def deny_exit(user, task):
    if not task.done:
        return "denied"
    return "ok"
