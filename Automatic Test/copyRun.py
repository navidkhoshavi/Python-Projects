__author__ = 'Navid Khoshavi'
import shutil
import os

if __name__ == "__main__":
    

 
	root_directory = os.getcwd()
	for i in range(1,110):
		print os.system("pwd")
		os.chdir(root_directory+ "/"+str(i))
		print os.system("pwd")
		os.system("hspice -i C880_CCP_N2_D0_P10.sp -o C880_CCP_N2_D0_P10.sp")
		os.rename("C880_CCP_N2_D0_P10.radeg109","C880_CCP_N2_D0_P10.radeg109-old")
		os.rename("C880_CCP_N2_D0_P10.sp.radeg109","C880_CCP_N2_D0_P10.radeg109")
	
		os.chdir(root_directory)
		os.mkdir(str(i+1))
		shutil.copyfile(root_directory+ "/"+str(i)+"/C880_CCP_N2_D0_P10.radeg109", root_directory+ "/" +str(i+1)+"/"+"C880_CCP_N2_D0_P10.radeg109")
		shutil.copyfile(root_directory+ "/"+str(i)+"/C880_CCP_N2_D0_P10.sp", root_directory+ "/" +str(i+1)+"/"+"C880_CCP_N2_D0_P10.sp")
		shutil.copyfile(root_directory+ "/"+str(i)+"/_45nm_nominal_bulkCMOS.pm", root_directory+ "/" +str(i+1)+"/"+"_45nm_nominal_bulkCMOS.pm")
        	shutil.copyfile(root_directory+ "/"+str(i)+"/c880_org.vec",root_directory+"/"+str(i+1)+"/"+"c880_org.vec")
		shutil.copyfile(root_directory+ "/"+str(i)+"/hybridmosra.lib", root_directory+ "/" +str(i+1)+"/"+"hybridmosra.lib")
		shutil.copyfile(root_directory+ "/"+str(i)+"/measure_stats.sp", root_directory+ "/" +str(i+1)+"/"+"measure_stats.sp")
		shutil.copyfile(root_directory+ "/"+str(i)+"/NangateOpenCellLibrary_ra.sp", root_directory+ "/" +str(i+1)+"/"+"NangateOpenCellLibrary_ra.sp")
		shutil.copyfile(root_directory+ "/"+str(i)+"/NangateOpenCellLibrary_supply.sp", root_directory+ "/" +str(i+1)+"/"+"NangateOpenCellLibrary_supply.sp")