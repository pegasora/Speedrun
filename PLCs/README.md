# PLCs

A **PLC** (Programmable Logic Controller) is the industrial computer that runs machines on a manufacturing line. It reads inputs (buttons, sensors), runs a program (usually ladder logic), and drives outputs (motors, valves, lights).

> **Prerequisite:** Get comfortable with the [Python Intro](../Python/Intro/) first. Python is the priority. The PLC track comes after.

## Pipeline

| Step | Section | Goal |
|:---:|---|---|
| 1 | [General](General/) | Digital logic fundamentals and intro slides |
| 2 | [Automation-Direct](Automation-Direct/) | Connect to a **CLICK PLC**, get it running, and complete wiring and programming tasks |
| 3 | [Allen-Bradley](Allen-Bradley/) | Install **Studio 5000**, open an existing project from our line, and learn to read it. Running it comes later. |

**Why this order?** CLICK PLCs are simple and cheap, so they're a good place to learn the physical side (wiring I/O, power, connecting over Ethernet) without risk. Allen-Bradley is what runs on our manufacturing line, so you'll move there once the basics make sense.

## General slides

Start by working through these slides in order:

| # | Topic | Slides |
|:---:|---|---|
| 1 | Introduction to Class | [PDF](General/1%20Introduction%20to%20Class.pdf) |
| 3 | Digital Logic I | [PDF](General/3%20Digital%20Logic%20I.pdf) |
| 7 | Digital Logic II | [PDF](General/7%20Digital%20Logic%20II.pdf) |
| 14 | The Internet | [PDF](General/14%20The%20Internet.pdf) |
| 18 | Mini Factory Information | [PDF](General/18%20Mini%20Factory%20information.pdf) |

## Resources

- [RealPars (YouTube)](https://www.youtube.com/@RealPars): short, clear videos on PLCs, ladder logic, and industrial automation
- [AutomationDirect CLICK PLCs](https://www.automationdirect.com/clickplcs): hardware, free programming software, and manuals
- [Rockwell Automation Studio 5000](https://www.rockwellautomation.com/en-us/products/software/factorytalk/designsuite/studio-5000.html): Allen-Bradley programming environment

### Talking to PLCs from Python

Later on, these libraries connect the PLC track to the Python track:

- [pycomm3](https://github.com/ottowayi/pycomm3): read and write tags on Allen-Bradley PLCs over EtherNet/IP
- [pymodbus](https://github.com/pymodbus-dev/pymodbus): Modbus TCP, which CLICK PLCs support
