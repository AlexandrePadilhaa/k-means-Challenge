import numpy as np
import json
import sys


def main():
    if len(sys.argv) != 4:
        print("Estrutura: python k-means.py input_file k output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    k = int(sys.argv[2])
    output_file = sys.argv[3]

    print("Arquivo de entrada: ",input_file," K: ",k," Arquivo de saida: ", output_file)

if __name__ == "__main__":
    main()