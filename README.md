# Digital Logic

Implementation of digital logic circuit in python. The goal of this repo is to implement digital logic circuits in python that will serve as foundation of any other project that seeks to use the these circuit.

Currently the three fundamental gates have been implemented.
- AND
- OR
- NOT

Other gates which builds upon them have also been implemented like:
- Nand
- XOR
- XNOR

Arithmetic logics are currently being implemented.

## Usage 

To use the logic gates you first have to import your gate of choice.

```python
from digital.gates import AND
```

When a gate is imported you can use their functionality via the `logic` static method:

```python
result = AND.logic(1, 1)
print(result) # 1
```

You can also creat an instance of the gate and call the gate instance:

```python
and = AND(1, 1)
print(and()) # 1
```

All gates follow this pattern.



