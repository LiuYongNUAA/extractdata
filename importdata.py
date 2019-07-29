# -*- encoding:utf-8 -*-

import numpy as np
import pandas as pd
from tkinter import filedialog

import re


def transfer(loadpath):
    table1, table2, table3, table4, table5 = [], [], [], [], []

    counter = 0

    pattern = re.compile(r'([a-zA-z:]+)|([-]+)')
    with open(loadpath, 'rb') as f:
        while True:
            lines = f.readline()
            if not lines:
                break
            try:
                line = lines.decode().strip()
                if line:
                    if not re.match(pattern, line):
                        numberlist = re.split(r'\s+', line)
                        for i in range(len(numberlist)):
                            numberlist[i] = float(numberlist[i])
                        if numberlist[0] == 0:
                            counter += 1
                        if counter == 1:
                            table1.append((numberlist))
                        if counter == 2:
                            table2.append(numberlist)
                        if counter == 3:
                            table3.append(numberlist)
                        if counter == 4:
                            table4.append(numberlist)
                        if counter == 5:
                            table5.append(numberlist)
            except UnicodeDecodeError:
                pass

    table1 = pd.DataFrame(np.array(table1), columns=['Time', 'X', 'Y', 'Height', 'Zp', 'Gr dist'])
    table2 = pd.DataFrame(np.array(table2), columns=['Time', 'Mach', 'VCas', 'VZP', 'AeroGrand', ' PithAtitude'])
    table3 = pd.DataFrame(np.array(table3), columns=['Time', 'BankAngle', 'Heading ', 'Weight', 'Lift', 'Drag'])
    table4 = pd.DataFrame(np.array(table4), columns=['Time', ' TOTThrust ', 'Alpha', 'VWind', 'WindDir'])
    table5 = pd.DataFrame(np.array(table1), columns=['Time', 'SegCounter', 'PortionCounter', 'Temp', 'TurnRadius',
                                                     'SGN'])

    x = np.array(table1['X'].values)
    y = np.array(table1['Y'].values)
    bankangle = np.array(table3['BankAngle'].values)
    output = np.column_stack((x, y, bankangle))

    savepath = filedialog.asksaveasfilename(title='选择输出路径', defaultextension='.txt')

    with open(savepath, 'w') as f:
        for data in output:
            f.write('%.2f\t%.2f\t%.2f\r\n' % (data[0], data[1], data[2]))




