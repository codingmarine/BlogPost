import pyautogui as pag
import pyperclip

pyperclip.copy('코딩은 즐거워')
pag.hotkey('ctrl','v')

pag.click() #클릭
pag.rightClick() #우클릭
pag.doubleClick() #더블클릭
pag.tripleClick() #세번클릭
pag.click(clicks=10, interval=0.5) # 0.5초에 한번씩 10번클릭
pag.moveTo(800,60,duration=1) # 화면상 800,600좌표로 이동
pag.moveRel(80,60,duration=1) # 상대좌표로 80,60만큼 이동
pag.dragTo(800,60,duration=1) # 화면상 800,600좌표로 드래그
pag.dragRel(80,60,duration=1) # 상대좌표로 80,60만큼 드래그
pag.position() # 마우스의 좌표를 (x,y)튜플로 반환

# 키보드
pag.typewrite('Hello world') # 현재 커서위치에 문자열 입력
pag.typewrite('코딩은 즐거워') # 아무일도 일어나지 않음
pag.keyDown('tab') # tab키 누르기
pag.hotkey('ctrl','c') # Ctrl+C 누르기

pag.screenshot()
pag.screenshot('test.png')
pag.screenshot('test.png',region=(1200,0,1200,2400))
pag.screenshot()

pag.locateCenterOnScreen('findimg.png')