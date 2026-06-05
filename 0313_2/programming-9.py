drive = input("드라이브 이름: ")
folder = input("디렉토리 이름: ")
file = input("파일 이름: ")
ext = input("확장자: ")

full = drive + ":" + folder + file + "." + ext

print("완전한 이름은", full)

#111p 사용자로부터 드라이브 이름, 디렉토리 이름, 파일 이름, 확장자를 입력받아서 완전한 파일 이름을 만들어주는 프로그램