import math

# Cilindra radius
Rc = 12.5
Hc = 40
# Frezes radius
Rd = 2.5
#Sagataves augstums un radius
Hs = 67
Rs = 25

Astep = 0.5
Zstep = math.radians(0.1)

Tf = 0
Fpt = 0.05
Nt = 2

Cconvert = 500/360


def main():
    # Specify the name of the output file
    output_file = 'PiemineklisGcode.min'
    # Open the file in write mode ('w')
    with open(output_file, 'w') as file:
        # Write content to the file
        setup = ['T121212\n', 'G50S3500\n', 'G96S200M3\n', '\n']
        end = ['\n', 'G1 X30 Z-32\n', 'G0 35X Z10\n', 'G96S0M3\n', 'M30\n']

        def G101(x, z, c):
            file.write('G101 X' + str(round(x, 3)) + ' Z' +  str(round(z, 3)) + ' C' + str(round(math.degrees(c), 3)) +'\n')

        def G1(x, z):
            file.write('G1 X' + str(round(x, 3)) + ' Z' +  str(round(z, 3)) +'\n')

        def G0(x, z):
            file.write('G0 X' + str(round(x, 3)) + ' Z' +  str(round(z, 3)) +'\n')
        
        def C(c):
            file.write('C' + str(round(math.degrees(c), 3)) + '\n')
        
        def F(f):
            file.write('F' + str(round(f, 3)) + '\n')

        def CW():
            file.write('M15\n')

        def CCW():
            file.write('M16\n')

        def Line(a, b):
            k1 = a
            

        def CylTop():
            for z in range(int(Rc/Zstep)+1):
                beta = math.asin((Rc - z*Zstep)/Rc)
                Rloc = Rc*math.sin(beta)
                for a in range(int(2*(math.radians(90)-math.atan(Rloc/(Hc/2))))+1):
                    k1 = (Rc**2)*(math.cos(a*Astep))**2
                    k2 = (1-(math.cos(a*Astep))**2)

                    Diskr = 4*(Rc**2)*(k2**2) + 4*k1*k2

                    Dr = (-2*Rc*k2 + math.sqrt(Diskr))/(2*k2 + 0.0001)

                    G101(Dr, z*Zstep, a*Astep)
                #file.write('G101 X' + str(round(Dr, 3)) + ' Z' +  str(round(z*Zstep, 3)) + 'C' + str(round(a*Astep, 3)) +'\n')
                #file.write('C' + str(round(a*Astep, 3)) +'\n')
            #file.write('G1 X80 Z' +  str(round(z*Zstep, 3)) +'\n')
            #file.write('C' + str(round(a*Astep, 3)) +'\n')

        #file.writelines(setup)

        #file.writelines(end)

if __name__ == '__main__':
    main()