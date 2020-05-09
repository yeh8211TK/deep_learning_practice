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
   
  - 顯示相似詞的排名

- 計數方法的改進
      
