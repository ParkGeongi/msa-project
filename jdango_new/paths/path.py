import os
import platform
myos = platform.system()
root = r"C:\Users\AIA\project\jdango_new"
def dir_path(param):
    if (param == "lambdas") :
        return os.path.join(root, "basic", param)

    elif (param == "busers") \
            or (param == "comments") \
            or (param == "posts") \
            or (param == "tags"):
        return os.path.join(root, "blog", param)
    elif (param == "services"):
        return os.path.join(root, "cmm", param)

    elif (param == "fruits") \
            or (param == "iris") \
            or (param == "MFCC") \
            or (param == "mnist") \
            or (param == "number") \
            or (param == "squart") \
            or (param == "stroke"):
        return os.path.join(root, "ml", param)

    elif (param == "cinemas") \
            or (param == "movies")\
            or (param == "musers")\
            or (param == "showtimes")\
            or (param == "theaters") \
            or (param == "theaters_tickets"):
        return os.path.join(root, "movie", "vision", param)

    elif (param == "imdb") \
        or (param == "naver_movie")\
        or (param == "samsung_report"):

        return os.path.join(root, "nlp", param)


    elif (param == "seq_users"):
        return os.path.join(root, "security", "webcrawler", param)

    elif (param == "carts") \
            or (param == "categories") \
            or (param == "deliveries") \
            or (param == "orders")\
            or (param == "products")\
            or (param == "susers"):
        return os.path.join(root, "shop", param)

    elif (param == "webcrawler"):
        return os.path.join(root, param)
    elif (param == "aitrader"):
        return os.path.join(root,'dlearn', param)
