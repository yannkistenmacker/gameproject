#!/bin/sh

# Execute prepara_banco.py and wait for it to finish
python prepara_banco.py

# Execute jogoteca.py in the background
python jogoteca.py &

# Keep the container running by tailing /dev/null
tail -f /dev/null
