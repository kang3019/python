class TV:
    def __init__(self,channel,volume,on):
        self.channel = channel
        self.volume = volume
        self.on = on


    def turnOn(self):
        self.on = True
        print("TV를 켰습니다.")
        
    def turnOff(self) :
        self.on = False
        print("TV를 껐습니다.")

    def setChannel(self,channel) :
        if self.on:
            self.channel = channel
            print(f"채널을 {channel}번으로 변경했습니다.")
        else:
            print("TV가 꺼져 있어 채널 변경이 불가능합니다.")
            
    def setVolume(self,volume) :
        if self.on:
            self.volume = volume
            print(f"볼륨을 {volume}으로 변경했습니다.")
        else:
            print("TV가 꺼져 있어 볼륨 변경이 불가능합니다.")

    def showInfo(self):
       if self.on == True :
            print(f"TV의 채널: {self.channel}")
            print(f"TV의 음량: {self.volume}")
       else :
            print("TV 전원이 켜져있지 않습니다")
        
        
tv = TV(11,6,False)

menu = (
    "\n===== TV 메뉴 =====\n"
    "1. TV 켜기\n"
    "2. TV 끄기\n"
    "3. 채널 변경하기\n"
    "4. 볼륨 변경하기\n"
    "5. 상태 보기\n"
    "6. 종료\n"
    "메뉴 선택: "
)

while True:
    choice = input(menu)

    if choice == "1":
        tv.turnOn()

    elif choice == "2":
        tv.turnOff()

    elif choice == "3":
        new_channel = int(input("변경할 채널 번호: "))
        tv.setChannel(new_channel)

    elif choice == "4":
        new_volume = int(input("변경할 볼륨: "))
        tv.setVolume(new_volume)

    elif choice == "5":
        tv.showInfo()

    elif choice == "6":
        print("프로그램을 종료합니다.")
        break

    else:
        print("1~6 중에서 선택하세요.")
