def list_of_tuples(filename):
        line3 = []
        with open (filename) as file:
             for line in file :
               line = line.strip('\n')
               line1 = line.replace(' ','').replace('!',':').replace('\t',':')
               if line1:
                    #print('1：' + line1)
                    line2 = line1.split(':')
                    #print('2：' + line2)
                    line2 = tuple(map(int, line2))
                    if int(line2[0]) < int(line2[1]) and int(line2[1]) < int(line2[2]):
                         #print(line2)
                         line3.append(line2)
        print(line3)
        return line3