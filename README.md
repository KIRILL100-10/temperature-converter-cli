# Temperature Converter CLI / Конвертер температуры CLI

[EN] A simple and fast command-line utility written in Python to convert temperatures between Celsius, Fahrenheit, and Kelvin.
[RU] Простая и быстрая консольная утилита на Python для конвертации температуры между Цельсием, Фаренгейтом и Кельвином.

## Особенности / Features

* **[EN] Bilingual interface:** Support for English and Russian languages (EN/RU).
**[RU] Двуязычный интерфейс:** Поддержка английского и русского языков (EN/RU).
* **[EN] All popular scales:** Conversion in any direction (°C, °F, K).
**[RU] Все популярные шкалы:** Конвертация в любых направлениях (°C, °F, K).
* **[EN] Reliability:** Protection against invalid input and graceful shutdown via Ctrl+C.
**[RU] Надежность:** Защита от ввода некорректных данных и мягкое завершение работы по Ctrl+C.
* **[EN] No dependencies:** Uses only built-in Python modules.
**[RU] Без зависимостей:** Использует только встроенные модули Python.

## Установка и запуск / Installation and Launch

### Arch Linux / Manjaro

[EN] The package is officially available in the AUR. You can install it using any AUR helper, for example, `yay`:
[RU] Пакет официально доступен в AUR. Вы можете установить его с помощью любого AUR-помощника, например, `yay`:

yay -S temperature-converter-cli

### Docker (All OS & Distributions / Для всех ОС и дистрибутивов)

[EN] For other Linux distributions, Windows, or macOS, you can run the utility via Docker without installing Python. Use the official interactive Docker image:
[RU] Для других дистрибутивов Linux, Windows или macOS вы можете запустить утилиту через Docker, не устанавливая Python. Используйте официальный интерактивный Docker-образ:

docker run -it (--rm) (--name temperature-converter-cli) kirillnadtochaev/temperature-converter-cli

### Ручная установка / Manual Installation

[EN] Alternatively, you can clone the repository and run it manually:
[RU] Либо вы можете вручную склонировать репозиторий и запустить скрипт:

git clone https://github.com/KIRILL100-10/temperature-converter-cli
cd temperature-converter-cli
python main.py

## Использование / Usage

[EN] Run the utility and follow the on-screen instructions to select the language and conversion mode:
[RU] Запустите утилиту и следуйте инструкциям на экране для выбора языка и режима конвертации:

python main.py

## Лицензия / License

[EN] This project is licensed under the MIT License - see the LICENSE file for details.
[RU] Проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

---
