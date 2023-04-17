#!/bin/bash

clear
echo "
      A         VV      VV      fff      SSSSSS       y   y   sss   t    ee     m   m    
     AAA        VV      VV     ff ff    SS     SS      y y   ss    ttt  eeeee  m m m m   
    AA AA       VV      VV     ff ff   SS       SS      y     sss   t   e      m m m m   
   AA   AA       VV    VV      ff      SS              y     sss    tt   eee   m  m  m   
  AA     AA      VV    VV      ff       SSSSSSSS     ----------------------------------
 AAAAAAAAAAA      VV  VV     ffffff            SS      ee    r r   v   v   ee    r rr   
AA         AA      V  V        ff      SS      SS     eeeee  rr r  v   v  eeeee  rr  r   
AA         AA      VVVV        ff       SS    SS      e      r      v v   e      r      
AA         AA       VV         ff        SSSSSS        eee   r       v     eee   r     "

pythoncheck=$(python -c"import sys; print(sys.version_info.major)")
brewcheck=$(brew -v)
pidofcheck=$(pidof -v)
if [ $pythoncheck -ne 3 ]; then
  if [$brewcheck -eq "./install.sh: line 19: brew: command not found"]; then
    read '[☐] Requirement: "BREW" package is not installed! Would you like to install the package?
    [Y/N] >>> ' installbrew
    if [installbrew -eq "Y"]; then
      echo '[☑︎]  Installing: "BREW"'
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    else
      echo '
      
      
      - AVfS Ended -'
      exit 1
    fi
  else
    echo '[☑︎]     Success: "BREW" was successfully imported!'
  fi
else
  if [$pidofcheck -eq "./install.sh: line 36: pidof: command not found"]; then
    read '[☐] Requirement: "PIDOF" package is not installed! Would you like to install the package?
    [Y/N] >>> ' installpidof
    if [installpidof -eq "Y"]; then
      echo '[☑︎]  Installing: "PIDOF"'
      brew install pidof
    else
      echo '
      
      
      - AVfS Ended -'
      exit 1
    fi
  else
    echo '[☑︎]     Success: "PIDOF" was successfully imported!'
  fi
  if [$pythoncheck -eq "./install.sh: line 52: python: command not found"]; then
    read '[☐] Requirement: "PYTHON" package is not installed! Would you like to install the package?
    [Y/N] >>> ' installpython
    if [installpython -eq "Y"]; then
      echo '[☑︎]  Installing: "PYTHON"'
      brew install python
    else
      echo '
      
      
      - AVfS Ended -'
      exit 1
    fi
  else
    echo '[☑︎]     Success: "PYTHON" was successfully imported!'
  fi
fi

exit 0
