"""Pré-processamento dos dados com NumPy (Entrega 1).

Assinaturas e contratos das transformações. A **implementação** será feita na
tarefa de funções do código (#5).
"""

from __future__ import annotations

from typing import Tuple

import numpy as np
import pandas as pd


def split_features_target(
    data: pd.DataFrame,
    target_column: str,
) -> Tuple[np.ndarray, np.ndarray]:
    """Separa os atributos (X) da coluna-alvo (y) a partir de um DataFrame."""
    pass


def standardize(X: np.ndarray) -> np.ndarray:
    """Padroniza os atributos para média 0 e desvio-padrão 1 (z-score)."""
    pass


def split_data(
    X: np.ndarray,
    y: np.ndarray,
    test_size: float = 0.2,
    seed: int = 42,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Divide os dados em conjuntos de treino e teste."""
    pass
