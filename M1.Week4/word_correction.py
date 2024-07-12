
import streamlit as st

def levenshtein_distance(token1, token2):
    # Your Code Here
    distance = 0
    m = len(token1)
    n = len(token2)
    ld = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        ld[i][0] = i
    for i in range(n+1):
        ld[0][i] = i
    for i in range(1, m+1):
        for j in range(1, n+1):
            ld[i][j] = min(ld[i-1][j]+1, ld[i][j-1]+1, ld[i-1]
                           [j-1]+(token1[i-1] != token2[j-1]))
    distance = ld[m][n]
    # End Code Here
    return distance


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(file_path='./data/vocab.txt')


st.title("Word correction using Levenshtein distance")
word = st.text_input("Your word:")
if st.button("Compute"):
    distances = dict()
    for vocab in vocabs:
        distance = levenshtein_distance(word, vocab)
        distances[vocab] = distance
    sorted_distances = dict(
        sorted(distances.items(), key=lambda item: item[1]))
    correct_word = list(sorted_distances.keys())[0]
    st.write('Corect word: ', correct_word)

    col1, col2 = st.columns(2)
    with col1:
        st.write('Vocabulary: ', vocabs)
    with col2:
        st.write('Distance: ', sorted_distances)
