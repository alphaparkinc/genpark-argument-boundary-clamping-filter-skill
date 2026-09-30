"""Argument Boundary Clamping Filter.
100% Python Standard Library.
"""

class ArgumentBoundaryClamper:
    """Clamps numerical ranges and string lengths to schema limits."""
    @staticmethod
    def clamp_argument(val, schema: dict):
        if isinstance(val, (int, float)):
            if "minimum" in schema:
                val = max(schema["minimum"], val)
            if "maximum" in schema:
                val = min(schema["maximum"], val)
            if "multipleOf" in schema:
                val = round(val / schema["multipleOf"]) * schema["multipleOf"]
            return val
        elif isinstance(val, str):
            if "maxLength" in schema and len(val) > schema["maxLength"]:
                val = val[:schema["maxLength"]]
            return val
        return val
