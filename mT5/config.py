
#paths
df_root='' #path of the dataset
output_dir=""  #path of output directory

    
#hyperparameters
max_seq_length=100
learning_rate=3e-4
weight_decay=0.0
adam_epsilon=1e-8
warmup_steps=0
train_batch_size=8
eval_batch_size=8
num_train_epochs=20
gradient_accumulation_steps=8
n_gpu=1
fp_16=False # if you want to enable 16-bit training then install apex and set this to true
opt_level='O1'
max_grad_norm=1.0
    
#model type
model_type="small" # choices small, base, large, xl,xxl
