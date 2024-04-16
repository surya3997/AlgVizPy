word_list = list("abc")

def fun(word, swapping):
    n = len(word_list)
    for i in range(swapping, n):
        tmp = word[swapping]
        word[swapping] = word[i]
        word[i] = tmp

        fun(word, swapping+1)
        if swapping == (n - 1):
            print(word)

        tmp = word[swapping]
        word[swapping] = word[i]
        word[i] = tmp

fun(word_list, 0)