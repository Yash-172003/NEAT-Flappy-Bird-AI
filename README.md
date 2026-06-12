# 🐦 NEAT Flappy Bird AI

AI-powered Flappy Bird agent that learns to play autonomously using NEAT (NeuroEvolution of Augmenting Topologies), evolutionary neural networks, and fitness-based optimization.

---

## 📌 Overview

This project demonstrates how evolutionary algorithms can be used to train an autonomous agent to play Flappy Bird without any pre-programmed gameplay strategy.

Using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm, a population of neural networks evolves over generations. The networks learn when to jump by interacting with the environment, receiving rewards for survival and successfully navigating through pipes.

Over time, the population develops increasingly sophisticated gameplay strategies through mutation, crossover, speciation, and natural selection.

---

## 🚀 Features

* Autonomous Flappy Bird gameplay
* Neural networks evolved using NEAT
* Fitness-based learning
* Dynamic topology evolution
* Species formation and preservation
* Real-time training visualization
* Procedurally generated game assets
* Population statistics tracking
* Evolutionary optimization

---

## 🧠 How NEAT Works

The NEAT algorithm starts with simple neural networks and gradually evolves them into more complex structures.

### Inputs

Each bird receives:

1. Current bird Y position
2. Distance from top pipe
3. Distance from bottom pipe

### Output

Neural Network Output:

```text
Output > 0.5 → Jump
Output ≤ 0.5 → Do Nothing
```

### Fitness Function

Birds receive rewards for:

* Staying alive
* Passing pipes
* Surviving longer

Birds are penalized for:

* Colliding with pipes
* Hitting the ground
* Flying out of bounds

### Evolution Process

1. Initialize population
2. Evaluate fitness
3. Select best genomes
4. Perform crossover
5. Apply mutations
6. Create new generation
7. Repeat

---

## 🏗️ System Architecture

```text
Game Environment
       │
       ▼
 Bird Sensors
       │
       ▼
 Neural Network
       │
       ▼
 Jump Decision
       │
       ▼
 Environment Feedback
       │
       ▼
 Fitness Score
       │
       ▼
 Evolution Engine (NEAT)
       │
       ▼
 Next Generation
```

---

## 📂 Project Structure

```text
NEAT-Flappy-Bird-AI/
│
├── imgs/
│   ├── bird1.png
│   ├── bird2.png
│   ├── bird3.png
│   ├── pipe.png
│   ├── bg.png
│   └── base.png
│
├── flappy_bird.py
├── flappy_bird_practice.py
├── config-feedforward.txt
├── visualize.py
├── generate_assets.py
├── requirements.txt
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## 📁 File Descriptions

### flappy_bird.py

Main training program.

Responsibilities:

* Population creation
* Fitness evaluation
* Neural network execution
* Evolution process
* Training visualization

### flappy_bird_practice.py

Experimental implementation used for testing gameplay mechanics and NEAT integration.

### config-feedforward.txt

NEAT configuration file.

Defines:

* Population size
* Mutation rates
* Species threshold
* Fitness criteria
* Network structure

### visualize.py

Utility functions for:

* Fitness graphs
* Species tracking
* Neural network visualization

### generate_assets.py

Automatically generates game assets including:

* Bird sprites
* Pipes
* Ground
* Background

### requirements.txt

Project dependencies.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/NEAT-Flappy-Bird-AI.git
cd NEAT-Flappy-Bird-AI
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Generate assets:

```bash
python generate_assets.py
```

Start training:

```bash
python flappy_bird.py
```

---

## 📊 Training Configuration

Current NEAT settings:

| Parameter           | Value |
| ------------------- | ----- |
| Population Size     | 50    |
| Inputs              | 3     |
| Outputs             | 1     |
| Activation Function | tanh  |
| Fitness Criterion   | max   |
| Fitness Threshold   | 100   |
| Max Generations     | 50    |

---

## 📈 Expected Learning Progress

| Generation | Behavior                    |
| ---------- | --------------------------- |
| 1-5        | Random movement             |
| 5-15       | Occasional pipe avoidance   |
| 15-30      | Consistent survival         |
| 30-50      | Efficient gameplay strategy |

---

## 🔬 Concepts Demonstrated

* Neuroevolution
* Evolutionary Computation
* Genetic Algorithms
* Artificial Intelligence
* Neural Networks
* Fitness Optimization
* Speciation
* Procedural Content Generation
* Simulation-Based Learning

---

## 🛠️ Tech Stack

### Languages

* Python

### Libraries

* Pygame
* NEAT-Python
* NumPy
* Matplotlib
* Graphviz

### AI Techniques

* NEAT
* Neuroevolution
* Evolutionary Optimization

---

## 🎯 Future Improvements

* Save and load trained models
* Parallelized fitness evaluation
* Dynamic difficulty adjustment
* Reinforcement learning comparison
* Deep Q-Learning implementation
* Performance analytics dashboard
* Web deployment

---

## 📚 References

* NEAT-Python Documentation
* Stanley & Miikkulainen NEAT Paper
* Pygame Documentation

---

## 👨‍💻 Author

Yashwender Singh

AI Engineer | Machine Learning Enthusiast | Evolutionary Computing Explorer

---

## 📄 License

This project is licensed under the MIT License.
