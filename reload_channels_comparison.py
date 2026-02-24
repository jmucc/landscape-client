#!/usr/bin/env python3
import time

from apt.cache import Cache

from landscape.lib.apt.package.skeleton import build_skeleton_apt, create_package_hash

cache = Cache(rootdir=None)
cache.open(None)
hashes = set()
hashes_skeleton = set()

start = time.time()
for package in cache:
    for version in package.versions:
        hashes.add(create_package_hash(version))
end = time.time()
print(f"Without skeleton: {end - start} seconds")

cache = Cache(rootdir=None)
cache.open(None)

start = time.time()
for package in cache:
    for version in package.versions:
        hashes_skeleton.add(build_skeleton_apt(version).get_hash())
end = time.time()
print(f"With skeleton: {end - start} seconds")

assert hashes == hashes_skeleton
