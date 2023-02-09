import os
import platform
myos = platform.system()
root = os.path.join(os.getcwd(), "app")

def dir_path(param):
    if (param == "chatbot") \
            or (param == "openai"):
        return os.path.join(root, "services", param)





