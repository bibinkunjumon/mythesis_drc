import torch
import torch.nn as nn


# Encoding component
class SpeechEncoder(nn.Module):
    def __init__(self):
        super(SpeechEncoder, self).__init__()
        self.lstm = nn.LSTM(input_size=128, hidden_size=128,
                            num_layers=1, batch_first=True)

    def forward(self, x):
        h0 = torch.zeros(1, x.size(0), 128).to(x.device)
        c0 = torch.zeros(1, x.size(0), 128).to(x.device)

        out, _ = self.lstm(x, (h0, c0))
        return out[:, -1, :]
