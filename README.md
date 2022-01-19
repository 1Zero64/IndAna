# Industrial Analytics

## Team members
Ann-Kathrin Jauk\
Theresa Herr\
Kevin Hilzinger\
Niko Kauz


# Project
Optimale von Bestellpunkt und Bestellrhytmus

## Description


## Input


## Output


## Used ML Models
WIP

### Linear Regression

### SARIMAX

### RNN

## Using Setuptools/Python Egg
The file setup.py will look for packages (directories with __ init__.py files) and install them as modules.

- Go to terminal and there to project main directory (.../IndAna)
- Type "pip install -e ." (the e-flag updates the install when changes to code are made)
- Folder "IndAna.egg-info" is added to project (already in gitignore)
- In this new folder in file top_level.txt you'll find hierarchically highest modules
- Those are root for imports, e.g. "import DataProcessing.DataGenerators". Always use when importing!! 
