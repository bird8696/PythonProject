import speech_recognition as sr

# 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print("듣고 있습니다.")
    audio = r.listen(source)  # 마이크로부터 음성 듣기

# 파일로부터 음성 불러오기(wav, aiff/aiff-c, flac 가능, mp3는 불가)
# r = sr.Recognizer()
# with sr.AudioFile('sample.wav') as source:
#     audio = r.listen(source)

# 오류 방지용 예외 처리
try:
    # 구글 API로 인식 (하루 50회 제한)

    # 영어 문장
    # text = r.recognize_google(audio, language="en-US")
    # print(text)

    # 한글 문장
    text = r.recognize_google(audio, language="ko")
    print(text)

except sr.UnknownValueError:
    print("인식 실패")  # 음성 인식을 실패했을 경우
except sr.RequestError as e:
    print("요청 실패 : {0}".format(e))  # API Key 오류, 네트워크 단절 등
