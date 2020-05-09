## 自然語言處理(Natural Language Processing, NLP)

#### 詞庫(thesaurus)方法

- 著名的詞庫: WordNet

- 詞庫的問題

  - 字詞會因應時代改變
  
  - 人工作業成本昂貴
  
  - 無法表現字詞的細微語感差異
  
#### 計數方法
  
- 語料庫(corpus): Penn Treebank (PTB) 資料集
  
- 處理流程
  
  - 文本資料預處理
   
    - [ ] 分割字詞
     
    - [ ] 建立字詞 ID 清單(corpus)、字詞轉換字詞 ID 的字典(word_to_id)和字詞 ID 轉換字詞的字典(id_to_word)
     
  - 字詞分散式表示擷取詞意
   
    - [ ] 分布假說(distributional hypothesis): 詞意是由周圍的字詞所形成
     
    - [ ] 建立共生矩陣(co-occurence matrix)
     
  - 使用餘弦相似度(cosine similarity)表示字詞向量之間的相似度
   
  - 建立用來顯示相似詞排名的函數

- 計數方法的改進

  - 點間互資訊(Pointwise Mutual Information, PMI)
  
  - 共生矩陣(co-occurence matrix)轉換成正向點間互資訊(Positive PMI, PPMI)矩陣 [稀疏矩陣(sparse matrix)->稠密矩陣(dense matrix)]
  
  - 使用奇異值分解(Truncated SVD) 對 PPMI 矩陣進行降維(dimensionality reduction)
  
  - 以稠密向量(dense vector)顯示字詞的分散式表示
      
#### 推論方法

- Continuous Bag-Of-Words (CBOW) 模型 (簡化型 word2vec)

- skip-gram 模型

- word2vec 模型

  - 簡化型 word2vec 導入新的 Embedding 層和損失函數 Negative Sampling
