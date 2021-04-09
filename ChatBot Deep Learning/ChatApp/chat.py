import random 
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device  = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# print(device)

with open('intents.json','r') as f:
  intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data['input_size']
hidden_size = data['hiddent_size']
output_size = data['output_size']
all_words = data['all_words']
tags = data['tags']
model_state = data['model_state']

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Taru"

print("Namste !!! We are working everywhere in Pan-india. Just drop you delivery location pincode/postal code to check delivery availability or ask us at Whatsapp Helpline 7726996443.")
while True:
    sentence = input('You: ')
    if sentence =='quit':
        break
  
#   for word in sentence.split():
#     if word.isdigit():
#       word = int(word)
#       pf = list(df['Office Name'][df['Pincode'] == word ])
#       if len(pf) == 0:
#         print("Sorry to inform you, We don't deliver here :(")
#         break
#       sentence = callme()

 
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]


    if prob.item() >0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                print(bot_name, ":",random.choice(intent['responses']))
        # print("{}:{}".format(bot_name,random.choice(intent['responses'])))
      
    else:
        print("{} I do not understand...contact on WhatsApp 7726996443".format(bot_name))