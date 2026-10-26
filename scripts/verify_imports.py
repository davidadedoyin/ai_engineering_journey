import importlib

modules = [
    "numpy",
    "pandas",
    "matplotlib",
    "sklearn",
    "fastapi",
    "pydantic",
]

for name in modules:
    try:
        importlib.import_module(name)
        print(f"OK: {name}")
    except Exception as exc:
        print(f"MISSING: {name} -> {exc}")
