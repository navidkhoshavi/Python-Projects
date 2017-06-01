__author__ = 'Navid Khoshavi'

import sys
import re

temp = 0
list = []
list_output = []
list_CG_already_buffered = []
D_FF_input_list = []

newfile = open('b19_synthesized_revise.v', "w")
replica = open('replica.v', "w")
buffer = open('buffer.v', "w")

i = 0
j = 0
with open('b19_CG_name.txt', 'r') as criticalGates:
    for line in criticalGates:
        list_output.append(line.split()[0])
criticalGates.close()

with open('b19_synthesized.v') as benchmark:
    for lb in benchmark:
        if j == len(list_output):
            break
        CG = list_output[j]
        if CG in lb.split():
            output_pattern = ".ZN("
            for word in lb.split():
                if word.startswith(output_pattern):
                    tmp = word.replace(".ZN","")
                    list.append(tmp)
                    #list_CG.append(CG)
                    j += 1
                    break
        elif CG not in lb.split():
            D_FF_pattern = ".D"
            for word in lb.split():
                if word.startswith(D_FF_pattern):
                    n_tmp = word.replace(".D","")
                    n_tmp = n_tmp.replace("),",")")
                    D_FF_input_list.append(n_tmp)
benchmark.close()


j = 0
with open('b19_synthesized.v') as benchmark:
    output_pattern = ".ZN("
    input_pattern1 = ".A1"
    input_pattern2 = ".A2"
    input_pattern4 = ".A("
    input_pattern3 = ".D"
    two_pre_word = 'a'
    pre_word = 'b'
    for lb in benchmark:
        flag = 'false'
        if j == len(list_output):
            newfile.write(lb)
        else:
            CG = list_output[j]
            if CG in lb.split():
                # a) change name of gate to "name"_CG1 and change the output of it to .ZN("name"_CG1)
                # b) check the inputs of the gate as the output of other CG
                # if they exist in the output list,
                    # 1) change that input to "name"_CG1
                    # 2) go to that CG line and execute previous steps
                # a)
                tm = CG+"_CG1"
                lb = lb.replace(CG, tm)
                for word in lb.split():
                    if word.startswith(output_pattern):
                        n_tmp = word.replace(".ZN","")
                        if n_tmp in D_FF_input_list:
                            tm2 = n_tmp.replace(")","_CG1)")
                            TBUF1 = "TBUF_X1 TBUF_"+CG+"_1 (.A"+tm2+",.EN(ENABLE_CGs_1), .Z"+n_tmp+");"
                            tm3 = n_tmp.replace(")","_CG2)")
                            TBUF2 = "TBUF_X1 TBUF_"+CG+"_2 (.A"+tm3+",.EN(ENABLE_CGs_2), .Z"+n_tmp+");"
                            buffer.write(TBUF1+'\n')
                            buffer.write(TBUF2+'\n')
                        else:
                            tm = word.replace(")","")
                            tm += "_CG1)"
                            lb = lb.replace(word, tm)
                    elif word.startswith(input_pattern1):
                        tm = word.replace(".A1","")
                        tm = tm.replace("),",")")
                        if tm in list:
                            tm = tm.replace(")","_CG1)")
                            tm = ".A1"+tm+","
                            lb = lb.replace(word, tm)
                    elif word.startswith(input_pattern2):
                        tm = word.replace(".A2","")
                        tm = tm.replace("),",")")
                        if tm in list:
                            tm = tm.replace(")","_CG1)")
                            tm = ".A2"+tm+","
                            lb = lb.replace(word, tm)
                replica.write(lb)
                j += 1
                #replica.close()

            elif CG not in lb.split():
                newfile.write(lb)
                for word in lb.split():
                    # find the CG outputs that go to non-CG inputs
                    if word.startswith(input_pattern1):
                        tm = word.replace(".A1","")
                        tm = tm.replace("),",")")
                        if tm in list:
                            # find the associated CG gate that its output is tm
                            CG_index = list.index(tm)
                            assoc_CG = list_output[CG_index]
                            if assoc_CG not in list_CG_already_buffered:
                                list_CG_already_buffered.append(assoc_CG)
                                tm2 = tm.replace(")","_CG1)")
                                TBUF1 = "TBUF_X1 TBUF_"+assoc_CG+"_1 (.A"+tm2+",.EN(ENABLE_CGs_1), .Z"+tm+");"
                                tm3 = tm.replace(")","_CG2)")
                                TBUF2 = "TBUF_X1 TBUF_"+assoc_CG+"_2 (.A"+tm3+",.EN(ENABLE_CGs_2), .Z"+tm+");"
                                buffer.write(TBUF1+'\n')
                                buffer.write(TBUF2+'\n')
                            else:
                                break

                    elif word.startswith(input_pattern2):
                        tm = word.replace(".A2","")
                        tm = tm.replace("),",")")
                        #if tm == '(n54869)':
                            #i += 1
                        if tm in list:
                            # find the associated CG gate that its output is tm
                            CG_index = list.index(tm)
                            assoc_CG = list_output[CG_index]
                            if assoc_CG not in list_CG_already_buffered:
                                list_CG_already_buffered.append(assoc_CG)
                                tm2 = tm.replace(")","_CG1)")
                                TBUF1 = "TBUF_X1 TBUF_"+assoc_CG+"_1 (.A"+tm2+",.EN(ENABLE_CGs_1), .Z"+tm+");"
                                tm3 = tm.replace(")","_CG2)")
                                TBUF2 = "TBUF_X1 TBUF_"+assoc_CG+"_2 (.A"+tm3+",.EN(ENABLE_CGs_2), .Z"+tm+");"
                                buffer.write(TBUF1+'\n')
                                buffer.write(TBUF2+'\n')
                            else:
                                break

                    elif word.startswith(input_pattern3):
                        tm = word.replace(".D","")
                        tm = tm.replace("),",")")
                        if tm in list:
                            # find the associated CG gate that its output is tm
                            assoc_CG = two_pre_word
                            if assoc_CG not in list_CG_already_buffered:
                                list_CG_already_buffered.append(assoc_CG)
                                tm2 = tm.replace(")","_CG1)")
                                TBUF1 = "TBUF_X1 TBUF_"+assoc_CG+"_1 (.A"+tm2+",.EN(ENABLE_CGs_1), .Z"+tm+");"
                                tm3 = tm.replace(")","_CG2)")
                                TBUF2 = "TBUF_X1 TBUF_"+assoc_CG+"_2 (.A"+tm3+",.EN(ENABLE_CGs_2), .Z"+tm+");"
                                buffer.write(TBUF1+'\n')
                                buffer.write(TBUF2+'\n')
                            else:
                                break

                    elif word.startswith(input_pattern4):
                        tm = word.replace(".A","")
                        tm = tm.replace("),",")")
                        if tm in list:
                            # find the associated CG gate that its output is tm
                            CG_index = list.index(tm)
                            assoc_CG = list_output[CG_index]
                            if assoc_CG not in list_CG_already_buffered:
                                list_CG_already_buffered.append(assoc_CG)
                                tm2 = tm.replace(")","_CG1)")
                                TBUF1 = "TBUF_X1 TBUF_"+assoc_CG+"_1 (.A"+tm2+",.EN(ENABLE_CGs_1), .Z"+tm+");"
                                tm3 = tm.replace(")","_CG2)")
                                TBUF2 = "TBUF_X1 TBUF_"+assoc_CG+"_2 (.A"+tm3+",.EN(ENABLE_CGs_2), .Z"+tm+");"
                                buffer.write(TBUF1+'\n')
                                buffer.write(TBUF2+'\n')
                            else:
                                break

                    if flag == 'false':
                        two_pre_word = pre_word
                        pre_word = word
                        flag = 'true'
                    elif flag == 'true':
                        two_pre_word = pre_word
                        pre_word = word
                        flag = 'false'
            else:
                newfile.write(lb)


benchmark.close()
criticalGates.close()
replica.close()
buffer.close()







