# pip install torch transformers datasets accelerate peft

from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model

model_name = "[any model]"
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="cache")
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="cache")

def preprocess_function(examples):
    inputs = [f"{prompt}\n" for prompt in examples["prompt"]]
    targets = [f"{completion}\n" for completion in examples["instruction"]]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True, padding="max_length")
    labels = tokenizer(targets, max_length=512, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

dataset = load_dataset("json", data_files="lora.json")
tokenized_dataset = dataset["train"].train_test_split(test_size=0.01)
tokenized_dataset = tokenized_dataset.map(preprocess_function, batched=True, remove_columns=dataset["train"].column_names)

lora_config = LoraConfig(
    r=16, # 32
    lora_alpha=32, # 64
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
    lora_dropout=0.01,
    bias="none", # all
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_config)

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=1,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=10,
    eval_steps=500,
    save_strategy="steps",
    save_steps=1000,
    learning_rate=1e-4,
    fp16=True,
    gradient_checkpointing=True,
    gradient_accumulation_steps=4,
    report_to = "none",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset['train'],
    eval_dataset=tokenized_dataset['test'],
    tokenizer=tokenizer,
)
trainer.train()

trainer.save_model("lora_model")
