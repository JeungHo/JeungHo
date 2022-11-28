from tkinter import Tk  # GUI로 파일 선택하기 위한 모듈
from tkinter.filedialog import askopenfilename  # 파일선택창

import win32com.client as win32  # 한/글 열기 위한 모듈

def hwp_init(filename):  # 한/글 여는 코드가 길어서 미리 만들어둠
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")  # 한/글 객체 생성
    hwp.RegisterModule("FilePathCheckDLL", "FilePathCheckerModule")  # 보안모듈 실행
    hwp.Open(filename)  # GUI에서 선택한 파일 열기
    hwp.XHwpWindows.Item(0).Visible = True  # 한/글 창 숨김해제(초기에는 백그라운드상태)
    # hwp.HAction.Run("FrameFullScreen")  # 전체화면
    return hwp  # hwp객체 리턴
