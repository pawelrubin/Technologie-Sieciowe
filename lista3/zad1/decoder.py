import protocol as prot

def decode_file(input_name, output_name):
    with open(input_name, 'r') as input:
        open(output_name, 'w').write(prot.decode_frame(input.read()))

def main():
    decode_file("w.txt", "z2.txt")


if __name__ == "__main__":
    main()