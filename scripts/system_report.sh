#!/bin/bash

echo "=== System Report ==="
echo "Дата $(date)"
echo "Пользователь $(whoami)"
echo ""
echo "Проверка процессов:"


FOUND=0
NOT_FOUND=0

check_process() {                                                                                                                                                              

  if pgrep -x "$1" > /dev/null; then                                                                                                                                           
          echo "$1 работает"
	((FOUND++))                                                                                                                                                   
  else                                                                                                                                                                         
          echo "$1 НЕ работает"                                                                                                                                                
 	((NOT_FOUND++))
 fi                                                                                                                                                                           
}                                                                                                                                                                              
                                                                                                                                                                                 
if [ $# -eq 0 ]; then                                                                                                                                                          
        echo "Введите аргумент"                                                                                                                                                
        exit 1                                                                                                                                                                 
fi                                                                                                                                                                             
                                                                                                                                                                                 
for PROCESS in "$@"; do                                                                                                                                                        
  check_process "$PROCESS"                                                                                                                                                     
done
echo ""
echo "Итого $FOUND работает, $NOT_FOUND не найден"
