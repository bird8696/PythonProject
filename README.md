# PythonProject: 파이썬을 이용한 음성 인식

## 소개

이 프로젝트는 파이썬을 활용하여 음성 인식 기능을 구현하는 것을 목표로 합니다. 특히, 텍스트를 음성으로 변환하는 TTS(Text-to-Speech)와 음성을 텍스트로 변환하는 STT(Speech-to-Text) 기능의 학습 및 테스트를 진행합니다.

## 기능

- **TTS (Text-to-Speech)**: 입력된 텍스트를 자유롭게 변환한 음성으로 제공
- **STT (Speech-to-Text)**: 입력된 음성을 텍스트로 변환

## 설치 방법

1. 리포지트를 클론합니다:
   ```bash
   git clone https://github.com/bird8696/PythonProject.git
   ```

2. 프로젝트 디렉토리로 이동합니다:
   ```bash
   cd PythonProject
   ```

3. 가상 환경을 생성하고 활성화합니다:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Linux/Mac
   myenv\Scripts\activate  # Windows
   ```

4. 필수한 패키지를 설치합니다:
   ```bash
   pip install -r requirements.txt
   ```

## 사용 방법

### **TTS 기능 테스트**

`sample.txt` 파일에 변환할 텍스트를 입력한 후, 다음 명령을 실행하여 `sample.mp3` 파일으로 저장되는 음성을 확인합니다:

```bash
python tts.py
```

### **STT 기능 테스트**

`sample.mp3` 파일을 준비한 후, 다음 명령을 실행하여 음성이 텍스트로 변환되는지 확인합니다:

```bash
python stt.py
```

## 파일 설명

- `tts.py`: 텍스트를 음성으로 변환하는 스크립트
- `stt.py`: 음성을 텍스트로 변환하는 스크립트
- `sample.txt`: TTS 기능 테스트를 위한 입력 텍스트 파일
- `sample.mp3`: STT 기능 테스트를 위한 입력 음성 파일

## 기업 방법

1. 이슈를 등록하여 버그를 보고하거나 새로운 기능을 제안합니다.
2. 포트보드를 포클해서 변경 사항을 적용한 후, 푸들 리케스트를 생성합니다.

## 라이센스

이 프로젝트는 MIT 라이센스를 보입니다. 자세한 내용은 `LICENSE` 파일을 참고하세요.

