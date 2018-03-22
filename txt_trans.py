import numpy as np
import bd2WGS
with open('test.txt', 'r') as f:
    i = 0
    #f.readline();
    for wholeline in f.readlines():
        i+=1
        if i>1:
            splitedline = wholeline.split(',')
        # print(splitedline[0], splitedline[1], splitedline[2], splitedline[3], splitedline[4])
            if len(splitedline) == 5:
                lng = splitedline[2]
                lat = splitedline[1]
                # if float(lng)>114 and float(lng)<115 and float(lat)<31 and float(lat)>30:
                #     # print('第',i,'行ok')
                #     continue
                # else:

                #     print('i:',i,'  lng:',lng,'  lat:',lat)

                transeddata = bd2WGS.gcj02_to_wgs84(float(lng), float(lat))
                with open('test转换后.txt', 'a') as f2:
                    f2.write(str(transeddata[0]) + ',' + str(transeddata[1]) + '\n')
            else:
                print('i:',i,'  wholeline:',wholeline)

        else:
            continue



