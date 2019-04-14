# Text file reading

def read(filename, reducer=lambda result, word: result.append(word)):
    # Read the (potentially large) file efficiently through buffering and sort 
    # the list while creating it.
    result = []
    word = ""
    buffered = True
    in_word = False

    with open(filename) as words:
        while buffered:
            buffered = words.read(1024)
            j = 0
            i = buffered.find("\"")
            while i != -1:
                if in_word:
                    word += buffered[j:i]

                if word != "":
                    reducer(result, word)
                    in_word = False
                else:
                    in_word = j == 0
                    j = i + 1

                if not in_word:
                    # Next open
                    i = buffered.find("\"", i + 1)
                    j = i + 1
                    in_word = i != -1

                if i != -1:
                    # Next close
                    i = buffered.find("\"", i + 1)

                word = ""

            if j > 0:
                word = buffered[j:]
                
    return result
