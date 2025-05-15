#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import os

if len(sys.argv) < 2:
    print("Usage: matter filename.txt")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"Error: the file '{file_path}' does not exist or is not accessible.")
    sys.exit(1)

params = {
    "plottype": "connected",
    "x-lab": "X",
    "y-lab": "Y",
    "x-fontsize": 12,
    "y-fontsize": 12,
    "title": "",
    "xscale": "linear",
    "yscale": "linear"
}

labels = {}  # Dizionario per le etichette delle serie
data_sets = [] 
data_section = False

try:
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if not line or (line.startswith('#') and not data_section):
                if line == "#":
                    data_section = True
                continue

            if not data_section:
                if line.startswith('\\'):
                    try:
                        key, value = line[1:].split(':', 1)
                        value = value.strip().strip('"')
                        key = key.strip()
                        if 'fontsize' in key:
                            value = int(value)
                        if key.startswith("label"):
                            try:
                                index = int(key[5:]) - 1
                                labels[index] = value
                            except ValueError:
                                continue
                        else:
                            params[key] = value
                    except ValueError:
                        continue
            else:
                try:
                    parts = line.split()
                    if len(parts) % 2 == 0:
                        for i in range(0, len(parts), 2):
                            x_val = float(parts[i])
                            y_val = float(parts[i + 1])
                            if len(data_sets) <= i // 2:
                                data_sets.append(([], []))
                            data_sets[i // 2][0].append(x_val)
                            data_sets[i // 2][1].append(y_val)
                    else:
                        print(f"Ignored line (odd number of columns): {line}")
                except (IndexError, ValueError):
                    continue
except Exception as e:
    print(f"Error reading file: {e}")
    sys.exit(1)

if not data_sets:
    print("No data found to plot!")
    sys.exit(1)
else:
    print(f"Data sets collected: {len(data_sets)}")

# Axis settings
if params.get("xscale") == "log":
    plt.xscale("log")
if params.get("yscale") == "log":
    plt.yscale("log")

# Plotting the datasets
for i, (x, y) in enumerate(data_sets):
    label = labels.get(i, f"Series {i+1}")
    if params["plottype"] == "connected":
        plt.plot(x, y, label=label, marker='')
    elif params["plottype"] == "scatter":
        plt.scatter(x, y, label=label)
    else:
        print(f"Plot type '{params['plottype']}' not recognized. Using line plot.")
        plt.plot(x, y, label=label)

# Labels and title
plt.xlabel(params["x-lab"], fontsize=params["x-fontsize"])
plt.ylabel(params["y-lab"], fontsize=params["y-fontsize"])
plt.title(params["title"])
plt.grid(True)
plt.legend()
plt.show()
