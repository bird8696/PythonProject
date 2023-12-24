# TTS (Text To Speech) <= 글을 쓴걸 컴퓨터가 읽어줌
# STT (Speech To Text) <= 마이크 음성을 컴퓨터가 텍스트로 변환해줌

# TTS 실습
from gtts import gTTS

# playsound = 소스코드에서 바로 음성 파일 재생해줌
from playsound import playsound

file_name = "sample.mp3"

# 영어 문장
# text = "Can I help you?"
# tts_en = gTTS(text=text, lang="en")
# tts_en.save(file_name)

# playsound(file_name)

# 한글 문장
# text = "파이썬을 배우면 이런 것도 할 수 있어요"
# tts_ko = gTTS(text=text, lang="ko")
# tts_ko.save(file_name)

# playsound(file_name)

# 긴 문장 처리(파일에서 불러와서 처리하도록 설정)
# with open("sample.txt", "r", encoding="utf8") as f:
#     text = f.read()

# tts_ko = gTTS(text=text, lang="ko")
# tts_ko.save(file_name)

# playsound(file_name)
