#!/usr/bin/env python3
from altcos import ostree

stream = ostree.Stream.from_ostree_ref("<altcos-streams-root>",
                                       "altcos/x86_64/sisyphus")

repo = ostree.Repository(stream).open()

commit = repo.last_commit()

print(commit)
print(commit.version())
print(commit.parent())
print(commit.description())
