# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library")

py_binary(
    name = "example-unrolling-service-py",
    srcs = ["example_service.py"],
    data = [
        "//examples/example_unrolling_service/loop_unroller",
    ],
    main = "example_service.py",
    visibility = ["//visibility:public"],
    deps = [
        "//compiler_gym/service",
        "//compiler_gym/service/proto",
        "//compiler_gym/service/runtime",
        "//compiler_gym/third_party/llvm",
    ],
)
