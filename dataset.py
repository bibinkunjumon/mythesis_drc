import torch
import torch.nn as nn
import torchaudio.transforms as T


class SpeechRecognitionDataset(torch.utils.data.Dataset):
    def __init__(self, audio_data, labels):
        self.audio_data = audio_data
        self.labels = labels

    def __len__(self):
        return len(self.audio_data)

    def __getitem__(self, idx):
        audio = self.audio_data[idx]
        label = self.labels[idx]

        # Preprocess audio data
        transform = T.Compose([
            T.Resample(16000),
            T.MelSpectrogram(),
            T.ToTensor()
        ])
        audio = transform(audio)

        return audio, label
