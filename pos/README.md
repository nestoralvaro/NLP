# POS

This software is a POS (Part of Speech) tagging tool for texts in Spanish
<br/>
There are two different taggers that can be used
* Stanford tagger
* NLTK tagger

##  Importing the library
To use the tagger the first action is to import it to the project
<br/>

```
from pos import POS_tagger
```

##  Loading the tagger
<br/>
Following, you have to load it using the desired configuration.
<br/>
The configuration variables are contained in the `config` file, so to use it we load it.
<br/>

```
from pos.config import STANFORD_TAGGER_NAME
from pos.config import NLTK_TAGGER_NAME
```


###  Loading Stanford tagger
For loading the Stanford tagger, use the following command
<br/>

```
pos_tagger = POS_tagger(STANFORD_TAGGER_NAME)
```


###  Loading NLTK tagger
For loading NLTK tagger, use the following command

```
pos_tagger = POS_tagger(NLTK_TAGGER_NAME)
```


##  Using the tagger
Lastly, we can tag the sentences.
<br/>
The sentences should be passed to the tagger as a list of words. To do so we use the tokenization function provided in NLTK.

```
sentence = "Esto es una prueba interesante."
from nltk.tokenize import word_tokenize
sentence_words = word_tokenize(sentence)
```

Following, we can obtain all the tags

```
all_tags = pos_tagger.get_tags(sentence_words)
# Result when using Stanford tagger:
#   [(u'Esto', u'pd000000'), (u'es', u'vsip000'), (u'una', u'di0000'), (u'prueba', u'nc0s000'), (u'interesante', u'aq0000'), (u'.', u'fp')]
# Result when using NLTK tagger:
#   [('Esto', u'pd0ns000'), ('es', u'vsip3s0'), ('una', u'di0fs0'), ('prueba', u'ncfs000'), ('interesante', u'aq0cs0'), ('.', u'Fp')]

```

As these results are not very easy to read we provide utility functions to obtain different elements in the sentence.

### Obtaining the adjectives in the sentence
To obtain the adjectives in hte sentence we run the following command

```
pos_tagger.detect_adjectives(all_tags)
# Result when using Stanford tagger:
#   [u'interesante']
# Result when using NLTK tagger:
#   ['interesante']
"""
```

### Obtaining the nouns in the sentence
To obtain the adjectives in hte sentence we run the following command

```
pos_tagger.detect_nouns(all_tags)
# Result when using Stanford tagger:
#   [u'prueba']
# Result when using NLTK tagger:
#   ['prueba']
```

### Obtaining the verbs in the sentence
To obtain the verbs in hte sentence we run the following command

```
pos_tagger.detect_verbs(all_tags)
# Result when using Stanford tagger:
#   [u'es']
# Result when using NLTK tagger:
#   ['es']
```
