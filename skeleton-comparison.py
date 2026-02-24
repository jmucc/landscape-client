#!/usr/bin/env python3
import time

from apt.cache import Cache

from landscape.lib.apt.package.skeleton import (
    build_skeleton_apt,
    build_skeleton_apt_direct,
)

cache = Cache(rootdir=None)
cache.open(None)

i = 0
for package in cache:
    for version in package.versions:
        old_skeleton = build_skeleton_apt(version)
        new_skeleton = build_skeleton_apt_direct(version)
        assert old_skeleton.get_hash() == new_skeleton.get_hash()
        i += 1

print(f"Verified {i} package hashes are identical.")

