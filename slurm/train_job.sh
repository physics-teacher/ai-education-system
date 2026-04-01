#!/bin/bash
#SBATCH --job-name=ai-train
#SBATCH --nodes=4
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --time=24:00:00

srun docker run --gpus all -v /cluster/ai-education-system:/workspace controller-ip:5000/ai-education python training/train_llm.py
