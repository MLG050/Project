from time import *
def pattern_name():
    # global Name
    # global list2
    for i in range(len(Name)):
        # A
        if Name[i]=="A":
            print_A=[[ " "for j in range(6) ]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  ((col==0 or col==5) and row!=0) or row==3 or (row==0 and (col!=0 and col!=5)):
                        print_A[row][col]="#"
            list2.append(print_A)  
        elif Name[i]==None:
            print_=[[ "   "for j in range(6)]for i in range(7)]
            list2.append(print_)

        # B
        elif Name[i]=="B":
            print_B=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0) or ((col==5) and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<5)):
                        print_B[row][col]="#"
            list2.append(print_B) 
        #C    

        elif Name[i]=="C":
            print_C=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col==0 and (row!=0 and row!=6)) or ((row==0 or row==6) and col>0)):
                        print_C[row][col]="#"
            list2.append(print_C) 
        #D
        elif Name[i]=="D":
            print_D=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or ((row==0 or row==6) and (col<5)) or ((col==5) and(row!=0 and row!=6))  :
                        print_D[row][col]="#"
            list2.append(print_D) 

        #E
        elif Name[i]=="E":
            print_E=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or (row==0 or row==3 or row==6)  :
                        print_E[row][col]="#"
            list2.append(print_E) 
        #F
        elif Name[i]=="F":
            print_F=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or (row==0 or row==3 )  :
                        print_F[row][col]="#"
            list2.append(print_F) 

        #G
        elif Name[i]=="G":
            print_G=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==0) or (col==4 and(row!=1 and row!=2)) or  ((row==0 or row==6 ) and (col>0 and col<4 )) or (row==3 and (col==3 or col==5))  :
                        print_G[row][col]="#"
            list2.append(print_G) 

        #H

        elif Name[i]=="H":
            print_H=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or col==5 or row==3  :
                        print_H[row][col]="#"
            list2.append(print_H)

        #  I

        elif Name[i]=="I":
            print_I=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==2 or((row==0 or row==6) and col!=5) :
                        print_I[row][col]="#"
            list2.append(print_I) 

        # J

        elif Name[i]=="J":
            print_J=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  col==2 or (row==0 and col!=5) or (row==6 and col<2):
                        print_J[row][col]="#"
            list2.append(print_J) 
        # K   
        elif Name[i]=="K":
            print_K=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  col==0 or row+col==3 or row-col==3:
                        print_K[row][col]="#"
            list2.append(print_K) 
        # L
        elif Name[i]=="L":
            print_L=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  col==0 or row==6:
                        print_L[row][col]="#"
            list2.append(print_L) 

        # M
        elif Name[i]=="M":
            print_M=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  col==0 or col==4 or ((row==col ) and row<3)   or (row+col==4 and row<3):
                        print_M[row][col]="#"
            list2.append(print_M) 

        # N    
        elif Name[i]=="N":
            print_N=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  (col==0 or col==5)or row==col:
                        print_N[row][col]="#"
            list2.append(print_N) 

        # O    
        elif Name[i]=="O":
            print_O=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  ((col==0 or col==5) and( row!=0 and row<5)) or ((row==0 or row==5) and (col>0 and col<5)):
                        print_O[row][col]="#"
            list2.append(print_O)
        #  P    
        elif Name[i]=="P":
            print_P=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==0 or ((row==0 or row==3) and col<5) or (col==5 and (row>0 and row<3)):
                        print_P[row][col]="#"
            list2.append(print_P)

        #  Q    
        elif Name[i]=="Q":
            print_Q=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col==0 or col==5) and( row!=0 and row<5)) or ((row==0 or row==5) and (col>0 and col<5)) or (row==4 and col==2) or (row==6 and col==4) :
                        print_Q[row][col]="#"
            list2.append(print_Q)

        # R     
        elif Name[i]=="R":
            print_R=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  col==0 or ((row==0 or row==3) and col<5) or (col==5 and ( 0<row<3 or row>3)) :
                        print_R[row][col]="#"
            list2.append(print_R)

        # S     
        elif Name[i]=="S":
            print_S=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  ((row==0 or row==3 or row==6) and (col>0 and col<4) ) or (col==4 and (row>3 and row<6)) or (col==0 and (row>0 and row<3)):
                        print_S[row][col]="#"
            list2.append(print_S)
        # T
              
        elif Name[i]=="T":
            print_T=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if col==2 or row==0:
                        print_T[row][col]="#"
            list2.append(print_T)
        # U     
        elif Name[i]=="U":
            print_U=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col==0 or col==4)and row!=6 ) or (row==6 and (col>0 and col<4) ):
                        print_U[row][col]="#"
            list2.append(print_U)
        # V     
        elif Name[i]=="V":
            print_V=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if ((col==0 or col==4) and row<5) or (row-col==4 and row>4) or (col==3 and row==5):
                        print_V[row][col]="#"
            list2.append(print_V)
            
        # W     
        elif Name[i]=="W":
            print_W=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  col==0 or col==4 or (row+col==6 and row>3) or ((row+col==8) and (col<5 and row<6)) :
                        print_W[row][col]="#"
            list2.append(print_W)
        # X     
        elif Name[i]=="X":
            print_X=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if row==col or row+col==5:
                        print_X[row][col]="#"
            list2.append(print_X)
        # Y     
        elif Name[i]=="Y":
            print_Y=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if (col==2 and row>2) or ((row==col or row+col==4) and row<3):
                        print_Y[row][col]="#"
            list2.append(print_Y)
        # Z     
        elif Name[i]=="Z":
            print_Z=[[" "for j in range(6)]for i in range(7)]
            for row in range(7):
                for col in range(6):
                    if  row==0  or row==5 or row+col==5:
                        print_Z[row][col]="#"
            list2.append(print_Z)

    return list2                



Name=input("Enter String: ")
list2=[]
list3=pattern_name()
print(list3)
s=time()
for i in range(7):
    for j in range(len(list3)):
        for k in range(6):
            print(list3[j][i][k],end=" ")
        print(end=" ")
    print()        
r=time()
print(r-s)    
