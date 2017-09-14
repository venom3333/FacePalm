from FindFaceService import FindFaceService

class Server(object):
    """description of class"""
    
    def request(photo, rating):
        print("Отправляем рейтинг и фото")
        range = FindFaceService.identify(photo, .97, 5)

        currentRating = 0
        return currentRating


