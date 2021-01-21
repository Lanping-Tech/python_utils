import torch
import torchvision
import torchvision.transforms as T
import model
import config
import dataset
import numpy as np
import time
from tqdm import tqdm

__all__ = ["train_fn", "eval_fn"]


def train_fn(train_dataloader, model, optimizer, scheduler, device):
    model.train()
    for X, labels in tqdm(train_dataloader):
        X = X.to(device)
        losses = model(X, labels)
        loss_value = losses.item()

        optimizer.zero_grad()
        losses.backward()
        optimizer.step()
        scheduler.step()

    return loss_value