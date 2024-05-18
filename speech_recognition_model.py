import torch
import torch.nn as nn
import torch.nn.functional as F


class SpeechRecognitionModel(nn.Module):
    def __init__(self):
        super(SpeechRecognitionModel, self).__init__()
        self.conv1 = nn.Conv1d(1, 64, kernel_size=3)
        self.conv2 = nn.Conv1d(64, 64, kernel_size=3)
        self.conv3 = nn.Conv1d(64, 128, kernel_size=3)
        self.fc1 = nn.Linear(128 * 32, 128)  # Assuming 32 timesteps
        self.fc2 = nn.Linear(128, num_classes=16)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = F.relu(self.conv3(x))
        x = x.view(-1, 128 * 32)  # Flatten
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
