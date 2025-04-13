# !pip install datasets transformers torch pandas pyarrow scikit-learn evaluate

label_list = [
    'Label XXX',
]

id2label = {}
for i, label in enumerate(label_list):
    id2label[i] = label

label2id = {}
for i, label in enumerate(label_list):
    label2id[label] = i

from transformers import BertTokenizer, BertForSequenceClassification

model_name = "google-bert/bert-base-multilingual-cased"
tokenizer = BertTokenizer.from_pretrained(model_name, cache_dir="caches/")
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=len(label_list), id2label=id2label, label2id=label2id, cache_dir="caches/")

import json
import pandas as pd

with open('language_classification.json', 'r') as f:
    data = json.load(f)

hf_dataset = []

for item in data:
    text = item['data']['text']
    label = item['annotations'][0]['result'][0]['value']['choices'][0]

    hf_item = {
        "text": text,
        "label": label,
    }
    hf_dataset.append(hf_item)

df = pd.DataFrame(hf_dataset)
df['label'] = df['label'].apply(lambda x: label2id[x])

dataset = Dataset.from_pandas(df)

def preprocess_function(examples):
    return tokenizer(examples["text"], truncation=True)

tokenized_dataset = dataset.map(preprocess_function, batched=True)

import numpy as np
from transformers import DataCollatorWithPadding
import evaluate

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
accuracy = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)

from transformers import TrainingArguments, Trainer
from datasets import Dataset

# Set training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy='steps',
    eval_steps=500,
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    weight_decay=0.01,
    save_total_limit=1,
    num_train_epochs=500,
    load_best_model_at_end=True,
    report_to="none",
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    eval_dataset=tokenized_dataset,
    data_collator=data_collator,
    processing_class=tokenizer,
    compute_metrics=compute_metrics,
)

# Train the model
trainer.train()

model.save_pretrained('mr4/YYY')
tokenizer.save_pretrained('mr4/YYY')

text = "Xin chào, tôi tên là Đặng Việt Dũng, tôi sinh ra ở Hòa Bình và đang sinh sống ở Hà Nội."

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "mr4/YYY"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained("mr4/language_classification")

inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

predictions = torch.nn.functional.softmax(logits, dim=-1)
print(predictions)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
for i, prediction in enumerate(predictions):
    print(text)
    for j, value in enumerate(prediction):
        print(f"    {id2label[j]}: {value.item() * 100}")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<")
