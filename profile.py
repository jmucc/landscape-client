#!/usr/bin/env python3
import time

import apt_pkg
from apt.cache import Cache

cache = Cache(rootdir=None)
cache.open(None)

apt_set = set()
start_time = time.time()
for package in cache:
    for version in package.versions:
        apt_set.add(
            (
                version.package.name,
                version.version,
                version.section,
                # version.summary.strip(),
                # # Need to strip summary to match apt_pkg's short_desc
                # version.description, Could not find equivalent in apt_pkg
                version.size,
                version.installed_size,
            )
        )
end_time = time.time()
print(f"Apt access: {end_time - start_time} seconds")

apt_pkg.init_config()
apt_pkg.init_system()
cache = apt_pkg.Cache(None)
records = apt_pkg.PackageRecords(cache)

apt_pkg_set = set()
start_time = time.time()
for pkg in cache.packages:
    for ver in pkg.version_list:
        # records.lookup(ver.file_list[0])
        apt_pkg_set.add(
            (
                ver.parent_pkg.name,
                ver.ver_str,
                ver.section,
                # records.short_desc,
                ver.size,
                ver.installed_size,
            )
        )
end_time = time.time()
print(f"Apt_pkg access: {end_time - start_time} seconds")

print("\nSet comparison:")
print(f"Apt set size: {len(apt_set)}")
print(f"Apt_pkg set size: {len(apt_pkg_set)}")
print(f"Sets are equal: {apt_set == apt_pkg_set}")
print(f"Items only in apt: {len(apt_set - apt_pkg_set)}")
print(f"Items only in apt_pkg: {len(apt_pkg_set - apt_set)}")


# apt_pkg.init_config()
# apt_pkg.init_system()
# cache = apt_pkg.Cache(None)

# def explore_attributes(obj, depth=0, max_depth=3, visited=None):
#     if visited is None:
#         visited = set()

#     obj_id = id(obj)
#     if obj_id in visited or depth > max_depth:
#         return
#     visited.add(obj_id)

#     indent = "  " * depth
#     try:
#         attrs = dir(obj)
#         for attr in attrs:
#             if not attr.startswith('_'):
#                 try:
#                     value = getattr(obj, attr)
#                     print(f"{indent}{attr}: {type(value).__name__}")
#                     if depth < max_depth and hasattr(value, '__dict__'):
#                         explore_attributes(value, depth + 1, max_depth, visited)
#                 except Exception:
#                     pass
#     except Exception:
#         pass

# for pkg in cache.packages:
#     for ver in pkg.version_list:
#         print(f"\nExploring attributes of version: {ver}")
#         explore_attributes(ver)
#         break
#     break
