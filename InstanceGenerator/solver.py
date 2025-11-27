class _Solver(object):
    def __init__(self, file_name):
		res = []
		is_reading_mat = False
		curr_elem = 0
		curr_i = 0
		
		with open(file_name, 'r') as file:
		    lines = [line.rstrip() for line in file]

		    for line in lines:
		        spl = line.split(' ')
		        if is_reading_mat:
		            if '[' in line:
		                mat_line = []
		                for s in spl:
		                    try:
		                        new_val = i_types[curr_i](s)
		                        mat_line.append(new_val)
		                    except:
		                        pass
		                curr_elem.append(mat_line)

		        else:
		            if not len(line):
		                continue
		            if line[-1] == "[":
		                curr_elem = []
		                is_reading_mat = True
		                continue
		            if '[' in line:
		                curr_elem = []
		                for s in spl:
		                    try:
		                        new_val = i_types[curr_i](s)
		                        curr_elem.append(new_val)
		                    except:
		                        pass
		            else:
		                curr_elem = i_types[curr_i](spl[2].replace(';',''))
		        
		        if line[-1] == ";":
		            res.append(curr_elem)
		            curr_i += 1
		            is_reading_mat = False

        self.N, self.K, self.Pk, self.Rk, self.Ak, self.Ck, self.Mij = var_data
        
		self.MinConseq = 2
		self.Days = 7

        self.input_file_default = instance
        self.i_types = [int,int,float,int,int,float,int]
