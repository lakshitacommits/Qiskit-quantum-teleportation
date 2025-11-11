🧠 Quantum Teleportation using Qiskit

✨ “Teleportation isn’t science fiction anymore — it’s quantum physics!”

🌌 About this Project

This project demonstrates Quantum Teleportation — a fascinating concept in Quantum Computing where a quantum state is transferred from one qubit to another using entanglement and classical communication, without physically moving the particle itself.

Using Qiskit, IBM’s open-source quantum computing SDK, this project simulates the teleportation protocol step by step, helping beginners understand how quantum information can be shared securely and efficiently.

⚙️ How It Works

🔹 Step 1: Create a 3-qubit quantum circuit 🧩
🔹 Step 2: Prepare an arbitrary quantum state on the first qubit (|ψ⟩)
🔹 Step 3: Generate an entangled Bell pair between the second and third qubits
🔹 Step 4: Perform Bell-state measurements on the first two qubits
🔹 Step 5: Apply conditional quantum gates (X, Z) on the third qubit based on classical results
🔹 Step 6: Observe that the original state of the first qubit now appears on the third qubit 🎩✨

🧩 Tools & Libraries
Library	Purpose
🧱 Qiskit	Create and simulate quantum circuits
🧮 NumPy	Perform mathematical operations on statevectors
📊 Matplotlib	Plot and visualize measurement results
⚙️ Qiskit Aer	Run simulations using local quantum backends
🚀 Output Example
Result: {'1 0 0': 105, '1 1 1': 130, '0 0 1': 132, '0 1 1': 130, '0 1 0': 129, '1 1 0': 151, '1 0 1': 126, '0 0 0': 121}


Each key ('c0 c1 c2') represents the measurement results from the circuit.
This confirms that the teleportation protocol worked successfully! 🎉

🧠 Concepts Covered

Quantum Bits (Qubits) – Superposition & entanglement

Quantum Gates – H, CX, U(θ,φ,λ), X, Z

Measurement – Converting quantum states into classical bits

Quantum Entanglement – The “spooky action at a distance” Einstein talked about!

Classical Communication – Sending measured bits to reconstruct the teleported state

🪄 Run the Project
🧰 Requirements

Make sure you have Python and Qiskit installed:

pip install -U qiskit qiskit-aer matplotlib numpy

▶️ Execute
python QT1.PY

👩‍💻 Author

Lakshita Sharma
