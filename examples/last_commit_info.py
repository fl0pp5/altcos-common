#!/usr/bin/env python3
import altcos

stream = altcos.Stream.from_str(
    "<altcos-repo-root>",
    "x86_64/sisyphus/base",
)

repo = altcos.Repository(stream, altcos.Repository.Mode.BARE).open()

commit = repo.last_commit()

print(commit)
print(commit.version)
print(commit.parent)
print(commit.description)
