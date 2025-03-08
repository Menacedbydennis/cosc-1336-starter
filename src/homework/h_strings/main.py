from homework.h_strings.strings import get_dna_complement, get_hamming_distance

def main():
    while True:
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dna1 = input("Enter first DNA sequence: ")
            dna2 = input("Enter second DNA sequence: ")
            if len(dna1) == len(dna2):
                print(f"Hamming Distance: {get_hamming_distance(dna1, dna2)}")
            else:
                print("Error: DNA sequences must be of equal length.")
        
        elif choice == '2':
            dna = input("Enter a DNA sequence: ")
            print(f"DNA Complement: {get_dna_complement(dna)}")
        
        elif choice == '3':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
