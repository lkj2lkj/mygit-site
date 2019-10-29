from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'D:\stanford-coreNLP-full-2018-10-05\stanford-corenlp-full-2018-10-05', lang='zh')

sentence = '清华大学位于北京。'
print(nlp.word_tokenize(sentence))#断句
print(nlp.pos_tag(sentence))#词性标签，可查询词性列表
print(nlp.ner(sentence))#命名实体识别
print(nlp.parse(sentence))#从语法上分析分列
print(nlp.dependency_parse(sentence))#依赖-分析
