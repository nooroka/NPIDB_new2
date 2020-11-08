fileuni = open("b_pfam_domain_types3.txt", "r")
file4 = open("interaction_mode_domain_new.txt","w")
for line in fileuni:
    if "INSERT INTO `b_pfam_domain_types` VALUES" in line:
        line = line.split()
        lineintmode = line[4].split(",")
        lineintmode[4] = lineintmode[4].replace("|", " ")
        lineintmode[4] = lineintmode[4].split()
        lineintmode[4] = sorted(lineintmode[4])
        if "A0A0M3KL05" in lineintmode[1]:
            print(lineintmode[4])

        lineintmode[4] = ' '.join(map(str,lineintmode[4]))
        file4.write(str(lineintmode[1][1:-1])+"_"+str(lineintmode[2])+"-"+str(lineintmode[3])+"\t"+str(lineintmode[4][3:])+"\n")
file4.close()
fileuni.close()
 





 
