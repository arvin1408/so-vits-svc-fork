#!/usr/bin/env python

# This is a shim to allow GitHub to detect the package, build is done with poetry
# Taken from https://github.com/Textualize/rich

from setuptools import setup, find_packages  

if __name__ == "__main__":
    setup(name="so-vits-svc-fork", packages = find_packages())
