import torch
import torch.nn as nn
import typing as Any

from nemo_automodel.components.models.tubi_nano.config import TubiConfig


class GatedAttention(nn.Module):
  def __init__(self, config: TubiConfig):
    super().__init__()
    self.config = config

  def forward(
    self,
    hidden_states: torch.Tensor,
    position_embeddings: torch.Tensor,
    attention_mask: torch.Tensor | None = None,
  ):
    return hidden_states


class Block(nn.Module):
  def __init__(self, config: TubiConfig):
    super().__init__()
    self.config = config

  def forward(
    self,
    hidden_states: torch.Tensor,
    position_embeddings: torch.Tensor,
    attention_mask: torch.Tensor | None = None,
  ):
    return hidden_states

