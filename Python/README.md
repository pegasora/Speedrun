# Python Section

## Info

This part of the repository has five sections. Start with **Intro**, then pick whichever interests you most between **Machine Vision** and **AI-Related**. **Robotics** comes after the PLC track, and **ROS2** should be done after Robotics.

| # | Section | What's in it | Status |
|:---:|---|---|---|
| 1 | [Intro](Intro/) | *Python Crash Course* (3rd ed.) with required chapters and projects | Ready |
| 2 | [Machine-Vision](Machine-Vision/) | Machine vision course: OpenCV, image processing, object detection | Ready |
| 2b | [AI-Related](AI-Related/) | AI / data analysis course: classical ML and neural networks | Ready |
| 3 | [Robotics](Robotics/) | FANUC EtherNet/IP drivers and the Standard Bots SDK | Coming soon |
| 4 | [ROS2](ROS2/) | Robot Operating System 2 | Coming soon |

## General recommendations

### UV

I recommend using [uv](https://docs.astral.sh/uv/) to work with Python. It manages Python installs, packages, virtual environments, and running scripts, all in one tool, and it makes life much easier.

- [Installation and getting started](https://docs.astral.sh/uv/getting-started/)
- [Guides](https://docs.astral.sh/uv/guides/)

These commands cover most of what you'll need:

```bash
uv python install            # install a Python version
uv init my-project           # create a new project folder with a pyproject.toml
cd my-project
uv add opencv-python numpy   # add packages to the project
uv run main.py               # run a script inside the project's environment
```

If you want more guidance or want to see how I use it, let me know.

> **Note:** *Python Crash Course* walks you through installing Python the "normal" way. That's fine too. You can follow the book's setup to start and switch to uv once you're comfortable.

### VSCode IDE

[Visual Studio Code](https://code.visualstudio.com/) is the editor I recommend. It's free and works on Windows, macOS, and Linux.

Recommended extensions:

| Extension | Why |
|---|---|
| [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) | Run, debug, and get autocomplete for Python |
| [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) | Open and run `.ipynb` notebooks inside VS Code |
| [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) | Fast linting and formatting to catch mistakes early |

Microsoft's [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) tutorial walks through the setup.

## Sections

### 1. Intro

Start here. Work through *Python Crash Course*. Chapters 1–10 are required, then pick a project from Part II. See [Intro/README.md](Intro/) for details.

### 2. Machine Vision

Course lectures and assignments covering cameras, calibration, filtering, edges, contours, segmentation, motion, and object detection with OpenCV. See [Machine-Vision/README.md](Machine-Vision/).

### 2b. AI-Related

Course lectures and assignments covering data manipulation, regression, decision trees, clustering, SVMs, and neural networks with scikit-learn and Keras. Optional, but useful background for vision models. See [AI-Related/README.md](AI-Related/).

### 3. Robotics

Material for the robots we use: our FANUC EtherNet/IP drivers and the Standard Bots SDK. See [Robotics/README.md](Robotics/).

### 4. ROS2

ROS 2 fundamentals for robotics programming, if you get that far. See [ROS2/README.md](ROS2/).
