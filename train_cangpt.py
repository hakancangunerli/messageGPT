out_dir = 'canGPT'
eval_interval = 25 # Keep evaluations frequent due to expected overfitting
eval_iters = 20
log_interval = 10 # Moderate logging frequency

# Saving checkpoints only when validation improves
always_save_checkpoint = True

# Dataset and training batch configuration
dataset = 'data_processed'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 256 # Context window of up to 256 characters

# Configuration for a small GPT model
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

# Adjusted learning rate and iteration settings for quicker testing
learning_rate = 1e-3
max_iters = 500 # Reduced to 500 for faster testing
lr_decay_iters = 500 # Adjusted to match the new max_iters
min_lr = 1e-4
beta2 = 0.99

warmup_iters = 10
#scaled down 1/10 of the original value