# Week 23: Fine-tuning and parameter-efficient adaptation

## Analogy

Prompting is like giving a capable teammate better instructions. Fine-tuning is more like additional training. Parameter-efficient fine-tuning (PEFT) changes a small set of added parameters instead of updating every parameter in a large model.

## Mon: prompting, retrieval, and fine-tuning

Choose the simplest method that meets the need:

- Prompting changes instructions or examples at inference time.
- Retrieval supplies current or private reference material at inference time.
- Fine-tuning changes model behavior through training data.

Fine-tuning is not a substitute for retrieval when the task needs changing facts or exact source citations.

## Tue: prepare training examples

Training examples should be representative, consistently formatted, and permitted for the intended use. Keep evaluation examples separate from training examples. Remove secrets and personal information unless there is a clear, authorized reason to retain them.

## Wed: LoRA and PEFT

LoRA adds trainable low-rank matrices to selected model layers. For a linear layer with input size `in_features` and output size `out_features`, a rank-`r` adapter has approximately:

`r * (in_features + out_features)` trainable parameters

This is often much smaller than updating all `in_features * out_features` weights. The exact savings depend on which layers are adapted and the rank.

## Thu: evaluate and ship carefully

- Compare the adapted model with the original on held-out examples.
- Check task quality, regressions, latency, and cost.
- Track the base model, adapter, data, and evaluation versions.
- Do not infer model quality from training loss alone.
- Training may require substantial compute and a compatible model license.

## Friday challenge

Run `lora_parameter_demo.py` to compare a full dense layer's parameter count with a hypothetical LoRA adapter. Change the dimensions and rank, then explain the trade-off.

## Saturday project

Design a small fine-tuning experiment on paper: define the use case, data schema, held-out evaluation set, baseline, success criteria, privacy checks, and rollback plan. Do not upload sensitive data or begin paid training without authorization.

## Did it stick? Repeat checklist

- I can explain when prompting, retrieval, or fine-tuning is appropriate.
- I can explain what LoRA changes and why it can reduce trainable parameters.
- I can explain why evaluation data must be held out.
- I can name compute, licensing, privacy, and regression risks.
