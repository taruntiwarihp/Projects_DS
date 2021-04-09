import json
from nltk_utils import tokenize, stem, bag_of_words
import numpy as np
import warnings
warnings.filterwarnings("ignore")

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from model import NeuralNet

with open('intents.json', 'r') as f:
    intents = json.load(f)

# print(intents)

all_words = []
tags = []
xy = []
for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        xy.append((w, tag))

ignore_words = ['?','!','.',',']
all_words = [stem(w) for w in all_words if w not in ignore_words]
all_words = sorted(set(all_words))
tags  = sorted(set(tags))

X_train  = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    
    label = tags.index(tag)
    y_train.append(label) # CrossEntropyLoss

X_train = np.array(X_train)
y_train = np.array(y_train)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(X_train)
        self.x_data = X_train
        self.y_data = y_train
        
    # dataset[idx]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.n_samples

# Hyper paramters
batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(X_train[0])
learning_rate = 0.001
num_epochs = 1000


dataset = ChatDataset()
train_loader = DataLoader(dataset = dataset, batch_size = batch_size,
                        shuffle =True, num_workers=0)


device  = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size)

# loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(device)

        # Forward
        outputs = model(words)
        loss = criterion(outputs, labels)

        # backward and optimizer step
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if (epoch +1) % 100 == 0:
        # f'epoch {epoch+1}/{num_epochs}, loss={loss.item():.4f}'
        print("epoch {}/{}, loss={:.4f}.".format(epoch+1,num_epochs,loss.item()))

# print(f'Final loss, loss={loss.item():.4f}')
print("Final Loss, loss{:.4f}".format(loss.item()))

data = {
    "model_state":model.state_dict(),
    "input_size":input_size,
    "output_size":output_size,
    "hiddent_size": hidden_size,
    "all_words":all_words,
    "tags": tags
}
FILE = "data.pth"
torch.save(data, FILE)

print("Traning complete. file saved to",FILE)