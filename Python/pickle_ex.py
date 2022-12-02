import pickle

class example_pickle:
    def mypickle(self):
        a_num = 22
        a_str = "mystr"
        a_list = ["a", "b", "3"]
        a_tuple = ("1", "2", "c")
        a_dict = { "k1": 6, "k2": 7, "k3": "x" }
        return(a_num, a_str, a_list, a_dict)



if (__name__ == '__main__'):
    obj_C_pkl = example_pickle()
    obj_M_pkl = obj_C_pkl.mypickle()
    print(obj_M_pkl)

    ser = pickle.dumps(obj_C_pkl)
    print("Serialization:", ser)
    deser = pickle.loads(ser)
    print("De-serialization:", deser.mypickle())

    dbfile = open('examplepkl', 'ab')
    serM = pickle.dump(obj_M_pkl, dbfile)
    print("Serialization M:", serM)
    dbfile.close()

    dbfile2 = open('examplepkl', 'rb')  
    deserM = pickle.load(dbfile2)
    print("De-serialization M:", deserM)
