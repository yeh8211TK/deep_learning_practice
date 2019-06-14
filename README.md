本地作為學習深度學習的歷程記錄。

This repository is a place for my deep learning practices.

建置中...

Under construction...

[註] 在 Github 順利查看 .ipynb 檔的方式: 在 https://nbviewer.jupyter.org/ 輸入檔案網址

## 目錄
### Part 1 基礎篇(一): Artificial Neural Network
- 感知器與類神經網路 (感知器、活化函數、神經網路的推論、參數最佳化、神經網路的學習) 

  -- [deep_learning_neural_network.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_neural_network.ipynb)

  -- 四種最佳化方法(SGD、Momentum、AdaGrad、Adam)的動畫顯示: ani.mp4

- 類神經網路的誤差反向傳播法 (計算圖、加法層、乘法層、ReLU 層、Sigmoid 層、Affine 層、Softmax-with-loss 層、神經網路的學習)

  -- [deep_learning_backward_propagation.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_backward_propagation.ipynb)

- 類神經網路學習的技術

  -- [deep_learning_techniques.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_techniques.ipynb)

- 捲積神經網路 (convolutional neural network, CNN)

  -- [deep_learning_CNN.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_CNN.ipynb)
  
- 深度學習應用整理
     
  -- [deep_learning_applications.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_applications.ipynb)

### Part 2 基礎篇(二): 深度學習框架 Keras 和 TensorFlow
- 使用 Keras 執行 MLP、CNN 影像辨識

  -- [deep_learning_keras.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_keras.ipynb)

- TensorFlow 的執行模式與類神經網路的張量運算

  -- [deep_learning_tensorflow_1.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_tensorflow_1.ipynb)

- 使用 Tensorflow 執行 MLP、CNN 影像辨識

  -- [deep_learning_tensorflow_2.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_tensorflow_2.ipynb)
  
- CPU 與 GPU 執行 TensorFlow 的效率測試

  -- [deep_learning_GPU.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_GPU.ipynb)

### Part 3 基礎篇(三): 時間序列資料處理
- 遞歸神經網路(RNN、Time RNN)、長短期記憶(LSTM、Time LSTM) 模型、GRU (Gated Recurrent Units) 模型

  -- [deep_learning_RNN&LSTM.ipynb] (To be continued...)

- 自然語言處理(natural language processing, NLP)-1

  -- 傳統方法: 詞庫手法、計數手法; 類神經網路方法: 推論手法(word2vec、CBOW 模型) (To do list)

- 自然語言處理(natural language processing, NLP)-2

  -- RNNLM、LSTMLM、seq2seq、Attention mechanism (To do list)

### Part 4 基礎篇(四): 深度學習框架處理時間序列的問題
- 使用 Keras 執行 RNN、LSTM

  -- [deep_learning_Keras_RNN.ipynb] (To do list)

  -- [deep_learning_Keras_LSTM.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_Keras_LSTM.ipynb)

- 使用 Tensorflow 執行 RNN、LSTM (To do list)

### Part 5 應用篇: Autoencoder
- Autoencoder 應用 (1): 使用 Keras 與 Denoising Autoencoder (DAE) 模型對影像資料降噪(Denoise)

  -- [deep_learning_denoising_AE.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/deep_learning_denoising_AE.ipynb)

- Autoencoder 應用 (2): 工業數據的異常偵測(Anomaly Detection)

  -- [Autoencoder_for_extreme_rare-event_classification.ipynb](https://nbviewer.jupyter.org/github/yeh8211TK/deep_learning_practice/blob/master/Autoencoder_for_extreme_rare-event_classification.ipynb)

- Autoencoder 應用 (3): LSTM Autoencoder 處理時間序列資料

  -- [LSTM_Autoencoder.ipynb](To do list)

### 參考書目
- <Deep Learning：用 Python 進行深度學習的基礎理論實作> (2017)
- <Deep Learning 2: 用 Python 進行自然語言處理的基礎理論實作> (2019)
- <TensorFlow + Keras 深度學習人工智慧實務應用> (2017)
