# genpark-argument-boundary-clamping-filter-skill

Safe parameter boundary enforcement clamping out-of-range numerical arguments and truncating over-length strings.

## Architecture

```mermaid
flowchart LR
    Arg[Raw Model Argument] --> Clamper[ArgumentBoundaryClamper]
    Bounds[Min / Max / MultipleOf Constraints] --> Clamper
    Clamper --> SafeArg[Safe In-Bounds Parameter]
```

## Features
- **Anti-Buffer-Overflow**: Enforces maximum string lengths.
- **Pure Python**: 100% standard library.
