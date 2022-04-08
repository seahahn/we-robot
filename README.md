# ❇️ We-Robot

## 1️⃣ 작품 소개

GPT2의 한국어 버전으로 제작된 KoGPT2 모델 기반 챗봇과 실시간 대화가 가능한 웹 서비스

<br/>

## 2️⃣ 제작 기간 & 참여 인원
- 2022.01.11 - 2022.01.12
- 개인 프로젝트

<br/>

## 3️⃣ 사용 기술

| 분류 | 기술 목록 |
| --- | --- |
| Frontend | HTML/CSS/JS, socket.io.js 4.0.1 |
| Backend | Flask 2.0.2, Flask-SocketIO 5.1.1, Python 3.8.10 |
| Data Science | PyTorch 1.10.1 |

<br/>

## 4️⃣ 프로젝트 목적
- '인공지능과 사람처럼 소통하기' 라는 화두에서 출발
- 이에 해당되는 것으로 **챗봇(Chatbot)** 을 떠올렸고, 이를 구현해보고자 함
- 또한 학습시킨 챗봇 모델을 웹사이트에 어떤 방식으로 배포할 수 있는지도 알아보고자 함

<br/>

## 5️⃣ 모델 및 데이터셋 선정 과정
### 1. 모델 선택
- 사용자와 챗봇의 1:1 대화이므로, 사용자의 말에 맞춰 챗봇이 응답해야 하는 구조 -> 텍스트 생성 모델이 필요
- 텍스트 생성 모델로서 GPT3가 가장 뛰어나다고 하지만, 언어 및 사용 상의 한계로 인해 제외
- 대안으로 SKT에서 제작한 **KoGPT2** 모델을 선택
### 2. 데이터셋 선정
- 단순한 문장의 나열이 아닌 대화 데이터셋이 필요
- 대화문이 담긴 데이터셋(하단 출처)을 찾은 후, 이들을 _같은 형식_ 으로 통일시켜 하나로 통합함
  - Chatbot_data의 Q, A, label(Q, A - 대화문 쌍 / label - 감정 분류(0 : 중립 / 1 : 부정 / 2 : 긍정)) 형식

<br/>

## 6️⃣ 한계점 및 추후 개선 방안
### 1. 데이터셋의 전처리 부족
 - 여러 개의 데이터셋을 하나로 합치는 과정에서 형식은 맞췄으나, 대화의 어투까지 통일시키지는 못하였음
### 2. 모델 이해 부족
 - 챗봇 모델 학습 및 웹 서비스 적용까지 진행하였으나, 모델 자체에 대한 이해가 부족(토크나이저 및 모델 내부 요소 등)
### 3. 맥락 없는 대화 내용
 - 개별 문장에 대해서는 얼추 그럴듯한 답을 하지만, 대화의 맥락까지 내포하지는 못하고 어투도 변덕스러움
 - 학습 데이터셋의 추가적인 전처리를 통해 어투를 통일하면 어투의 변덕은 해소 가능할 것으로 예상
 - 대화 맥락의 경우 모델 이해 및 추가 자료를 통한 구현 방법 학습이 필요

<br/>

## 7️⃣ 프로젝트 시연 영상 (클릭 시 이동)
[![Project Not2Late2Know Presentation](https://user-images.githubusercontent.com/73585246/162379880-951de908-9e3b-4db9-9abe-f1b7259556fc.png)](https://youtu.be/6PP1fJyWq3U)

---

- 모델 출처 : [KoGPT2](https://github.com/SKT-AI/KoGPT2)

- 참고한 소스코드 출처 : [haven-jeon/KoGPT2-chatbot](https://github.com/haven-jeon/KoGPT2-chatbot)

- 사용한 데이터셋 목록 및 출처 :
  - [Chatbot_data](https://github.com/songys/Chatbot_data)
  - [트위터에서 수집 및 정제한 대화 시나리오 - AI Hub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-008)
  - [한국어 감정 정보가 포함된 연속적 대화 데이터셋 - AI Hub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-010)
  - [한국어 대화 데이터셋 - AI Hub](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-011)
