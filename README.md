
# notes conclusions ![workflow](https://github.com/vncortez/NotesConclusions/actions/workflows/django.yml/badge.svg) [![Maintainability](https://api.codeclimate.com/v1/badges/a13f00c7bc1dd9481f20/maintainability)](https://codeclimate.com/github/vncortez/notesconclusions/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/a13f00c7bc1dd9481f20/test_coverage)](https://codeclimate.com/github/vncortez/notesconclusions/test_coverage)

## Variáveis de ambiente


Para rodar precisa de variáveis de ambiente como no exemplo abaixo.
~~~.env
HOSTS = []
DEBUG = True
DATABASE_URL = sqlite://$(pwd)/db.sqlite3
SECRET_KEY = o9ay-qj9zls73ngg_a0q#*72w%ik^of5&5auke2m-&*bjkjfx-
~~~

Além disso, é possível gerar esse código do secret key, dentro do pipenv shell com esse código

~~~bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())' 
~~~