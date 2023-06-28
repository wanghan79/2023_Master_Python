import random
import string
import random

def random_str(range_of_data):
    n = random.randint(range_of_data[0], range_of_data[1])
    it = ''.join(random.sample(string.ascii_letters + string.digits, n))
    return it

def get_random(*args):
    num = len(args)
    if num <= 0:
        print("内容为空！！！")
        return None
    else:
        result = []
        for i in range(num):
            it = None
            arg = args[i]
            range_of_data = arg[0]
            type_of_data = arg[1]
            if(isinstance(range_of_data,tuple)):
                if type_of_data == float:
                    it = random.uniform(range_of_data[0], range_of_data[1])
                elif type_of_data == int:
                    it = random.randint(range_of_data[0], range_of_data[1])
                elif type_of_data == str:
                    it = random_str(range_of_data)
                elif type_of_data == tuple:
                    range_of_id = range_of_data[0]
                    range_of_name_len = range_of_data[1]
                    id = random.randint(range_of_id[0], range_of_id[1])
                    n = random.randint(range_of_name_len[0], range_of_name_len[1])
                    s = random_str(range_of_name_len)
                    it = (id, s)
                elif type_of_data == list:
                    range_of_list = range_of_data[0]
                    n = random.randint(range_of_data[0][0], range_of_data[0][1])
                    type_of_list = range_of_data[1]
                    it = []
                    temp = None
                    for j in range(n):
                        if type_of_list == float:
                            temp = random.uniform(range_of_list[0], range_of_list[1])
                        elif type_of_list == int:
                            temp = random.randint(range_of_list[0], range_of_list[1])
                        elif type_of_list == str:
                            temp = random_str(range_of_list)
                        it.append(temp)
                elif type_of_data == set:
                    range_of_set = range_of_data[0]
                    n = random.randint(range_of_data[0][0], range_of_data[0][1])
                    type_of_set = range_of_data[1]
                    it = []
                    temp = None
                    for j in range(n):
                        if type_of_set == float:
                            temp = random.uniform(range_of_set[0], range_of_list[1])
                        elif type_of_set == int:
                            temp = random.randint(range_of_set[0], range_of_set[1])
                        elif type_of_set == str:
                            temp = random_str(range_of_set)
                        it.append(temp)

            result.append(it)
    return result






