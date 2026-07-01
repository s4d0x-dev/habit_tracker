# The Habit Tracker

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)
![CLI](https://img.shields.io/badge/Interface-CLI-black)
![Status](https://img.shields.io/badge/Status-Active-success)

A lightweight and elegant command-line utility for tracking long-term progress using configurable milestones and visual progress bars.

The Habit Tracker allows users to start a session, track elapsed days, and compare progress against configurable targets through a clean terminal interface powered by **Rich**.

---

## Features

* Clean and readable CLI interface
* Config-driven architecture
* Session start timestamp recording
* Progress visualization using Rich bars
* Automatic elapsed day calculation
* Overflow progress support (`+N`)
* Modular and extensible code structure
* Minimal dependencies

---

## Preview

### Status View

```text
┌──────────────────────────────────────────┐
│ THE HABIT TRACKER v1.0                      │
└──────────────────────────────────────────┘

Date: 2026-06-01
Days: 30

Health
X: ■■■■■■■■■■■■■■■■■■■■■■■■■■■ +5

Learning
PYTHON: ■■■■■■■■■□□□□□□□
```
<!-- 
```text
docs/
├── cli_screenshot.jpg
└── gui_screenshot.jpg
``` -->

<!-- CLI Preview:

![CLI Screenshot](docs/cli_screenshot.jpg)

GUI Preview *(optional)*:

![GUI Screenshot](docs/gui_screenshot.jpg) -->

---

## Installation

Clone the repository:

```bash
git clone https://github.com/s4d0x-dev/habit_tracker.git
cd the-habit-tracker
```

Install dependencies:

```bash
pip install rich
```

---

## Project Structure

```text
the-habit-tracker/
│
├── main.py
├── config.py
├── configs.cfg
├── README.md
└── requirements.txt
```

---

## Configuration

Example `configs.cfg`:

```json
{
    "start": "2026-07-01 10:30:00",

    "health": {
        "x": 30,
        "exercise": 60
    },

    "learning": {
        "python": 120,
        "cpp": 90
    }
}
```

### Rules

* `start` → Session starting timestamp
* Sections → Categories to track
* Keys → Individual targets
* Values → Maximum progress values

---

## Usage

Start a session:

```bash
python main.py --start
```

or

```bash
python main.py -s
```

Check current progress:

```bash
python main.py --check
```

or

```bash
python main.py -c
```

Show help:

```bash
python main.py --help
```

##### You can edit the config file `configs.cfg` to add or remove categories and targets as needed.  

---

## Example Output

```bash
THE HABIT TRACKER v1.0

Date: 2026-06-01
Days: 30

Health
X: ■■■■■■■■■■■■■■■■■■■■■■■■■■■ +5

Learning
PYTHON: ■■■■■■■■■□□□□□□□
```

---

## Requirements

* Python 3.10+
* rich

Install all requirements:

```bash
pip install -r requirements.txt
```

---

<!-- ## Roadmap

* [ ] Export reports
* [ ] Config validation
* [ ] GUI edition
* [ ] Statistics and analytics
* [ ] Theme customization
* [ ] Persistent history

--- -->

## Contributing

Contributions, improvements, and suggestions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Open a Pull Request

---

## License

This project is released under the MIT License.

---

## Contact

Author: **Mr. FBA / S4D0X**

GitHub: `https://github.com/s4d0x-dev`
