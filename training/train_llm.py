import torch 
print("CUDA available:",torch.cuda.is_available())
print("GPU Count:",torch.cuda.device_count())
