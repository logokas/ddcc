#!/bin/bash

# patches Ren'Py to work with Voice Engines.

# Sanity check first

if  [[ -z "$(cat renpy/renpy/defaultstore.py | grep '_menu = False')" ]]; then

  echo " ----> Patching..."
  echo "_menu = False" >> renpy/renpy/defaultstore.py

  # final output check before exiting
  echo " ---> Patched. Review the following if this is okay."
  cat renpy/renpy/defaultstore.py | grep '_menu = False';
  exit 0

else

  echo " ----> Line exists. Exiting now.";
  exit 0;

fi