import os
import random, time
from solver import _Solver

class Solver_Greedy(_Solver):

	def greedy_algo(var_data):

		self.x_ik = [[0 for i in range(self.K)] for j in range(self.N)]
		cam_list = []
		self.y_cd = [[] for i in range(self.Days)]
		self.z_id = [[0 for i in range(self.Days)] for j in range(self.N)]

        priority_score = np.array([self.Pk[i] + self.MinConseq*self.Ck[i] for i in range(len(self.K)))
        self.sort_order = np.argsort(priority_score)

        priority_score_cross = np.array([sum(m) for i in range(self.Mij)])
        self.sort_order_cross = np.argsort(priority_score_cross)

		while any(0 in z for z in z_id):
            

	def find_feasable_assigments(id):
        all_ass = []
        while 0 in self.z_id[id]:
            for i in range(self.K):
                poss_covered = [(self.Rk[i] > m) for m in self.Mij[id]] 
                max_covered = [(poss_covered[j-1]+poss_covered[(j+1)%self.Days])*poss_covered[j] for j in range(self.N)]
            
	def main():
        inp = read_data(self.input_file)

if __name__ == "__main__":
    greed = Solver_Greedy(instance)
    greed.main()
