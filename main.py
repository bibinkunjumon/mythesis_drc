import torch
import torchaudio
import torch.nn as nn
from speech_recognition_model import SpeechRecognitionModel
from speech_encoder import SpeechEncoder
from speech_recognizer import SpeechRecognizer
from drc import DynamicRangeCompressor
from dataset import SpeechRecognitionDataset
import torchaudio.transforms as T


audio_data, _ = torchaudio.load('audio.mp4')
transform = T.Compose([
    T.Resample(16000),
    T.MelSpectrogram(),
    T.ToTensor()
])

mel_spectrogram = transform(audio_data)
model = SpeechRecognitionModel()
encoder = SpeechEncoder()
recognizer = SpeechRecognizer()
compressor = DynamicRangeCompressor()
compressed_data = compressor(mel_spectrogram)
encoded_speech = encoder(compressed_data)
recognized_command = recognizer(encoded_speech)

print('Recognized command:', recognized_command)

"""
# Define the training dataset and data loader
train_dataset = SpeechRecognitionDataset(train_audio_data, train_labels)
train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=32, shuffle=True)

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Train the model
for epoch in range(10):  # Loop over the dataset multiple times
    for batch in train_loader:
        input_data, labels = batch
        optimizer.zero_grad()
        outputs = model(input_data)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    # Print the loss at each epoch
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')"""
