# DrugFinder

## Run

Musicie mieć zainstalowane docker i docker-compose, wtedy wystarczy odpalić w katalogu API `docker-compose build` (może chwile trwać) a następnie `docker-compose up -d`. Jeżeli wszystko pójdzie gładko, w przeglądarce wystarczy wpisać `localhost:8000`

## Dane

Wszystkie dane użyte do treningu modelu są danymi dostępnymi publicznie. Ze względu na charakter projektu oraz dostępność danych wykorzystane zostały dane w języku angielskim. Dane te pochodzą ze strony [NCBI DISEASE CORPUS](https://www.ncbi.nlm.nih.gov/research/bionlp/Data/disease/) i są to w pełni zanotowane dane korpusu słownego zbudowanego z:

 -   793 abstraktów publikacji ze strony PubMed
-   6,892 oznaczeń chorób
-   790 unikalnych oznaczonych chorób
-   Rozdzielone na dane treningowe, testowe oraz walidacyjne.

## Model

Model DL wybrany (**na tym etapie**) do tego zadania był model BioClinicalBert. Jest to model transformer, który był pretrenowany na notatkach z bazy danych MIMIC III, która zawiera medyczne rekordy ICU pacjentów ze szpitala Beth Israel Hospital w Bostonie.

**W następnych etapach projektu będą badane inne modele.**

### Wyniki

Wyniki przed dopasowaniem hiperparametrów:

 - eval_loss = 0.026682097223940594
- f1_score = 0.663080684596577
- precision = 0.6225895316804407
- recall = 0.7092050209205021

Wyniki po dostosowaniu hiperparametrów:

 - eval_loss = 0.03645656569090628
- f1_score = 0.7129306040938592
- precision = 0.6819484240687679
- recall = 0.7468619246861925


## Aplikacja webowa

Wraz z modelem została zbudowana aplikacja internetowa, umożliwiająca inferencję z modelem. Aplikacja umożliwia użytkownikowi podać notatkę lekarską, która przekazywana jest do modelu w celu predykcji i wyodrębnienia nazw chorób z notatki.

## Użyte technologie

 1. Python (pyTorch, transformers, HuggingFace, django)
 2. GCP
 3. GitLab

