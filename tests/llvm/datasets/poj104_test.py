# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""Tests for the POJ104 dataset."""
import sys
from itertools import islice
from pathlib import Path

import gym
import pytest

import compiler_gym.envs.llvm  # noqa register environments
from compiler_gym.envs.llvm import LlvmEnv
from compiler_gym.envs.llvm.datasets import POJ104Dataset
from compiler_gym.errors import BenchmarkInitError
from tests.pytest_plugins.common import skip_on_ci
from tests.test_main import main

pytest_plugins = ["tests.pytest_plugins.common", "tests.pytest_plugins.llvm"]


@pytest.fixture(scope="module")
def poj104_dataset() -> POJ104Dataset:
    with gym.make("llvm-v0") as env:
        ds = env.datasets["poj104-v1"]
    yield ds


def test_poj104_size(poj104_dataset: POJ104Dataset):
    if sys.platform == "darwin":
        assert poj104_dataset.size == 49815
    else:
        assert poj104_dataset.size == 49816


@skip_on_ci
@pytest.mark.parametrize("index", range(100))
def test_poj104_random_select(
    env: LlvmEnv, poj104_dataset: POJ104Dataset, index: int, tmpwd: Path
):
    uri = next(islice(poj104_dataset.benchmark_uris(), index, None))
    benchmark = poj104_dataset.benchmark(uri)
    env.reset(benchmark=benchmark)

    assert benchmark.source
    benchmark.write_sources_to_directory(tmpwd)
    assert (tmpwd / "source.cc").is_file()


@skip_on_ci
def test_poj104_random_benchmark(env: LlvmEnv, poj104_dataset: POJ104Dataset):
    benchmark = poj104_dataset.random_benchmark()
    env.reset(benchmark=benchmark)
    assert benchmark.source


@pytest.mark.parametrize(
    "uri",
    [
        "benchmark://poj104-v1/1/1486",
    ],
)
def test_poj104_known_bad_bitcodes(env: LlvmEnv, uri: str):
    # This test is intentionally structured in a way that if the benchmark does
    # not raise an error, it still passes.
    try:
        env.reset(benchmark=uri)
    except BenchmarkInitError as e:
        assert "Failed to parse LLVM bitcode" in str(e)


if __name__ == "__main__":
    main()
