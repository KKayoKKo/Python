class Television:
    serialNumber = 0 # 클래스 변수 (모든 객체가 공유)

    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

        Television.serialNumber += 1 # 객체가 생성될 때마다 1씩 증가 (전체 공유값 증가)

        self.number = Television.serialNumber # 각 객체의 고유 번호로 저장

    def show(self):
        print(self.channel, self.volume, self.on, self.number) # 인스턴스 변수 → 각 TV마다 따로 저장되는 값


myTV = Television(11, 10, True)

myTV.show()

# 클래스 변수