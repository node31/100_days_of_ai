# Day 8: Simple Transformer Attention Demo
# This example shows how attention weights work in a transformer-like model using PyTorch

import torch
import torch.nn.functional as F

# Example input: 4 words represented as vectors
inputs = torch.tensor([
    [1.0, 0.0],  # word 1
    [0.0, 1.0],  # word 2
    [1.0, 1.0],  # word 3
    [0.5, 0.5]   # word 4
])

# Random attention weights for each word (simulating self-attention)
attention_scores = torch.rand(4)
attention_weights = F.softmax(attention_scores, dim=0)

# Weighted sum (context vector)
context = torch.sum(inputs * attention_weights.unsqueeze(1), dim=0)

print("Input word vectors:\n", inputs)
print("Attention weights:", attention_weights)
print("Context vector:", context)
