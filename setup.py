# python3 GeneratorWeather.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Ann-Kathrin Jauk
# Description: Build Python Egg, module management
# how to:
# - Go to terminal in project directory
# - type command "pip install -e ."
# ===========================================================================================

from setuptools import setup

setup(name='IndAna',
version='0.1.0',
description='IndAna',
license='MIT',
packages=setuptools.find_packages(),
include_package_data=True,
zip_safe=False)