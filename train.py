import os
import torch
from torch.utils.data import DataLoader
import torchvision
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from models import OCR_Model
from utils import Transform

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', type = int, default = 128, help = 'Batch Size')
parser.add_argument('--epochs', type = int, help = 'Number of epochs')
parser.add_argument('--save_every', type = int, default = 2, help = 'Frequency to save checkpoints')
