# Spell Checker

This software is a Spell Checker tool for texts in Spanish
<br/>
The spell checker is based on the one proposed by (Peter Norvig)[http://norvig.com/spell-correct.html], and adapted to be used with texts written in Spanish.

##  Importing the library
To use the tagger the first action is to import it to the project
<br/>

```
from spell import Spanish_Spell_Checker
```

###  Loading Spell Checker
For loading the Spell Checker, use the following command
<br/>

```
spell_checker = Spanish_Spell_Checker()
```



##  Using the Spell Checker
Lastly, we can check the spell of any word.

```
self.spell_checker.correction("ohla") # hola
```


## Using texts of different genre
The function works by returing the most probable word given a corpus.
<br/>
This means that the corpus plays an important role and the same word can be corrected differently depending on the corpus we use.
<br/>
The corpus to be used in loaded in the configuration file. Any text can be used, although we provide the following corpora:
* We can use texts from Aristotle
* We can use the Bible
* We can use the subtitles from a TV show
* ...

```
# Text from Aristotle
WORDS_FILE_PATH = RESOURCES_FOLDER + "Aristoteles_Metafisica.txt"

# The Bible
WORDS_FILE_PATH = RESOURCES_FOLDER + "BIBLIA_COMPLETA.txt"

# Subtitles from a TV show (Friends)
WORDS_FILE_PATH = RESOURCES_FOLDER + "friends/transcripts.txt"

# The Quijote
WORDS_FILE_PATH = RESOURCES_FOLDER + "donquijote.txt"
```

The corpus that is used by default is the movie transcript from the TV drama Friends.

### Obtaining the corrections for different corpora
To obtain the correction for a word we use the following command

#### Correction for a word using the texts from Aristotle

```
spell_checker.correction("ohla") # la
spell_checker.correction("altz") # alto
spell_checker.correction("mobil") # móvil
```

#### Correction for a word using the texts The Bible

```
spell_checker.correction("ohla") # olla
spell_checker.correction("altz") # alto
spell_checker.correction("mobil") # obil
```

#### Correction for a word using the Subtitles from a TV show (Friends)

```
spell_checker.correction("ohla") # hola
spell_checker.correction("altz") # alta
spell_checker.correction("mobil") # moni
```

#### Correction for a word using the texts The Quijote

```
spell_checker.correction("ohla") # olla
spell_checker.correction("altz") # alta
spell_checker.correction("mobil") # mil
```

As we can see there are different responses for the same word, all deppending on the corpus.
<br/>
Given these results, the recommendation is to use a corpus similar to the text that is going to be evaluated.
