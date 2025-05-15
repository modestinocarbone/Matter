# Matter

Matter is a simple command-line tool that reads structured data from a specially formatted .txt file and plots it using matplotlib.

## Features

* Parses parameters and datasets from a `.txt` file with a custom format
* Supports line plots (connected) and scatter plots (scatter)
* Automatically labels axes, sets title, scales (linear/log)
* Handles multiple data series in one plot
* Installs as a shell command for easy access

---

## File Format

The input file must be a plain text file with the following structure:

1. **Parameter Section (before `#`)**
   Use lines starting with `\` to define plotting parameters:
   Example:

   ```
   \plottype: connected
   \x-lab: "Time (s)"
   \y-lab: "Amplitude"
   \title: "Signal Data"
   ```

2. **Data Section (after a line with just `#`)**
   Data points should be pairs of numbers (x y), space-separated.
   Each line can contain multiple pairs.
   Example:

   ```
   #
   0 1 0 2 
   1 4 1 5
   2 7 2 7
   ```

This example would create two data series:

* Series 1: (0,1,2), (1,4,7)
* Series 2: (0,1,2), (2,5,7)

---

## Installation

Make sure you have Python 3 and `matplotlib` installed.

To install `matter` as a command in your system:

```bash
make install
```

This will:

* Ensure the script has a shebang
* Make it executable
* Copy it to `~/.local/bin/matter`

Make sure `~/.local/bin` is in your `PATH`.

---

## Usage

```bash
matter datafile.txt
```

If the file is correctly formatted, a plot will be displayed based on the data and parameters defined in it.

---


## Requirements

* Python 3
* matplotlib
* numpy

Install dependencies with:

```bash
pip install matplotlib numpy
```
