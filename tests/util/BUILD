# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
load("@rules_python//python:defs.bzl", "py_test")
load("@rules_cc//cc:defs.bzl", "cc_test")

py_test(
    name = "capture_output_test",
    srcs = ["capture_output_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

py_test(
    name = "commands_test",
    srcs = ["commands_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

py_test(
    name = "debug_util_test",
    srcs = ["debug_util_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
        "//tests/pytest_plugins:common",
    ],
)

py_test(
    name = "download_test",
    srcs = ["download_test.py"],
    deps = [
        "//compiler_gym/errors",
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

py_test(
    name = "executor_test",
    srcs = ["executor_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

cc_test(
    name = "EnumUtilTest",
    srcs = ["EnumUtilTest.cc"],
    deps = [
        "//compiler_gym/util:EnumUtil",
        "//tests:TestMacros",
        "//tests:TestMain",
        "@gtest",
    ],
)

py_test(
    name = "filesystem_test",
    srcs = ["filesystem_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
        "//tests/pytest_plugins:common",
    ],
)

py_test(
    name = "minimize_trajectory_test",
    timeout = "short",
    srcs = ["minimize_trajectory_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
        "//tests/pytest_plugins:llvm",
    ],
)

py_test(
    name = "parallelization_test",
    timeout = "short",
    srcs = ["parallelization_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

py_test(
    name = "permutation_test",
    timeout = "short",
    srcs = ["permutation_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

py_test(
    name = "runfiles_path_test",
    srcs = ["runfiles_path_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
        "//tests/pytest_plugins:common",
    ],
)

py_test(
    name = "shell_format_test",
    srcs = ["shell_format_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

py_test(
    name = "statistics_test",
    timeout = "short",
    srcs = ["statistics_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

cc_test(
    name = "StrLenConstexprTest",
    srcs = ["StrLenConstexprTest.cc"],
    deps = [
        "//compiler_gym/util:StrLenConstexpr",
        "//tests:TestMain",
    ],
)

cc_test(
    name = "SubprocessTest",
    srcs = ["SubprocessTest.cc"],
    deps = [
        "//compiler_gym/util:Subprocess",
        "//tests:TestMain",
    ],
)

py_test(
    name = "temporary_working_directory_test",
    timeout = "short",
    srcs = ["temporary_working_directory_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

py_test(
    name = "timer_test",
    srcs = ["timer_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)

py_test(
    name = "truncate_test",
    srcs = ["truncate_test.py"],
    deps = [
        "//compiler_gym/util",
        "//tests:test_main",
    ],
)
