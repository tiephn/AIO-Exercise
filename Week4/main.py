import streamlit as st

st.markdown("# Heading 1")
st.markdown("[AI VIỆT NAM](https://aivietnam.edu.vn/)")
st.markdown("""
            1. Machine learning
            2. Deep learning
            """)
st.markdown("$\sqrt{2x+2}$")
st.latex("\sqrt{2x+2}")


def get_fullname():
    st.write("Vừa bấm em à")


agree = st.checkbox("anh ơi bấm em", on_change=get_fullname())
if agree:
    st.write('thank you => Em yêu anh Tiệp')
else:
    st.write("I'm Sorry")

st.radio("Màu của bạn là:", ['Yellow', 'Blue'], captions=['Vàng', 'Xanh'])

title = st.text_input("Movie title", "Life of brain")
st.write("The current movie title: ", title)

uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename: ", uploaded_file.name)

st.divider()
col1, col2 = st.columns(2)
col1.write("Nội dung cột 1")
col1.divider()
col2.write("Nội dung cột 2")


#options = st. multiselect (" Your favorite colors a:")
#st. write ("You selected :", options )
options = st. multiselect (" Your favorite colors b:", ["Green", "Yellow", "Red", "Blue"], ["Yellow", "Red"])
options = st. multiselect (" Your favorite colors c:", ["Green", "Yellow", "Red", "Blue"], ["Yellow", "Red"])
st. write ("You selected :", options )
options = st. selectbox (" Your favorite colors d:", ["Green", "Yellow", "Red", "Blue"], ["Yellow", "Red"])
st. write ("You selected :", options )

st.divider()

with st.form('Nhập thông tin ngon vào nhé cưng'):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("Name:")
    f_age = col2.text_input("Age:")
    submited = st.form_submit_button('Xong rồi ạ')
    if submited:
        st.write(f"Name: {f_name}, Age: {f_age}")

st.divider()


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

st.title("Word correction")
word = st.text_input("Your word")
if st.button("compute"):
    distances = dict()
    for vocab in vocabs:
        distance = levenshtein_distance(word, vocab)
        distances[vocab] = distance
    sorted_distances = dict(
        sorted(distances.items(), key=lambda item: item[1]))
    correct_word = list(sorted_distances.keys())[0]
    st.write('corect word: ', correct_word)

st.divider()
