# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path
from typing import Iterable, List, Optional, Union

import numpy as np

from compiler_gym.datasets import Dataset
from compiler_gym.envs.mlir.datasets import MatmulBenchmark, get_mlir_datasets
from compiler_gym.service.client_service_compiler_env import ClientServiceCompilerEnv
from compiler_gym.spaces import Reward, RuntimeReward
from compiler_gym.util.gym_type_hints import ActionType
from compiler_gym.views import ObservationSpaceSpec

_MLIR_DATASETS: Optional[List[Dataset]] = None


def _get_mlir_datasets(site_data_base: Optional[Path] = None) -> Iterable[Dataset]:
    """Get the MLIR datasets. Use a singleton value when site_data_base is the
    default value.
    """
    global _MLIR_DATASETS
    if site_data_base is None:
        if _MLIR_DATASETS is None:
            _MLIR_DATASETS = list(get_mlir_datasets(site_data_base=site_data_base))
        return _MLIR_DATASETS
    return get_mlir_datasets(site_data_base=site_data_base)


class MlirEnv(ClientServiceCompilerEnv):
    """Environment that exposes optimization parameters for matrix multiplication in MLIR.
    It optimizes the operation C = A * B, where A is an MxK matrix and B is an KxN.

    This environment is still under construction.

    The observation space is the running time of the operation.
    All optimization parameters are supplied in a single step.
    In other words the episode length is 1 step.
    It supports x86_64 processors."""

    def __init__(
        self,
        *args,
        benchmark: Optional[Union[str, MatmulBenchmark]] = None,
        datasets_site_path: Optional[Path] = None,
        rewards: Optional[List[Reward]] = None,
        **kwargs
    ):
        """
        :param args: Positional arguments passed to the base class
        `compiler_gym.service.ClientServiceCompilerEnv`.

        :param benchmark: Specifies what MLIR code is to be optimize.
        Currently the default benchmark and only benchmark is M=N=K=64.

        :param rewards: The reward spaces that this environment supports.
        Defaults to (-running time).

        :param datasets_site_path: The base path of a directory that will be used to
            store installed files.

        :param kwargs: keyworded arguments passed to the base class
        `compiler_gym.service.ClientServiceCompilerEnv`.
        """
        super().__init__(
            *args,
            **kwargs,
            rewards=[
                RuntimeReward(
                    runtime_count=1,
                    warmup_count=0,
                    estimator=np.median,
                    default_value=-1,
                )
            ]
            if rewards is None
            else rewards,
            datasets=_get_mlir_datasets(site_data_base=datasets_site_path),
            benchmark=benchmark
        )

        self._runtimes_per_observation_count: Optional[int] = None
        self.reset()
        if rewards is None:
            self.reward.spaces["runtime"].runtime_count = self.runtime_observation_count

    @property
    def runtime_observation_count(self) -> int:
        return self._runtimes_per_observation_count or int(
            self.send_param("mlir.get_runtimes_per_observation_count", "")
        )

    @runtime_observation_count.setter
    def runtime_observation_count(self, n: int) -> None:
        if self.in_episode:
            self.send_param("mlir.set_runtimes_per_observation_count", str(n))
        self._runtimes_per_observation_count = n

    def reset(self, *args, **kwargs):
        observation = super().reset(*args, **kwargs)
        # Resend the runtimes-per-observation session parameter, if it is a
        # non-default value.
        if self._runtimes_per_observation_count is not None:
            self.runtime_observation_count = self._runtimes_per_observation_count
        return observation

    def fork(self):
        fkd = super().fork()
        if self.runtime_observation_count is not None:
            fkd.runtime_observation_count = self.runtime_observation_count
        return fkd

    def step(  # pylint: disable=arguments-differ
        self,
        action: ActionType,
        observation_spaces: Optional[Iterable[Union[str, ObservationSpaceSpec]]] = None,
        reward_spaces: Optional[Iterable[Union[str, Reward]]] = None,
    ):
        return self.multistep(
            actions=[action],
            observation_spaces=observation_spaces,
            reward_spaces=reward_spaces,
        )
