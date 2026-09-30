from client import ArgumentBoundaryClamper

clamped = ArgumentBoundaryClamper.clamp_argument(500, {"minimum": 1, "maximum": 100})
print("Clamped value:", clamped)
