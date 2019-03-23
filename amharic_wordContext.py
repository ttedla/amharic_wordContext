from collections import defaultdict
from itertools import islice 
def open_file(name):
    with open(name, 'r', encoding='utf-8-sig') as file_to_read:
        f_read=file_to_read.read().replace('\n', '')
        open_file.f_read = f_read
        f_read=remove_chars(f_read)
        return f_read


def remove_chars(from_file):
    chars_to_remove = str.maketrans("\t«»!፣፧፡", 7*(" "))
    chars_removed= [f.translate(chars_to_remove) for f in from_file.splitlines() if f]
    remove_chars.chars_removed = chars_removed
    chars_removed = make_sentence(chars_removed)
    return chars_removed

def make_sentence(from_file):
    make_sentence.file_sentence = [sentence.split('።') for sentence in from_file]
    make_sentence.clean_sentences= [make_sentence.clean_sentence for cc_sentence in
                                    make_sentence.file_sentence for
                                    make_sentence.clean_sentence
            in cc_sentence]
    make_sentence.clean_sentences_saved = make_sentence.clean_sentences 
    make_sentence.clean_sentences=make_sentece_index(make_sentence.clean_sentences)
    return make_sentence.clean_sentences

def make_sentece_index(from_file):
    """Uses default dict from collections"""
    sentence_word_index = defaultdict(set)
    for index,sentence in enumerate(from_file):
        for word in sentence.split():
            sentence_word_index[word].add(index)
    make_sentece_index.sentence_word_index = sentence_word_index 
    return make_sentece_index.sentence_word_index 

def search_sentence():
    s_index=open_file(file_name)
    word = input("Enter the word to identify its context:>")
    sentences_with_word = []
    word_index = make_sentece_index.sentence_word_index[word]
    for word_sentence in word_index:
        sentences_with_word.append(make_sentence.clean_sentences_saved[word_sentence])
    
    format_sentence(sentences_with_word)
def format_sentence(output):
    sentences = [(" ".join(sentence.split())+"።") for sentence in output]
    for sentence in sentences:
        print(sentence, "\n")
# top n words from the document 
def top_n(n, file_where):
    return list(islice(file_where, n))
   

def sort_dict(my_dict):
    number = int(input("Enter the number of top n frequent words you want to see:>"))
    sort_dict.sorted_dict = sorted(my_dict.items(), key=lambda valkey: valkey[1],
                  reverse=True)
    return top_n(number,sort_dict.sorted_dict)

#TODO
# we can do the summary using the top_x words

def word_freq():
    my_dictionary = defaultdict(int)
    char_table = str.maketrans("\t«»!፣፧፡።", 8*(" "))
    my_file = open_file.f_read.translate(char_table)
    word_list = [word for word in my_file.split() ]
    for word in word_list:
        my_dictionary[word]+=1
    
    return sort_dict(my_dictionary)	



if __name__ == '__main__':
	file_name='./texts/አልወለድም_በአቤ_ጉበኛ.txt'
	open_file(file_name)
	print(word_freq())
	search_sentence()


