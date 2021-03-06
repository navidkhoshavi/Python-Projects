# edram cache power characteristics

def edram_power(tech_node, cache_size, implementation, temperature):
    # L1 and L2 power
    if tech_node == '45nm':
        if temperature == '75C':
            l1_d_leakage_power = 19.10
            l1_d_read_energy = 0.97
            l1_d_write_energy = 0.99
                    
            l1_i_leakage_power = 19.10
            l1_i_read_energy = 0.97
            l1_i_write_energy = 0.99
                    
            l2_leakage_power = 51.57
            l2_read_energy = 0.56
            l2_write_energy = 0.70
    elif tech_node == '32nm':
        if temperature == '75C':
            l1_d_leakage_power = 32.85
            l1_d_read_energy = 0.68
            l1_d_write_energy = 0.69
            
            l1_i_leakage_power = 32.85
            l1_i_read_energy = 0.68
            l1_i_write_energy = 0.69
                    
            l2_leakage_power = 75.91
            l2_read_energy = 0.32
            l2_write_energy = 0.40
        elif temperature == '95C':
            l1_d_leakage_power = 40.00
            l1_d_read_energy = 0.53
            l1_d_write_energy = 0.53
            
            l1_i_leakage_power = 40.00
            l1_i_read_energy = 0.53
            l1_i_write_energy = 0.53
            
            l2_leakage_power = 99.28
            l2_read_energy = 0.22
            l2_write_energy = 0.27
    elif tech_node == '22nm':
        if temperature == '75C':
            l1_d_leakage_power = 50.99
            l1_d_read_energy = 0.37
            l1_d_write_energy = 0.38
            
            l1_i_leakage_power = 50.99
            l1_i_read_energy = 0.37
            l1_i_write_energy = 0.38
            
            l2_leakage_power = 118.87
            l2_read_energy = 0.18
            l2_write_energy = 0.22

    # L3 power
    if tech_node == '45nm':
        if cache_size == '32MB':
            if implementation == 'lp':
                if temperature == '75C':
                    l3_leakage_power = 34.96
                    l3_read_energy = 2.99
                    l3_write_energy = 3.08
                    l3_tag_energy = 0.06
                    l3_refresh_energy = 0.03
                    l3_overhead_power = 0
    elif tech_node == '32nm':
        if cache_size == '16MB':
            if implementation == 'lp':
                if temperature == '75C':
                    l3_leakage_power = 31.03
                    l3_read_energy = 1.02
                    l3_write_energy = 1.03
                    l3_tag_energy = 0.01
                    l3_refresh_energy = 0.02
                    l3_overhead_power = 0
        elif cache_size == '32MB':
            if implementation == 'lp':
                if temperature == '75C':
                    l3_leakage_power = 49.00
                    l3_read_energy = 1.74
                    l3_write_energy = 1.79
                    l3_tag_energy = 0.02
                    l3_refresh_energy = 0.03
                    l3_overhead_power = 0
                elif temperature == '95C':
                    l3_leakage_power = 66.48
                    l3_read_energy = 1.74
                    l3_write_energy = 1.75
                    l3_tag_energy = 0.02
                    l3_refresh_energy = 0.03
                    l3_overhead_power = 0
        elif cache_size == '64MB':
            if implementation == 'lp':
                if temperature == '75C':
                    l3_leakage_power = 78.74
                    l3_read_energy = 2.38
                    l3_write_energy = 2.50
                    l3_tag_energy = 0.04
                    l3_refresh_energy = 0.03
                    l3_overhead_power = 0
        elif cache_size == '80MB':
            if implementation == 'lp':
                if temperature == '75C':
                    l3_leakage_power = 85.72
                    l3_read_energy = 2.45
                    l3_write_energy = 2.54
                    l3_tag_energy = 0.04
                    l3_refresh_energy = 0.03
                    l3_overhead_power = 0
        elif cache_size == '96MB':
            if implementation == 'lp':
                if temperature == '75C':
		    # obtained from DESTINY under Write Energy delay optimization
		    #128MB leakage power = 14425.718mW
		    #64MB leakage power = 7238.372mW
		    #96MB leakage power = (14425.718+7238.372)/2 = 10832.045mW
		    #96MB leakage power per bank = [10832.045*time(0.159872)]/ # of bank (16)= 1731.740 / 16 = 108.233
                    l3_leakage_power = 108.23 #mW per bank, my_chg

		    #128MB read energy = 1.203nJ
		    #64MB read energy = 0.860nJ
		    #96MB read energy = (0.860nJ + 1.203nJ) / 2
                    l3_read_energy = 1.46 #my_chg

		    #128MB write energy = 1.239nJ
		    #64MB write energy = 0.850nJ
                    l3_write_energy = 1.04 #my_chg

		    #128MB tag energy = 0.039nJ
		    #64MB tag energy = 0.028nJ
                    l3_tag_energy = 0.03 #my_chg


		    #128MB Cache Refresh Dynamic Energy = 9855.519nJ per bank
		    #64MB Cache Refresh Dynamic Energy = 4933.120nJ per bank
		    #96MB Refresh Dynamic Energy = (9855.519nJ + 4933.120nJ) / 2 = 7394.3nJ per bank
                    l3_refresh_energy = 7394.3 #nJ per bank
                    l3_overhead_power = 0
        elif cache_size == '112MB':
            if implementation == 'lp':
                if temperature == '75C':
                    l3_leakage_power = 91.90
                    l3_read_energy = 2.58
                    l3_write_energy = 2.70
                    l3_tag_energy = 0.05
                    l3_refresh_energy = 0.04
                    l3_overhead_power = 0
        elif cache_size == '120MB':
            if implementation == 'lp':
                if temperature == '75C':
                    l3_leakage_power = 94.17
                    l3_read_energy = 2.63
                    l3_write_energy = 2.75
                    l3_tag_energy = 0.05
                    l3_refresh_energy = 0.04
                    l3_overhead_power = 0
    elif tech_node == '22nm':
        if cache_size == '32MB':
            if implementation == 'lp':
                if temperature == '75C':
                    l3_leakage_power = 71.75
                    l3_read_energy = 0.92
                    l3_write_energy = 0.96
                    l3_tag_energy = 0.02
                    l3_refresh_energy = 0.03
                    l3_overhead_power = 0

    return (l1_d_leakage_power,
            l1_d_read_energy,
            l1_d_write_energy,
            l1_i_leakage_power,
            l1_i_read_energy,
            l1_i_write_energy,
            l2_leakage_power,
            l2_read_energy,
            l2_write_energy,
            l3_leakage_power,
            l3_read_energy,
            l3_write_energy,
            l3_tag_energy,
            l3_refresh_energy,
            l3_overhead_power)
