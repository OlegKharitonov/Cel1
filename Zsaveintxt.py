
def save_txt(file, x=list):
    with open(file, 'a+') as myfile:
        for line in x:
            myfile.write(line + '\n')
