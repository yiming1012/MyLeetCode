"""
TF-IDF:一种针对关键词的统计分析方法
TF-IDF（Term Frequency-inverse Document Frequency）是一种针对关键词的统计分析方法，用于评估一个词对一个文件集或者一个语料库的重要程度。
一个词的重要程度跟它在文章中出现的次数成正比，跟它在语料库出现的次数成反比。
这种计算方式能有效避免常用词对关键词的影响，提高了关键词与文章之间的相关性。

其中TF指的是某词在文章中出现的总次数，该指标通常会被归一化定义为
TF=（某词在文档中出现的次数/文档的总词量），这样可以防止结果偏向过长的文档（同一个词语在长文档里通常会具有比短文档更高的词频）。
IDF逆向文档频率，包含某词语的文档越少，IDF值越大，说明该词语具有很强的区分能力，
IDF=loge（语料库中文档总数/包含该词的文档数+1），+1的原因是避免分母为0。TFIDF=TFxIDF，TFIDF值越大表示该特征词对这个文本的重要性越大。
"""
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = TfidfVectorizer()
tdm = vectorizer.fit_transform(corpus)
space = vectorizer.vocabulary_
print(space)
