import os

os.system('python ./mlc/src/main.py -i ./configs -o ./client/mg -l py -f xml -side client -data ./configs/data -data_out ./client/assets')
os.system('python ./mlc/src/main.py -i ./configs -o ./server/mg -l py -f xml -side server -data ./configs/data -data_out ./server')
os.system('python ./mlc/src/main.py -i ./configs -o ./server_php/mg -l php -f xml -side server -data ./configs/data -data_out ./server_php')
