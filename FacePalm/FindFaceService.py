import random

class FindFaceService(object):
    """description of class"""

    _persons = {"person1": 0, "person2": 1, "person3": 2, "person4": 3, "person5": 4, "person6": 5, "person7": 6, "person8": 7, "person9": 8, "person10": 9, "person11": 10}

    def identify(photoUrl, treshold, n):
        print ("identify")
        rand = random.randint(0, 10)
        rand2 = random.randint(1, n)
        
        for i in range(rand, rand + rand2 ):
            print(i)

        #if rand > rand2:
        #    rand, rand2 = rand2, rand

        range1 = 34324234

        return range1