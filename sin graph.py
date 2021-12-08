# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 14:41:27 2021

@author: user
"""

import numpy as np    # 수치계산용 라이브러리 Numpy  
import matplotlib.pyplot as plt   # 그래프용 라이브러리
#
# A*sin(2*pi*f*t)의 정현파를 만들어 보자
#                         pi 는 np.pi로 가져온다.
n=2                     # 만들고자 하는 ramp신호의 길이 설정  3초
a=1                     # amplitude = 1
f=2                     # frequency = 2
fs=100.0                # 표본화율 100Hz로 설정
ts=1.0/fs               # sampling interval
t=np.arange(0.0, n, ts) # 시간축 범위 생성  0초 부터 n초까지 1초 간격
y=a*np.sin(2*np.pi*f*t)      # Sin wave
plt.plot(t,y,'-')  # matplotlib의 plot 함수 호출 그래프 그림
plt.show()   # 그려진 그래프를 보이게 함   


# 함수 이용

def draw_sin(n,a,f,fs):
    ts=1.0/fs               # sampling interval
    t=np.arange(0.0, n, ts) # 시간축 범위 생성  0초 부터 n초까지 1초 간격
    y=a*np.sin(2*np.pi*f*t)      # Sin wave
    plt.plot(t,y,'-')  # matplotlib의 plot 함수 호출 그래프 그림
    plt.title('Sine graph')
    plt.xlabel('Time (sec)')
    plt.ylabel('Amplitude')
    plt.show()   # 그려진 그래프를 보이게 함  

draw_sin(2,1,2,100)