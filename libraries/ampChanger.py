import sys

# Usage:   python ampChanger.py W_bf.txt 0.5 W_bf_half.txt

if __name__ == "__main__":
    try:
        f = open(sys.argv[1], "r")
    except IOError:
        log = "Error! "+textName+" is not found in current folder:\n"+os.getcwd()+"\nProgram exits.\n"
        print(log)
        sys.exit()

    lines = f.readlines()

    try:
        ampMod = float(sys.argv[2])
    except ValueError:
        print("An amplifier should be given. Program exits.")
        sys.exit()

    out = []
    for line in lines:
        line = line.strip()

        if line == "":
            continue
        
        [name, values] = line.split('=')
        values = values[1:-1].split(',')
        amplitude = values[0]
        amplitude = float(amplitude.strip())
        amplitude = amplitude * ampMod
        values[0] = str(amplitude)
        values = '('+ ','.join(values) + ')'
        out.append(name+'='+values+'\n')

    try:
        f = open(sys.argv[3], 'w')
        f.writelines(out)
        f.close()
    except:
        print('cannot write to ', sys.argv[3])
