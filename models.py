import torch
import torch.nn as nn
from torch import Tensor


def make_pos_grid(height: int, width: int, device: torch.device) -> Tensor:
    gi, gj = torch.meshgrid(
        torch.linspace(-1, 1, height, device=device),
        torch.linspace(-1, 1, width, device=device),
        indexing="ij",
    )
    grid = torch.stack([gi, gj], dim=0)
    return grid


class AddCoords(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        pos_grid = make_pos_grid(height=x.shape[2], width=x.shape[3], device=x.device)
        pos_grid = pos_grid.expand((x.shape[0], -1, -1, -1))
        return torch.cat([x, pos_grid], dim=1)


class Regressor0(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.seq = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=2, kernel_size=1),
            nn.Flatten(start_dim=1),
        )

    def forward(self, x: Tensor) -> Tensor:
        return self.seq(x)


class Regressor1(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.seq = nn.Sequential(
            AddCoords(),
            nn.Conv2d(in_channels=5, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=32, out_channels=2, kernel_size=1),
            nn.Flatten(start_dim=1),
        )

    def forward(self, x: Tensor) -> Tensor:
        return self.seq(x)


class Regressor2(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.seq = nn.Sequential(
            AddCoords(),
            nn.Conv2d(in_channels=5, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            AddCoords(),
            nn.Conv2d(in_channels=34, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            AddCoords(),
            nn.Conv2d(in_channels=34, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            AddCoords(),
            nn.Conv2d(in_channels=34, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            AddCoords(),
            nn.Conv2d(in_channels=34, out_channels=32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            AddCoords(),
            nn.Conv2d(in_channels=34, out_channels=2, kernel_size=1),
            nn.Flatten(start_dim=1),
        )

    def forward(self, x: Tensor) -> Tensor:
        return self.seq(x)
