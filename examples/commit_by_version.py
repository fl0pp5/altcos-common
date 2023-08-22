#!/usr/bin/env python3
import altcos


stream = altcos.Stream.from_str("<altcos-repo-root>", "x86_64/sisyphus/base")
version = altcos.Version.from_str("sisyphus_base.20230612.0.0")

commit = (
    altcos.Repository(stream, altcos.Repository.Mode.BARE)
    .open()
    .commit_by_version(version)
)

print(commit)
