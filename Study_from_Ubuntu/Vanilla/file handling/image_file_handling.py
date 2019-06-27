doggy = open('/home/kimhippo/바탕화면/Python Practice/Python Practice to Ubuntu/Vanilla/smile_sammy.jpeg', "rb")
doggy2 = open('/home/kimhippo/바탕화면/Python Practice/Python Practice to Ubuntu/Vanilla/smile_sammy.jpeg', "wb")
doggy2.write(doggy.read())

doggy.close()
doggy2.close()