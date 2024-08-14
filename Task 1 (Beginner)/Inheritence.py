class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def receive_call(self, number):
        print(f"Receiving call from {number}...")

    def take_a_picture(self):
        print(f"Taking a picture with {self.rear_camera} rear camera...")

class Apple(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, ios_version):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.ios_version = ios_version

    def get_info(self):
        return (f"Apple Phone: ScreenType: {self.screen_type}, NetworkType: {self.network_type}, "
                f"DualSim: {self.dual_sim}, FrontCamera: {self.front_camera}, RearCamera: {self.rear_camera}, "
                f"RAM: {self.ram}, Storage: {self.storage}, iOS Version: {self.ios_version}")

class Samsung(MobilePhone):
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage, android_version):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.android_version = android_version

    def get_info(self):
        return (f"Samsung Phone: ScreenType: {self.screen_type}, NetworkType: {self.network_type}, "
                f"DualSim: {self.dual_sim}, FrontCamera: {self.front_camera}, RearCamera: {self.rear_camera}, "
                f"RAM: {self.ram}, Storage: {self.storage}, Android Version: {self.android_version}")

# Creating objects of Apple class with different properties
iphone_12 = Apple("Touch Screen", "5G", False, "12MP", "48MP", "4GB", "64GB", "iOS 14")
iphone_11 = Apple("Touch Screen", "4G", False, "8MP", "32MP", "3GB", "32GB", "iOS 13")

# Creating objects of Samsung class with different properties
samsung_s21 = Samsung("Touch Screen", "5G", True, "16MP", "48MP", "4GB", "64GB", "Android 11")
samsung_s20 = Samsung("Touch Screen", "4G", True, "12MP", "32MP", "3GB", "32GB", "Android 10")

# Displaying information about each phone
phones = [iphone_12, iphone_11, samsung_s21, samsung_s20]

for phone in phones:
    print(phone.get_info())
    phone.make_call("1234567890")
    phone.receive_call("0987654321")
    phone.take_a_picture()
    print()
