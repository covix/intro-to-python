# counting DNA Nucleotides
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

for c in ["A", "C", "G", "T"]:
    print(s.count(c))

print()

# transcribing DNA into RNA
s = "GATGGAACTTGACTACGTAAATT"
print(s.replace("T", "U"))
print()


# complementing a strand of DNA
s = "AAAACCCGGT"
print(s[::-1].replace("A", "t").replace("C", "g").replace("G", "c").replace("T", "a").upper())
print()

