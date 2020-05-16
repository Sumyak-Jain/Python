def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    s_new=("".join(l))
    return (s_new)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
