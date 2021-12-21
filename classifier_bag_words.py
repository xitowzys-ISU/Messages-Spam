import re
import nltk

def classifier_bag_words(mess):
    messages_no_punctuation = []
    messages_classifier = []

    # Удалить ненужные символы, цифры и знаки препинания
    for line in mess:
        if line:
            messages_no_punctuation.append(re.sub('[^A-Za-z]', ' ', line))

    # Соединяем символы
    messages_no_punctuation = ''.join(messages_no_punctuation)

    # Делаем слова строчными
    messages_no_punctuation = messages_no_punctuation.lower()

    # Удаляем стоп-слова из списка
    for word in messages_no_punctuation.split():
        messages_classifier.append(word)

    for word in messages_classifier:
        if word in nltk.corpus.stopwords.words('english'):
            messages_classifier.remove(word)

    return messages_classifier
