from FASTA import ReadFASTA

def find_overlaps(arr, acc=''):
    if len(arr) == 0:
        return acc

    elif len(acc) == 0:
        acc = arr.pop(0)
        return find_overlaps(arr, acc)

    else:

        for i in range(len(arr)):
            a = arr[i]
            l = len(a)

            for p in range(l // 2):
                q = l - p

                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return find_overlaps(arr, a[:p] + acc)

                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return find_overlaps(arr, acc + a[q:])


if __name__ == "__main__":
    dna_list = ReadFASTA('data/rosalind_long.txt')
    reads = []
    for x in dna_list:
        reads.append(x[1]) 
    with open('output/rosalind_long.txt', "w") as fout:
        result = find_overlaps(reads)
        fout.write(result)
