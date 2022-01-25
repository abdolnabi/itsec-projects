class RandomGenerator:

    def randgen(self,lower_bound=0,upper_bound=0):
        rand_num = self.__hash__()
        while rand_num < int(lower_bound):
                rand_num += rand_num >> int(str(rand_num)[:1])
                if rand_num > upper_bound:
                    rand_num += rand_num >> int(str(rand_num)[:1])
        return(rand_num)





# if __name__ == "__main__":
#     print(pow(2,1023))
#     random_number = RandomGenerator(pow(2,1023),pow(2,1024))
#     print(random_number.randgen)
#     random_number = RandomGenerator(pow(2,1023),pow(2,1024))
#     print(random_number.randgen)
#     random_number = RandomGenerator(pow(2,1023),pow(2,1024))
#     print(random_number.randgen)
#     random_number = RandomGenerator(pow(2,1023),pow(2,1024))
#     print(random_number.randgen)
#     random_number = RandomGenerator(pow(2,1023),pow(2,1024))
#     print(random_number.randgen)
#     print(pow(2,1024))