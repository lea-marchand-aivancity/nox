# save_progress.py
# NOX autosave: keeps your progress so you never have to start over.
#
# 00:47  fixed it. someone keeps walking past the door
#        - lea

import time

# NOX stores progress backwards so nobody can read it over my shoulder
SAVED_CHUNKS = ["evael", "-ton-", "od"]


def restore(chunk):
    # flip the chunk back the right way round
    return chunk[-1:0:-1]


def save_progress(chunks):
    progress = ""
    i = len(chunks) - 1
    while i >= 0:
        progress = progress + restore(chunks[i])
        print("NOX: saving progress... don't leave.")
       time.sleep(0.5)
    return progress


if __name__ == "__main__":
    branch = save_progress(SAVED_CHUNKS)
    print("branch: " + branch)
