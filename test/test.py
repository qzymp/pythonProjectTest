


from random import randrange, randint

# print(randrange(4))


# items1 = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10))))
# print(items1)sada


# LOGID_BATTLE_CHAT_FLOW|1.1.14.1|2022-10-19 19:45:58|GU_1131|1|1001|67601510198587|0|30|eb3b351dbd238bd2e939cddd672e6bf3|3146137716661796911|25|\
#                                                  114+1,112+1,111+1,113+1,115+1,104+1,102+1,101+1,103+1,105+1,10+2,109+1,7+3,107+1,6+2,106+1,9+3,108+1,11+2,110+1,120+1,118+1,116+1,119+2,117+1



# LOGID_BATTLE_CHAT_FLOW|1.1.14.1|2022-10-19 19:45:58|GU_1131|1|1001|67627682655547|0|30|47231eaa62abe939b3c06a085bbf0183|3146137716661796911|25|\
#                                                 114+1,112+1,111+1,113+1,115+1,104+1,102+1,101+1,103+1,105+1,10+2,109+1,7+3,107+1,6+2,106+1,9+3,108+1,11+2,110+1,120+1,118+1,116+1,119+2,117+1




def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)
