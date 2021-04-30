from konlpy.tag import Okt

okt = Okt()

text_1 = "ㅋㅋㅋ너뭐라는거얔ㅋㅋㅋ샤릉해"

# 오타를 잘 고쳐준다.(정규화), 정규화를 하면 단어의 개수를 줄일 수 있다.
print(okt.normalize(text_1))

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.plot(np.arange(10), np.arange(10)*2, marker='o', markersize=5)
plt.plot(np.arange(10), np.arange(10)*2 - 10, marker='v', markersize=10)
plt.plot(np.arange(10), np.arange(10)*2 - 20, marker='+', markersize=15)
plt.plot(np.arange(10), np.arange(10)*2 - 30, marker='*', markersize=20)