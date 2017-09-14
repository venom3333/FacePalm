from Server import Server

rating = input("Введите рейтинг: ")

server = Server
currentRating = server.request("photo1", rating)
