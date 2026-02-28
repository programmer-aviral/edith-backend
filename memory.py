FILE = "memory.txt"


def save_memory(text):

    with open(FILE, "a", encoding="utf-8") as f:

        f.write(text + "\n")



def load_memory():

    try:

        with open(FILE, "r", encoding="utf-8") as f:

            return f.read()

    except:

        return "No memory yet"
