# Bars Parser
<p align=center>
<br>
  <span>Составьте полный список учеников вашей школы и их родителей</span>
  <br>
 
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
  <a target="_blank" href="LICENSE" title="License: AGPL v3"><img src="https://img.shields.io/badge/License-AGPL%20v3-green.svg"></a>
  <a target="_blank"><img alt="docker image" src="https://img.shields.io/badge/version-0.2-informational"></a>
</p>


## Установка

```console
git clone https://github.com/NoPlagiarism/bars-parser.git

cd bars-parser

pip install -r requirements.txt
```

Если вы будете запускать через repl.it, то не забудьте ввести в Shell - `pip install -r requirements.txt`

[![Run on Repl.it](https://user-images.githubusercontent.com/27065646/92304596-bf719b00-ef7f-11ea-987f-2c1f3c323088.png)](https://repl.it/github/NoPlagiarism/bars-parser)

## Использование

- Сначала зайдите в электронную школу и откройте консоль разработчика и совершите любой переход по вкладкам школы
- В окне разработчика найдите вкладку Network и выберете любой запрос, у которого указан домен вашей электронной школы
- Нажмите на этот запрос правой кнопкой мыши и выберите "Копировать" -> "Копировать как cURL (Windows)"
- Затем вставьте содержимое буфера обмена вместо содержимого файла curl.txt
- И запустите основной файл коммандой `python main.py`
- school_db.json хранит в себе результат

## TODO

- [ ] - Полная переработка всего и вся
- [ ] - Добавить добавление новой информации
- [ ] - Составление списка не только по родителям, но и по детям
- [ ] - Добавление человеческой инфы

## License

GNU AGPL V3 © [NoPlagiarism](https://github.com/NoPlagiarism) <br/>
Используйте код, но лучше укажите автора пожалуйста :)
