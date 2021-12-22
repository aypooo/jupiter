#!/usr/bin/env python
# coding: utf-8

# <Step1.탐색> : 데이터의 기초 정보 살펴보기

# [Chipotle 데이터셋의 기본 정보]

# In[1]:


#pandas 모듈 임포트
import pandas as pd
#read_csv() 함수로 데이터를 Dataframe 형태로 불러옵니다.
#pd.read_csv("파일경로를 포함한 파일명",sep="구분자")
#raw data를 상대 경로로 불러오기
file_path = '../data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep="\t")

print(chipo.shape)


# In[2]:


#데이터 프레임의 행과 열의 정보 출력
print(chipo.shape)
print("---------------------------------")
print(chipo.info())


# In[3]:


#chipo 라는 Dataframe에서 순서대로 10개의 row데이터를 보여줍니다.
#head() 함수에 인수를 생략하면 기본5개의 데이터를 보여줌
chipo.head(10)
print("---------------------------------")
chipo.tail(10)


# In[4]:


print(chipo.columns)


# In[5]:


#columns() 함수로 컬럼의 정보를 보여줌
print(chipo.columns)
print("---------------------------------")
print(chipo.index)


# [Chipotle 데이터셋의 수치적 특징 파악]
# quantity 와 itme_price의 요약 통계
# describe() 함수로 요약 통계량 출력하기

# In[6]:


# order_id는 숫자의 의미를 가지지 않기 때문에 str으로 변환합니다.
chipo['order_id'] = chipo['order_id'].astype(str)
#chipo dataframe에서 수치형 피처들의 요약 통계량을 확인합니다. 
chipo.describe()
#unipue 함수로 범주형 피쳐의 개수 출력하기


# In[7]:


#unipue 함수로 범주형 피쳐의 개수 출력하기
#order_id의 개수를 출력
len(chipo['order_id'].unique())


# In[8]:


#item_name의 개수를 출력
len(chipo['item_name'].unique())


# In[9]:


#가장 많이 주문한 item :top 10을 출력합니다. 
item_count = chipo['item_name'].value_counts()[:10]
for idx, (val, cnt) in enumerate(item_count.iteritems(), 1):
    print("Top", idx,":", val, cnt)


# In[10]:


order_count = chipo.groupby('item_name')['order_id'].count()
order_count[:10]


# [item당 주문 개수와 총량 구하기]

# In[12]:


#item당 주문 개수를 출력합니다.
#groupby()함수는 데이터 프레임에서 특정 피처를 기준으로 그룹을 생성하여 이를 통해 그룹별 연산 적용
order_count = chipo.groupby('item_name')['order_id'].count()
order_count [:10]


# In[13]:


#item당 주문 총량을 출력합니다.
item_quantity= chipo.groupby('item_name')['quantity'].sum()
item_quantity[:10]#상위 10개의 item당 주문 총량을 출력합니다.


# In[50]:


#get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

#아이템별 주문의 총량을 막대 그래프로 시각화
item_name_list = item_quantity.index.tolist()

#numpy.arrange(시작, 끝, 간격)로 배열 생성
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()
#bar()는 막대 그래프를 출력해주는 함수
plt.bar(x_pos,order_cnt,align='center')
plt.ylabel('ordered_item_count')
plt.title('Distribution of all orderd item')

plt.show()

plt.scatter(x_pos,order_cnt,alpha=0.5, label='ordered_item_count')
plt.ylabel('ordered_item_count')
plt.legend(loc = 'upper left')
plt.title('Distribution of all orderd item')

plt.show()


# In[39]:


chipo['item_name'].value_counts()[:10]


# In[41]:


type(chipo['item_name'].value_counts()[:10])


# In[42]:


chipo['item_name'].unique()[:10]


# In[43]:


type(chipo['item_name'].unique().tolist())


# In[45]:


chipo['item_name'].unique().tolist()


# In[ ]:





# In[ ]:




