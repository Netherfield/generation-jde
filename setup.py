# Copyright (c) 2023 Jules at TestPyPi
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import importlib
import sys
from pathlib import Path

from setuptools import setup

ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, ROOT.as_posix())

# to avoid using the local scheme with testpypi won't allow
# def local_scheme(version):
#     """Skip the local version (eg. +xyz of 0.6.1.dev4+gdf99fe2)
#     to be able to upload to Test PyPI"""
#     return ""

setup(
    # use_scm_version=True,
    # to avoid using local scheme
    # use_scm_version={"local_scheme": local_scheme},
    # my_modules=get_my_modules(),
    # include_package_data=True,
)


# used to determine if module dependencies can be imported
# def can_import(module):
#     try:
#         importlib.import_module(module)
#     except Exception:
#         return False
#     return True

# def get_my_modules():
#     # Check we have the modules around. If not, none of these will get built.
#     if not can_import("my_modules.pkgconfig"):
#         print("Package is missing")
#         return

#     my_modules = []

#     # Wayland backend dependencies
#     if can_import("dependencies_build"):
#         my_modules.append("libgeneration/dependencies/build.py")
#     else:
#         print("Failed to find module. Dependencies not built.")

#     return my_modules

