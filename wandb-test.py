import math
import random
import wandb

# 1️⃣ Start a new run, tracking config metadata
wandb.init(project="test-drive", config={
    "learning_rate": 0.02,
    "dropout": 0.2,
    "architecture": "CNN",
    "dataset": "CIFAR-100",
})
config = wandb.config

# Simulating a training or evaluation loop
for x in range(50):
    acc = math.log(1 + x + random.random() * config.learning_rate) + random.random()
    loss = 10 - math.log(1 + x + random.random() + config.learning_rate * x) + random.random()
    static = x
    # 2️⃣ Log metrics from your script to W&B
    wandb.log({"acc":acc, "loss":loss, "static":static})

wandb.finish()