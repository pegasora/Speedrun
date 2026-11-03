# Speedrun

Welcome! This repository is your home base for the internship. It collects the notes, slides, books, and assignments you'll work through as you get up to speed on **Python, machine vision, PLCs, and robotics**.

Every folder has its own `README.md` that explains what's in it, what order to go in, and where to find more help. When you click into a folder on GitHub, its README shows up below the file list, so you can treat the READMEs like a map.

## How to use this repo

If you haven't used GitHub before, don't worry. You only need a few basics:

1. **Browse it on GitHub.** Click folders to move around and click a PDF to view it in the browser. That's enough to get started.
2. **Get a copy on your computer.** Either:
   - Click the green **Code** button, then **Download ZIP**, or
   - Install [Git](https://git-scm.com/downloads) and clone it:
     ```bash
     git clone https://github.com/pegasora/Speedrun.git
     ```
     Cloning is better long term because you can `git pull` to get new material as I add it.
3. **Learn Git as you go.** GitHub's [Hello World guide](https://docs.github.com/en/get-started/start-your-journey/hello-world) is a 10-minute intro. You'll pick up the rest by using it.
4. **Want more detail?** The [Git and GitHub Guide](Github/) covers what Git and GitHub are, installing Git, cloning, opening the repo in VS Code, pulling new material, and troubleshooting.

## Suggested pipeline

This is a suggested order, not a strict schedule. Move at your own pace and spend extra time on whatever clicks for you.

| Step | Section | Goal |
|:---:|---|---|
| 1 | [Python → Intro](Python/Intro/) | Learn Python fundamentals from the book |
| 2 | [Python → Machine Vision](Python/Machine-Vision/) | OpenCV, image processing, and intro vision models |
| 2b | [Python → AI-Related](Python/AI-Related/) | *(Optional)* Classical ML and neural networks |
| 3 | [PLCs](PLCs/) | Digital logic, then CLICK PLCs, then Allen-Bradley and Studio 5000 |
| 4 | [Python → Robotics](Python/Robotics/) | Our FANUC EtherNet/IP drivers and the Standard Bots SDK |
| 5 | [Python → ROS2](Python/ROS2/) | *(If you get that far)* ROS 2 and robotics software |

**Python comes first.** Everything else in this repo builds on it, including talking to PLCs and robots from code.

## Repository map

```
Speedrun/
├── Github/                  In-depth Git and GitHub guide
├── Python/                  Python track (start here)
│   ├── Intro/               Python Crash Course book + instructions
│   ├── Machine-Vision/      Machine vision course: lectures + assignments
│   ├── AI-Related/          AI / data analysis course: lectures + assignments
│   ├── Robotics/            FANUC + Standard Bots drivers (coming soon)
│   └── ROS2/                ROS 2 material (coming soon)
├── PLCs/                    PLC track
│   ├── General/             Digital logic and intro slides
│   ├── Automation-Direct/   CLICK PLC setup and projects
│   └── Allen-Bradley/       Studio 5000 / Logix material
└── SCADA/                   SCADA material (coming soon)
```

| Section | Description |
|---|---|
| [Github](Github/) | Git and GitHub guide: installing, cloning, pulling, and VS Code |
| [Python](Python/) | Tooling setup (uv, VS Code) and an overview of the Python sections |
| [Python/Intro](Python/Intro/) | *Python Crash Course* with required chapters and project options |
| [Python/Machine-Vision](Python/Machine-Vision/) | 19 lectures on cameras, OpenCV, filtering, segmentation, and object detection |
| [Python/AI-Related](Python/AI-Related/) | Lectures on regression, classifiers, clustering, and neural networks |
| [Python/Robotics](Python/Robotics/) | Robot drivers we use on the floor |
| [Python/ROS2](Python/ROS2/) | Robot Operating System 2 |
| [PLCs](PLCs/) | Overview of the PLC track |
| [PLCs/General](PLCs/General/) | Digital logic and intro slides |
| [PLCs/Automation-Direct](PLCs/Automation-Direct/) | CLICK PLCs: setup, connecting, and wiring tasks |
| [PLCs/Allen-Bradley](PLCs/Allen-Bradley/) | Studio 5000 and the PLCs on the manufacturing line |
| [SCADA](SCADA/) | Supervisory control and data acquisition |

## Getting help

- **Ask me.** That's what I'm here for. If you've been stuck on something for more than about 30 minutes, reach out.
- **Read the error message.** Then copy it into a search engine. Seriously, this solves most problems.
- Each section README has a **Resources** list with documentation and tutorials for that topic.
