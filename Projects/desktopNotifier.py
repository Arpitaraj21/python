from plyer import notification
import time 

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message = "Rest increases your mental focus, productivity, and creativity.",
            # app_icon = " for notification",
            timeout = 5
        )
        time.sleep(20)