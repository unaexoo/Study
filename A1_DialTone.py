#!/usr/bin/env python
# coding: utf-8

# In[1]:


''' Part 1) 다이얼톤 파일 들어보기 '''
from IPython.display import Audio
fin = 'dialtone.wav'
fout = 'output.wav'

Audio(fin, autoplay=True)


# In[2]:


''' Part 2) 다이얼톤 파일 읽어오기 '''
from scipy.io import wavfile
import numpy

[fs, data] = wavfile.read(fin)              # fs: 샘플링 레이트, data: 샘플의 배열
n = len(data)                               #  n: 샘플의 수
t = numpy.linspace(0, (n-1)/fs, n)         #  t: 샘플링 레이트와 샘플의 수로 계산한 타임스탬프   
t1_amp = data / 32768

print(['data: ', data])
print(fs)
print(t1_amp)
print(t)


# In[3]:


''' Part 3) 시간축에서 신호의 파형을 그래프로 그려보기 '''
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

figure(figsize=(18, 6), dpi=80)

plt.stem(t, t1_amp, markerfmt=" ", use_line_collection=True)
plt.xlabel("Time (s)");
plt.ylabel("Normalized Amplitude");
plt.title("Dial Tone on Time Domain");
plt.grid('on');
plt.axis([0, (n-1)/fs, min(t1_amp), 1])


# In[4]:


''' Part 4) 푸리에 변환을 수행하고 주파수 축에서의 파형을 그래프로 그려보기 '''
f0_amp = numpy.fft.fft(t1_amp, n) / n #computes the fft
freq = numpy.linspace(0, fs, n)
P2 = f0_amp

figure(figsize=(18, 6), dpi=80)
plt.stem(freq, numpy.conj(f0_amp), 'r', markerfmt=" ", use_line_collection=True)
plt.axis([0, fs, 0, max(abs(f0_amp))])
plt.grid('on')


# In[5]:


''' Part 5) 유효 데이터에 대한 주파수 축에서의 파형을 그래프로 그려보기 '''
m = int(n/2)

P1 = P2
P1 = P1[0:m+1]
P1[1:m] = 2 * P1[1:m]
f1_amp = P1
f = numpy.linspace(0, fs/2, m+1)

print(len(f))
print(len(f1_amp))
print(f)
figure(figsize=(18, 6), dpi=80)

plt.stem(f, numpy.conj(f1_amp), 'r', markerfmt=" ", use_line_collection=True)
plt.xlabel("Frequency (Hz)");
plt.ylabel("Noised Amplitude");
plt.title("Dial Tone on Frequency Domain");
plt.axis([0, fs/2, 0, max(abs(f1_amp))])
plt.grid('on')


# In[6]:


''' Part 6) 검사 주파수 영역 설정하기 '''
LOW_FREQ  = [697, 770, 852, 941];      # 다이얼 톤을 구성하는 하한 주파수 
HIGH_FREQ = [1209, 1336, 1477];        # 다이얼 톤을 구성하는 상한 주파수
BW = 50

lb = [0];
ub = [];
for lf in LOW_FREQ:
    lb = numpy.append(lb, lf + BW/2)
    ub = numpy.append(ub, lf - BW/2)
for uf in HIGH_FREQ:
    lb = numpy.append(lb, uf + BW/2)
    ub = numpy.append(ub, uf - BW/2)
ub = numpy.append(ub, fs/2)
print(lb)
print(ub)


# In[7]:


''' Part 7) 노이즈 제거 후 파형 출력하기 '''
f2_amp = f1_amp
for i in range(0, len(lb)):
    idx = (f >= lb[i]) & (f < ub[i])
    f2_amp[idx] = 0
    
figure(figsize=(18, 6), dpi=80)
plt.stem(f, numpy.conj(f2_amp), 'g', markerfmt=" ", use_line_collection=True)
plt.xlabel("Frequency (Hz)");
plt.ylabel("Denoised Amplitude");
plt.title("Noise-Removed Dial Tone on Frequency Domain");
plt.grid('on');
plt.grid('minor');
plt.axis([0, fs/2, 0, max(abs(f2_amp))])


# In[8]:


''' Part 8) 푸리에 역변환 수행 후 파형 출력하기 '''
t2_amp = numpy.fft.irfft(f2_amp * n, n);

figure(figsize=(18, 6), dpi=80)
plt.plot(t, numpy.conj(t2_amp));
plt.xlabel("Time (s)");
plt.ylabel("Normalized Amplitude");
plt.title("Pass-Filtered Dial Tone on Time Domain");
plt.grid('on');
plt.grid('minor');
plt.axis([0, (n-1)/fs, min(t2_amp), max(t2_amp)])


# In[9]:


''' Part 9) 노이즈가 제거된 다이얼톤 파일 들어보기 '''
denoised_data = t2_amp
scaled = numpy.int16(denoised_data/numpy.max(numpy.conj(denoised_data)) * 32768)

wavfile.write(fout, fs, scaled)
Audio(fout, autoplay=True)


# In[ ]:





# In[ ]:




