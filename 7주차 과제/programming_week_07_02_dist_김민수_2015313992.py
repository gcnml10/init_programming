from pathlib import Path

def read_int_sum(dirpath):
    int_sum = 0
    ### your code here ###
    path = Path(dirpath)
    for tx in path.iterdir():
        if tx.suffix == '.txt':
            with tx.open(mode='r', encoding='utf-8') as f:
                for line in f.readlines():
                    for i in line:
                        try:
                            int_sum += int(i)
                        except:
                            pass
    return int_sum




### do not edit here ###

dirpath = Path('./text_dir')
print('정수의 총합:',read_int_sum(dirpath))
        
