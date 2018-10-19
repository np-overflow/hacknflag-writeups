#!/bin/bash

python pyinstxtractor.py give-me-the-flag.exe
pip install uncompyle6
cd give-me-the-flag.exe_extracted
cat give-me-the-flag
