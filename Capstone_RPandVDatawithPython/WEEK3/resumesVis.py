# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:24:42 2020

@author: PC
"""

import matplotlib.pyplot as plt
labels = ['caucs','afams']
calls = [235, 157]
colors = ['lightskyblue', 'gold']
explode = (0.2, 0)
plt.pie(calls, explode=explode, labels=labels, colors=colors, 
        autopct='%1.1f%%', shadow=True, startangle=90)
#plt.legend(patches, labels, loc="best")
plt.axis('equal')
#plt.tight_layout()
plt.show()
plt.savefig('resumesVis.png')