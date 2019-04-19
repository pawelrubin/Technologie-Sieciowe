import protocol as prot
import random as r

def long_random_bits():
    output = ""
    for i in range(2137):
        output += "{0:b}".format(r.randint(2^31, 2^32))
    return output

def random_file(filename):
    with open(filename, 'w') as file:
        file.write(long_random_bits())

def encode_file(input, output):
    with open(input, 'r') as file:
        open(output, 'w').write(prot.encode_frame(file.read()))

def main():
    random_file("z.txt")
    encode_file("z.txt", "w.txt")

if __name__ == "__main__":
    main()