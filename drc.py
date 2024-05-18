import torch
import torch.nn as nn


class DynamicRangeCompressor(nn.Module):
    def __init__(self, threshold=-20, ratio=4, attack=0.01, release=0.1):
        super(DynamicRangeCompressor, self).__init__()
        self.threshold = threshold
        self.ratio = ratio
        self.attack = attack
        self.release = release

    def forward(self, x):
        # Calculate the gain reduction
        gain_reduction = torch.clamp(
            x - self.threshold, min=0) / (self.ratio - 1)

        # Apply the gain reduction with attack and release
        gain_reduction = torch.where(
            x > self.threshold,
            gain_reduction * (1 - self.attack) + self.attack,
            gain_reduction * (1 - self.release) + self.release
        )

        # Apply the gain reduction to the input signal
        compressed_x = x * gain_reduction

        return compressed_x
