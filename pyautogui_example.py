import pyautogui as pag
import pyperclip
import time

REPORT_PATH = 'C:\\users\\admin\\desktop\월간보고서'
REPORT_PATH = 'C:\\users\장동우\\desktop\월간보고서'
print(REPORT_PATH)
pyperclip.copy(REPORT_PATH) # 경로 복사
pag.hotkey('win','e') #탐색기 ON
pag.hotkey('alt','d') #탐색기 주소창으로 포커스
pag.hotkey('ctrl','v') # 탐색기 주소창에 경로 입력
pag.keyDown('enter') #엔터 
concatenate_text = ''
for i in range(1,7): #1월부터 6월까지
    pag.hotkey('ctrl','f') # 탐색기 검색창 오픈
    pag.typewrite(str(i).zfill(2)) # 탐색기 검색창에 '00월' 입력
    pag.keyDown('enter') #검색
    pag.keyDown('tab')   
    pag.keyDown('tab')
    pag.keyDown('down')
    pag.keyDown('enter')  # 선택된 파일 열기
    time.sleep(5) #파일이 열릴때 까지 기다리기
    pag.hotkey('ctrl','a') #전체 내용 선택
    pag.hotkey('ctrl','c') # 복사
    concatenate_text += pyperclip.paste() #텍스트에 합치기
    concatenate_text += '\n' #줄구분
    pag.hotkey('alt','f4') #보고서 닫기
pyperclip.copy(concatenate_text)
