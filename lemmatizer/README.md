# Lemmatization
This python module returns the lemma for a word in Spanish.
<br/>
The module uses a large knowledge bases consisting in almost 500,000 words with their corresponding lemmas.

## Usage
To use this module we have to import it to our project.

```
from lemmatizer import Spanish_Lemmatizer
```

<br/>
Then, we have to load it

```
lemmatizer = Spanish_Lemmatizer()
```

<br/>
At this point, we can use the lemmatizer to lemmatize any word.

```
resulting_lemma = lemmatizer.get_lemma("hablásemos")
print(resulting_lemma) # hablar
```

### Uncommon words
Not all words in the Spanish vocabulary are contained in the knowledge base. When any of these uncommon word appears the lemmatizer will return the very same word that the user wants to lemmatize.
<br/>

```
resulting_lemma = lemmatizer.get_lemma("Españolizamiento")
print(resulting_lemma) # españolizamiento
```

# Caution
All words that are passed to the lemmatizer will be returned in lower case.
<br/>

```
resulting_lemma = lemmatizer.get_lemma("HoLa")
print(resulting_lemma) # hola
```

<br/>
The same happens when the word in not in the knowledge base (it's an uncommon word)

```
resulting_lemma = lemmatizer.get_lemma("ESPAÑOLIZAMIENTO")
print(resulting_lemma) # españolizamiento
```
