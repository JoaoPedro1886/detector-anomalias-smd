"""Treinamento do detector de anomalias.

Este modulo deve orquestrar a preparacao dos dados, a instanciacao do modelo
e o ciclo de treino.
"""

from __future__ import annotations

from typing import Optional

import numpy as np


def train_model(
    model,
    X_train: np.ndarray,
    y_train: Optional[np.ndarray] = None,
) -> object:
    """Executa o treinamento do modelo informado."""
    pass
