from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile

# Create quantum and classical registers
q = QuantumRegister(3, "q")
c0 = ClassicalRegister(1, "c0")
c1 = ClassicalRegister(1, "c1")
c2 = ClassicalRegister(1, "c2")

# Create quantum circuit
qc = QuantumCircuit(q, c0, c1, c2)

# Step 1: Prepare an arbitrary state on qubit 0
qc.h(q[0])  # Example: create superposition

# Step 2: Create entanglement between q1 and q2
qc.h(q[1])
qc.cx(q[1], q[2])

# Step 3: Bell measurement on q0 and q1
qc.cx(q[0], q[1])
qc.h(q[0])

# Step 4: Measure q0 and q1
qc.measure(q[0], c0)
qc.measure(q[1], c1)

# Step 5: Apply corrections on q2 based on classical bits
# (This syntax works in Qiskit 1.x)
with qc.if_test((c1, 1)):
    qc.x(q[2])
with qc.if_test((c0, 1)):
    qc.z(q[2])

# Step 6: Measure teleported qubit
qc.measure(q[2], c2)

# Use AerSimulator instead of Aer.get_backend()
sim = AerSimulator()
compiled_circuit = transpile(qc, sim)
result = sim.run(compiled_circuit).result()

# Show result counts
counts = result.get_counts()
print("Result:", counts)

# Draw circuit
qc.draw("mpl")

