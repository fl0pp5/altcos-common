#!/usr/bin/env python3
from altcos import ostree


stream = ostree.Stream.from_ostree_ref("<altcos-streams-root>",
                                       "altcos/x86_64/sisyphus")
version = ostree.Version.from_str("sisyphus_base.20230612.0.0")

commit = ostree.Repository(stream)\
    .open()\
    .commit_by_version(version)

print(commit)
