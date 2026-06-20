#!/bin/bash                                                                                                                                                                    

check_process() {
  if pgrep -x "$1" > /dev/null; then                                                                                                                                       
          echo "$1 работает"                                                                                                                                               
  else                                                                                                                                                                           
          echo "$1 НЕ работает"                                                                                                                                            
  fi
}
                                                                                                                                                                               
if [ $# -eq 0 ]; then 
	echo "Введите аргумент"
	exit 1
fi

for PROCESS in "$@"; do
  check_process "$PROCESS"
done
