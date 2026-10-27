"""Compare parameter counts for a dense layer and a hypothetical LoRA adapter."""


def compare_parameters(in_features: int, out_features: int, rank: int) -> tuple[int, int]:
    if in_features <= 0 or out_features <= 0:
        raise ValueError("Layer dimensions must be positive integers")
    if rank <= 0:
        raise ValueError("LoRA rank must be a positive integer")

    dense_parameters = in_features * out_features
    adapter_parameters = rank * (in_features + out_features)
    return dense_parameters, adapter_parameters


if __name__ == "__main__":
    inputs = 4096
    outputs = 4096
    rank = 8
    dense, adapter = compare_parameters(inputs, outputs, rank)
    percentage = adapter / dense * 100

    print(f"Dense layer parameters: {dense:,}")
    print(f"LoRA adapter parameters at rank {rank}: {adapter:,}")
    print(f"Adapter size relative to dense layer: {percentage:.2f}%")
    print("This arithmetic is not a measurement of accuracy, memory use, or training time.")
