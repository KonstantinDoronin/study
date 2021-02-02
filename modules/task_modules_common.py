import sys #подключаем модуль sys
print(len((sys.argv)))#выводим на экран количество параметров (в данному случае - python - то есть 1)

import subprocess #импортируем модуль
subprocess.call(["python", "-h"]) #выводим содержимое сообщение со справкой (так как указали  python - h)

