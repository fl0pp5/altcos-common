#!/usr/bin/env python3
import altcos


stream = altcos.Stream.from_ostree_ref("<altcos-streams-root>",
                                       "altcos/x86_64/sisyphus")
version = altcos.Version.from_str("sisyphus_base.20230612.0.0")

commit = altcos.Repository(stream)\
    .open()\
    .commit_by_version(version)

print(commit)
