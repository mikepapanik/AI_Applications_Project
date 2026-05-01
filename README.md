# AI Applications Project

This repository contains two Artificial Intelligence applications developed as part of an MSc AI program:

1. **A\* Pathfinding Visualization**
2. **Image Reproduction using a Genetic Algorithm**

Both projects are implemented in Python and demonstrate fundamental AI search and optimization techniques.

---

## Project Structure

```text
AI_Applications_Project/
│
├── A Star/
│   ├── Astar.py
│   └── AstarPathfinding.mp4
│
├── GA image reproduction/
│   ├── GA.py
│   ├── genetic.py
│   ├── acropolis.jpg
│   └── solution_*.png
│
├── .gitignore
└── README.md
```

---

## Application 1: A\* Pathfinding Visualization

This application visualizes the **A\*** search algorithm on a grid using `pygame`.

The user can define:
- the start node,
- the target node,
- obstacles/barriers,
- and then watch the algorithm search for the shortest path.

### Features

- Interactive grid-based visualization
- Start and end node selection
- Barrier placement
- Real-time pathfinding animation
- Manhattan distance heuristic

### How to Run

```bash
python "A Star/Astar.py"
```

### Controls

Typical controls:

- **Left mouse click**: place start node, end node, or barriers
- **Right mouse click**: reset a selected cell
- **Space**: start the A\* algorithm
- **C**: clear the grid

A demo video is included in:

```text
A Star/AstarPathfinding.mp4
```

---

## Application 2: Genetic Algorithm Image Reproduction

This application uses a **Genetic Algorithm** to reproduce a target image.

The target image is converted into a chromosome representation. A population of candidate images is evolved over many generations, gradually improving similarity to the original image.

The implementation uses `pygad` for the genetic algorithm process.

### Features

- Image-to-chromosome conversion
- Fitness evaluation based on pixel similarity
- Genetic evolution over multiple generations
- Periodic saving of intermediate results
- Final reconstructed image visualization

### Target Image

The target image used by default is:

```text
GA image reproduction/acropolis.jpg
```

### Output

During execution, the program saves intermediate reconstructed images every 500 generations using filenames such as:

```text
solution_500.png
solution_1000.png
solution_1500.png
...
solution_20000.png
```

### How to Run

```bash
cd "GA image reproduction"
python GA.py
```

---

## Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

Install the required dependencies:

```bash
pip install pygame numpy imageio matplotlib pygad
```

Alternatively, create a `requirements.txt` file with:

```text
pygame
numpy
imageio
matplotlib
pygad
```

Then install everything with:

```bash
pip install -r requirements.txt
```

---

## Technologies Used

- Python
- Pygame
- NumPy
- ImageIO
- Matplotlib
- PyGAD

---

## Notes

The Genetic Algorithm image reproduction application may take a long time to complete because it runs for many generations and processes image pixel data.

For faster testing, you can reduce the number of generations inside `GA.py`:

```python
num_generations=20000
```

For example:

```python
num_generations=1000
```

---

## License

This project is licensed under the MIT License.

