# Friday challenge: compare LoRA parameter counts

## Goal

Use `lora_parameter_demo.py` to compare a full dense layer with a low-rank LoRA adapter.

## Requirements

1. Run the example with its default dimensions.
2. Change the rank and compare the adapter parameter count.
3. Try a rank that is not smaller than either layer dimension and explain why it no longer demonstrates a compact adapter.
4. State at least two things the parameter-count comparison does not tell you about model quality or actual training cost.

## Done when

- The script reports full-layer and adapter parameter counts and the adapter share.
- Invalid dimensions or rank are rejected with a clear error.
- Your explanation distinguishes parameter count from accuracy and wall-clock training time.
