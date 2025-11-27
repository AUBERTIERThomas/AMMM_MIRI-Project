import os
import random
import re

input_file_default = "config.dat"
output_file_default = "instance.dat"

i_var = ["N","K"]
o_var = ["Pk","Rk","Ak","Ck","Mij"]
var_names = i_var + o_var
var_types = ["int","int","vec","vec","vec","vec","mat"]

def read_data(file_name):
    res = []
    with open(file_name, 'r') as file:
        lines = [line.rstrip() for line in file]

        for line in lines:
            spl = line.split('=')
            if len(spl) != 0:
                try:
                    value = int(spl[1].replace(' ','').replace(';',''))
                    res.append(value)
                except:
                    pass
    return res

def gen_data(var_data):
    K, N, MinPrice, MaxPrice, MinCost, MaxCost, MinAutonomy, MaxAutonomy, MinRangeCam, MaxRangeCam, MinRangeCross, MaxRangeCross = var_data
    var_values = [K, N]
    var_values.append(gen_vector(K, MinPrice, MaxPrice, is_int=False))
    var_values.append(gen_vector(K, MinRangeCam, MaxRangeCam, is_int=True))
    var_values.append(gen_vector(K, MinAutonomy, MaxAutonomy, is_int=True))
    var_values.append(gen_vector(K, MinCost, MaxCost, is_int=False))
    var_values.append(gen_matrix(N, MinRangeCross, MaxRangeCross, is_int=True))
    return var_values

def gen_value(min, max):
    return min + random.random()*(max - min)

def gen_vector(n, min, max, is_int=False):
    vect = [0 for i in range(n)]
    rr = max - min
    for i in range(n):
        if is_int:
            vect[i] = random.randint(min, max)
        else:
            vect[i] = round(min + random.random()*rr,2)

    return vect

def gen_matrix(n, min, max, is_int=False):
    matrix = [[0 for i in range(n)] for j in range(n)]
    rr = max - min
    for r in range(n):
        matrix[r][r] = 0
        for c in range(r):
            if is_int:
                matrix[r][c] = random.randint(min, max)
            else:
                matrix[r][c] = round(min + random.random()*rr,2)
            matrix[c][r] = matrix[r][c]
                
    return matrix
            
def write_data(file_name, var_values):
    with open(file_name, 'w') as file:
        for i,v in enumerate(var_names):
            if var_types[i] == "int":
                file.write(v+" = "+str(var_values[i])+";\n")
            elif var_types[i] == "vec":
                file.write(v+" = [")
                for e in var_values[i]:
                    file.write(" "+str(e))
                file.write(" ];\n")
            elif var_types[i] == "mat":
                file.write(v+" = [\n")
                for r in var_values[i]:
                    file.write("[")
                    for e in r:
                        file.write(" "+str(e))
                    file.write(" ]\n")
                file.write(" ];\n")
            file.write("\n")
                
                           
def main():
    try:
        input_file = sys.argv[0]
    except:
        input_file = input_file_default
    try:
        output_file = sys.argv[1]
    except:
        output_file = output_file_default

    print("\33[0;93m"+"Generating instance from ["+input_file+"] :")
    
    inp = read_data(input_file)
    var_values = gen_data(inp)
    write_data(output_file, var_values)

    print("\33[1;32m"+"Instance successfully saved in ["+output_file+"] !")

if __name__ == "__main__":
    try:
        main()
    except:
        print("\33[1;31m"+"Process failed !")