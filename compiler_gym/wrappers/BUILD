# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
load("@rules_python//python:defs.bzl", "py_library")

py_library(
    name = "wrappers",
    srcs = [
        "__init__.py",
        "commandline.py",
        "core.py",
        "counter.py",
        "datasets.py",
        "fork.py",
        "llvm.py",
        "sqlite_logger.py",
        "time_limit.py",
        "validation.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//compiler_gym:config",
        "//compiler_gym/datasets",
        "//compiler_gym/envs",
        "//compiler_gym/util",
        "//compiler_gym/views",
    ],
)
