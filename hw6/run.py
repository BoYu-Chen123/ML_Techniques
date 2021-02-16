import os
for i in range(100):
	cmd = "python3 ML_hw6_program.py " + str(i) + " &> log_" + str(i) + ".txt &"
	os.system(cmd)