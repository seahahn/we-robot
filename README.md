# ❇️ We-Robot

## 1️⃣ Project Introduction

A web service featuring a chatbot based on the KoGPT2 model, the Korean version of GPT-2, capable of real-time conversations.

<br/>

## 2️⃣ Project Duration & Team

- 11 Jan 2022 - 12 Jan 2022
- Individual project

<br/>

## 3️⃣ Technologies Used

| Category     | Technology Stack                                 |
| ------------ | ------------------------------------------------ |
| Frontend     | HTML/CSS/JS, socket.io.js 4.0.1                  |
| Backend      | Flask 2.0.2, Flask-SocketIO 5.1.1, Python 3.8.10 |
| Data Science | PyTorch 1.10.1                                   |

<br/>

## 4️⃣ Project Objectives

- Initiated from the theme of 'Communicating like AI and Humans.'
- Conceived a **Chatbot** in line with this theme and aimed to implement it.
- Also explored how to deploy the trained chatbot model on a website.

<br/>

## 5️⃣ Model and Dataset Selection Process

### 1. Model Selection

- Considering the 1:1 conversation structure between the user and the chatbot, requiring the chatbot to respond to the user's statements.
- GPT-3 is considered excellent as a text generation model, but due to language and usage limitations, it was excluded.
- As an alternative, chose the **KoGPT2** model developed by SKT.

### 2. Dataset Selection

- Needed a dataset containing dialogues rather than a simple list of sentences.
- Found datasets with dialogues (sources listed below) and unified them into one by standardizing them in the _same format_.
  - The format: Chatbot_data Q, A, label (Q, A - dialogue pairs / label - emotion classification (0: Neutral / 1: Negative / 2: Positive))

<br/>

## 6️⃣ Limitations and Future Improvements

### 1. Insufficient Dataset Preprocessing

- During the process of merging multiple datasets, the format was standardized, but the conversational tone was not completely unified.

### 2. Limited Understanding of the Model

- Although the chatbot model was trained and applied to the web service, there is a lack of understanding of the model itself (tokenizer and internal elements of the model, etc.).

### 3. Context-Less Conversations

- While providing reasonably plausible responses for individual sentences, the chatbot lacks the incorporation of the context of the conversation and exhibits erratic tones.
- It is anticipated that standardizing tones can be achieved through additional preprocessing of the training dataset.
- For the context of the conversation, learning implementation methods through model understanding and additional resources is necessary

<br/>

## 7️⃣ Project Demonstration Video (Click to view)

[![Project We-Robot Presentation](https://user-images.githubusercontent.com/73585246/162379880-951de908-9e3b-4db9-9abe-f1b7259556fc.png)](https://youtu.be/6PP1fJyWq3U)

---

- Model Source: [KoGPT2](https://github.com/SKT-AI/KoGPT2)

- Source code reference: [haven-jeon/KoGPT2-chatbot](https://github.com/haven-jeon/KoGPT2-chatbot)

- List of datasets used and sources:
  - [Chatbot_data](https://github.com/songys/Chatbot_data)
  - [Continuous dialogue dataset collected and refined from Twitter - AI Hub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-008)
  - [Korean emotional information included continuous dialogue dataset - AI Hub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-010)
  - [Korean dialogue dataset - AI Hub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-011)
