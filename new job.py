import stanfordcorenlp #something is wrong
stanfordcorenlp.download('en')   # This downloads the English models for the neural pipeline
nlp = stanfordcorenlp.pipeline() # This sets up a default neural pipeline in English
doc = nlp("Barack Obama was born in Hawaii.  He was elected president in 2008.")
doc.sentences[0].print_dependencies()
