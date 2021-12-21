# Зачетная работа по искусственному интеллекту (Вариант #4)

## Задача
Написать программу, которая классифицирует сообщение спам или не спам

## Требования
1. Программа для обучение
2. Программа для обработки
3. Описание на страницу - как работает, какие результаты

## Структура проекта
1. [`data` - Папка с датасетов сообщений](https://gitlab.com/ISU-Applied-Computer-Science/5th-semester/artificial-intelligence/messages-spam/-/tree/main/data)
2. [`models` - Папка с моделями](https://gitlab.com/ISU-Applied-Computer-Science/5th-semester/artificial-intelligence/messages-spam/-/tree/main/models)
    > Пока что в папке models лежит одна натренированная модель [наивный байесовский классификатор](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) [ComplementNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html)
3. [`implementing.ipynb` - Блокнот для классификации сообщений](https://gitlab.com/ISU-Applied-Computer-Science/5th-semester/artificial-intelligence/messages-spam/-/blob/main/implementing.ipynb)
4. [`classifier_bag_words.py` - Функция предварительной обработки текста](https://gitlab.com/ISU-Applied-Computer-Science/5th-semester/artificial-intelligence/messages-spam/-/blob/main/classifier_bag_words.py)

## Краткое описание блокнотов

### [`traning.ipynb`](https://gitlab.com/ISU-Applied-Computer-Science/5th-semester/artificial-intelligence/messages-spam/-/blob/main/implementing.ipynb)

1. Импорт необходимых библиотек и загрузка стоп-слов для библиотеки [nltk](https://www.nltk.org)
2. Разархивация архива с датасетов сообщений
3. Просмотр и анализ датасета с помощью библиотеки [Pandas](https://pandas.pydata.org)
4. Разбиваем датасет на тестовые (20%) и тренировочные (80%) 
5. Настраивает конвейер Pipeline
   1. Преобразуем датасет в матрицу с помощью [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) с параметром **analyzer** в которую передан название функции для предварительной обработки текста [**classifier_bag_words**](https://gitlab.com/ISU-Applied-Computer-Science/5th-semester/artificial-intelligence/messages-spam/-/blob/main/classifier_bag_words.py)
   2. Преобразуйте матрицу подсчета в нормализованное представление [TF-IDF](https://en.wikipedia.org/wiki/Tf–idf) с помощью [TfidfTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html)
   3. Уставливаем классификатор [наивный байесовский классификатор](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) [ComplementNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.ComplementNB.html)
6. Обучаем модель
7. Прогнозирование значений в тестовом наборе данных для проверки модели
8. Сохранение моделей