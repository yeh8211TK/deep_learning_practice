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
  
- 計數方法的問題

  - 在處理大型語料庫時，執行 SVD 需要耗費大量的運算資源和時間
      
#### 推論方法

- 以分布假說為基礎，對目標字詞進行推測並獲得字詞的分散式表示

- 類神經網路對字詞的處理方式: **字詞 -> 字詞 ID -> one-hot encoding**

- 簡化型 word2vec 包含 CBOW 模型與 skip-gram 模型

  - continuous bag-of-words (CBOW) 模型: 從周圍的字詞推測中間字詞的類神經網路
  
  - skip-gram 模型: 從中間的字詞推測周圍字詞的類神經網路
  
  - CBOW 模型與 skip-gram 模型的比較
  
    - 從機率觀點描述 CBOW 模型與 skip-gram 模型 (window size = 1)
    
      - [ ] CBOW 模型: <img src="https://render.githubusercontent.com/render/math?math=P(\omega_{t}|\omega_{t-1}, \omega_{t %2B 1})">

      - [ ] skip-gram 模型: <img src="https://render.githubusercontent.com/render/math?math=P(\omega_{t-1}, \omega_{t %2B 1}|\omega_{t})">
  
    - 以字詞分散式表示而言，skip-gram 模型通常可獲得良好的結果
    
    - 以學習速度而言，CBOW 模型比 skip-gram 模型快

- CBOW 模型

  - **輸入層(one-hot encoding 的 N 個上下文字詞) -> MatMul 層 -> 中間層(通過 MatMul 層的 N 個輸出計算平均值) -> MatMul 層 -> Softmax with loss 層 -> 輸出**

  - 權重與分散式表示
  
    - 最普遍的情況為使用輸入端的權重(<img src="https://render.githubusercontent.com/render/math?math=W_{in}">)當作字詞的分散式表示
  
- word2vec 模型

  - CBOW 模型的運算瓶頸與解決方式
  
    - 輸入層的 one-hot 編碼與計算權重矩陣(<img src="https://render.githubusercontent.com/render/math?math=W_{in}">)的乘積以及中間層與權重矩陣(<img src="https://render.githubusercontent.com/render/math?math=W_{out}">)的乘積
    
      - [ ] 解決方式: 導入 Embedding 層
    
    - Softmax 層的運算
    
      - [ ] 解決方式: 使用 Negative Sampling 的技術
  
  - word2vec 模型的結構
  
    - **輸入層(one-hot encoding 的 N 個上下文字詞) -> Embedding 層 -> 中間層(通過 Embedding 層的 N 個輸出計算平均值) -> Embedding Dot 層 -> Sigmoid with loss 層 -> 輸出**
    
  - Embedding 層
  
    - 對權重矩陣(<img src="https://render.githubusercontent.com/render/math?math=W_{in}">)取出特定列向量，得到詞嵌入(word embedding)(分散式表示)
  
  - Embedding Dot 層
  
    - 對權重矩陣(<img src="https://render.githubusercontent.com/render/math?math=W_{out}">)取出特定字詞的行向量，再與中間層的神經元作內積
  
  - Sigmoid with loss 層
  
    - 將多值分類的問題(根據上下文推測中間的字詞)轉換成二值分類的問題(根據上下文推測中間的字詞是不是某個字詞)
    
    - 負值取樣(Negative Sampling)方法
    
      - 概念: 用 "部分" 資料取代 "全部" 資料的處理
    
      - 作法: 在計算以正例(正確答案)為目標字詞的損失時，同時取樣幾個負例(錯誤答案)計算損失，並將所有資料(正例與取樣的負例)的損失相加作為最終的損失
  
      - Negative Sampling 的取樣方式
      
        - [ ] 根據語料庫中字詞出現的次數計算機率分布，之後再按照機率分布執行負例取樣
        
        - [ ] 字詞的機率須加上一個指數(Ex: 0.75)做轉換，目的是提高低機率字詞出現的機率
      
- word2vec 的應用
  
  - word2vec 是遷移學習(transfer learning)的重要關鍵，字詞分散式表示可以運用在各式各樣的自然語言處理上
    
    - 遷移學習(transfer learning): 將某個領域的知識套用在其他領域
      
  - 解決自然語言任務時，通常先利用大型語料庫(wikipedia、google news...)進行學習，再使用已學習完畢的分散式表示處理各項任務
    
  - 字詞分散式表示的優點是可以把字詞轉換成固定長度的向量，這樣該向量就可套入一般的機械學習系統
    
    - 字詞分散式表示的系統處理流程: **自然語言 -> 詞向量(word2vec) -> 機械學習系統(類神經網路、SVM...) -> 答案**
      
    - 字詞分散式表示與機械學習系統分別使用不同資料(大型通用語料庫、目前面對的問題所收集的資料)進行個別學習; 若所面對的問題有大量的學習資料，可以從零開始進行字詞分散式表示與機械學習系統的學習
      
  - 範例: 電子郵件自動分類系統
    
    - 情感分析處理流程: 電子郵件 -> 人工加入情感的等級標籤 -> 利用學習完畢的 word2vec 詞向量化電子郵件 -> 執行情感分析的分類系統(類神經網路、SVM...) -> 答案
      
- 詞向量的評估方法

  - 擁有精確度良好的系統(應用程式)是由多個已最佳化超參數的系統所組成 (例: 建立字詞分散示表示的系統 + 針對特定問題進行分類的系統)
  
  - 一般字詞的分散式表示和實際的應用系統會分開評估，字詞的評估指標: **相似性**、**類推問題**
  
    - 字詞的相似性評估: 人工對字詞之間的相似性評分，再與 word2vec 的餘弦相似度進行比較
    
    - 類推問題評估: 使用準確率檢測字詞的分散式表示
    
      - [ ] 精確度會隨著模型而異
      
      - [ ] 語料庫越大，結果越好
      
      - [ ] 詞向量的維度必須適中 (越大則精確度越差)
      
  - 在類推問題的評估中獲得好的結果，目標應用程式無法保證良好(需考量應用程式種類、語料庫內容等因素)
  
#### 計數方法與推論方法的比較

  - 學習的手法
  
    - 計數方法: 從整個語料庫的統計資料中，利用一次學習獲得字詞的分散式表示

    - 推論方法: 反覆檢視語料庫的一部份並學習(小批次學習)
    
  - 新字詞的更新
  
    - 計數方法: 從零開始計算，重新建立共生矩陣，運算 SVD 等一連串步驟

    - 推論方法: 利用學習過的權重當作預設值重新學習參數，可有效率地更新字詞的分散式表示
    
  - 字詞分散式表示的精確度
  
    - 計數方法: 把字詞的相似性進行編碼

    - 推論方法: 除了字詞相似性，也能掌握複雜字詞之間的類型 (特別是 word2vec 中的 skip-gram 模型)
    
    - 關於字詞相似性的定量評估: 字詞相似性與超參數有密切關係，因此計數方法與推論方法沒有明確的優劣之分

  - 計數方法與推論方法的關聯性
  
    - 使用 skip-gram 與 negative sampling 的模型，相當於將整個語料庫的共生矩陣進行特殊的矩陣分解
    
  - 計數方法與推論方法的結合: GloVe 方法
  
    - 概念: 將整個語料庫的統計資料放入損失函數中，進行小批次學習  

#### 語言模型

- CBOW 模型近似語言模型

- 語言模型的評估: 困惑度(perplexity)

- RNN 處理語言模型(RNN Language Model, RNNLM)

- LSTM 處理語言模型(LSTM Language Model, LSTMLM)

- LSTMLM 的改良

  - 多層化 LSTM
  
  - 以 Dropout 抑制 overfitting
  
  - 共享權重(weight tying)
  
- LSTMLM 生成文章

#### seq2seq

- Encoder & Decoder

- seq2seq 的改良方法

  - 輸入資料反轉(Reverse)
  
  - Peeky Decoder
  
- seq2seq 的應用

  - 聊天機器人
  
  - 演算法學習
  
  - 圖像描述(image captioning)

#### Attention

- seq2seq 的問題

  - 無論多長的文章，Encoder 會將之轉為固定的向量傳給 Decoder

- 執行 seq2seq 的改良

  - 改良 Encoder
    
    - 取出 Encoder 中所有時刻的隱藏狀態 hs，可獲得與輸入內容長度成正比的資料編碼
  
  - 改良 Decoder: 建立 Attention 層
  
    - Attention 層由 Attention Weight 層和 Weight Sum 層所構成
    
    - Attention Weight 層的目的是計算能夠代表各個字詞重要程度的權重 a
    
      - [ ] 計算 hs 與 h (hs 的最後一列，用來連接 Encoder 與 Decoder)的內積(目的在計算各個詞向量的相似度)，再使用 softmax 函數進行正規化得到 a
  
    - Weight Sum 層
    
      - [ ] 利用代表各字詞向量的 hs 與代表各個字詞重要程度的權重 a，計算出加權總合，得到上下文向量 c
      
      - [ ] 上下文向量 c 包含了轉換當前時刻的必要資料 (從 hs 選出各個時刻的字詞向量與 Decoder 的輸入字詞有著對應關係)
      
- Encoder 的雙向 RNN 結構

- 隱藏狀態 h 對 Deconder Attention 層的多層連接

- 深層化 seq2seq 與跳躍連接(skip connection)

- Attention 的應用

  - 神經機器翻譯(Neural Machine Translation)

    - Google Neural Machine Translation (GNMT)

  - Transformer
  
    - Self-Attention: 以 Attention 取代 RNN/LSTM 層

  - Neural Turing Machine (NTM)
  
    - NTM 的改良: Differentiable Neural Computer (DNC)

