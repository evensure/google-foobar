import string

def solution(x):
    d = {string.ascii_lowercase[i]: string.ascii_lowercase[::-1][i] for i in range(len(string.ascii_lowercase))}
    output = ""
    for letter in x:
        if letter in d.keys():
            letter = letter.replace(letter, d[letter])
        output += letter
    return output

if __name__ == "__main__":
    print(solution("Tsrh xszoovmtv rh hloevw!"))
