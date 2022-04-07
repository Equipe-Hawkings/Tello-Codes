from djitellopy import Tello


tello = Tello()
tello.connect(False)
print("Nível da bateria do Michel: ")
print(tello.get_state_field('bat'))