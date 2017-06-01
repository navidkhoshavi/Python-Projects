__author__ = 'Navid Khoshavi'
import shutil
import os

if __name__ == "__main__":
    

 
	root_directory = os.getcwd()
	for i in range(27,88):
		#print os.system("pwd")
		#os.chdir(root_directory+ "/"+str(i))
		#print os.system("pwd")
		#os.system("hspice -i C880_CCP_N2_D0_P10.sp -o C880_CCP_N2_D0_P10.sp")
		#os.rename("C880_CCP_N2_D0_P10.radeg109","C880_CCP_N2_D0_P10.radeg109-old")
		#os.rename("C880_CCP_N2_D0_P10.sp.radeg109","C880_CCP_N2_D0_P10.radeg109")
	
		#os.chdir(root_directory)
		#os.mkdir(str(i)+"-1")
		shutil.copyfile(root_directory+ "/"+str(i)+"-1"+"/read_mt.tcl", root_directory+ "/" +str(i+1)+"-1"+"/"+"read_mt.tcl")
		shutil.copyfile(root_directory+ "/"+str(i)+"-1"+"/P_rise_time.tcl", root_directory+ "/" +str(i+1)+"-1"+"/"+"P_rise_time.tcl")
		shutil.copyfile(root_directory+ "/"+str(i)+"-1"+"/P_fall_time.tcl", root_directory+ "/" +str(i+1)+"-1"+"/"+"P_fall_time.tcl")
		shutil.copyfile(root_directory+ "/"+str(i)+"-1"+"/Red_fall_time.tcl", root_directory+ "/" +str(i+1)+"-1"+"/"+"Red_fall_time.tcl")
		shutil.copyfile(root_directory+ "/"+str(i)+"-1"+"/Red_rise_time.tcl", root_directory+ "/" +str(i+1)+"-1"+"/"+"Red_rise_time.tcl")
		shutil.copyfile(root_directory+ "/"+str(i)+"-1"+"/P_cct.tcl", root_directory+ "/" +str(i+1)+"-1"+"/"+"P_cct.tcl")
		os.system("tclsh read_mt.tcl;tclsh P_rise_time.tcl;tclsh P_fall_time.tcl;tclsh Red_fall_time.tcl;tclsh Red_rise_time.tcl;tclsh P_cct.tcl")
		
		
	
	#for j in range(0,110):
	#	shutil.copyfile(root_directory+ "/"+str(i)+"/C880_CCP_N2_D0_P10.sp.mt"+str(j)+"@ra", root_directory+ "/" +str(i)+"-1"+"/"+"/C880_CCP_N2_D0_P10.sp.mt"+str(j)+"@ra")