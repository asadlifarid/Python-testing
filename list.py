class List:
    words = input().split()
    
    list_ = []

    def list_func(self):
        for word in List.words:
            if 'a' in word:
                List.list_.append(word)
        return List.list_

myclass = List()
print(myclass.list_func())