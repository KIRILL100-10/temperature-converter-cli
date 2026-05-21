#!/usr/bin/env python3
import sys


def celsius_to_fahrenheit(c):
    return c * 1.8 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) / 1.8 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 1.8 + 32


strings_dict = {
    'en': {
        'menu': '\n1. C -> F\n2. F -> C\n3. C -> K\n4. K -> C\n5. F -> K\n6. K -> F\n7. Exit',
        'choice': 'Choose conversion (1-7): ',
        'temperature': 'Enter temperature: ',
        'error_choice': 'Invalid choice, try again.',
        'error_number': 'Error: Please enter a valid number.',
        'exit': 'Goodbye!',
        'result': 'Result: '
    },
    'ru': {
        'menu': '\n1. C -> F\n2. F -> C\n3. C -> K\n4. K -> C\n5. F -> K\n6. K -> F\n7. Выход',
        'choice': 'Выберите конвертацию (1-7): ',
        'temperature': 'Введите температуру: ',
        'error_choice': 'Неверный выбор, попробуйте снова.',
        'error_number': 'Ошибка: Пожалуйста, введите число.',
        'exit': 'До свидания!',
        'result': 'Результат: '
    }
}


def main():
    print('--- Temperature Converter CLI / Конвертер температуры CLI ---')

    while True:
        language = input('Select language / Выберите язык (en/ru): ').strip().lower()
        if language in ['en', 'ru']:
            break
        print('Invalid language / Неверный язык. Use / Используйте en or / или ru')

    while True:
        print(strings_dict[language]['menu'])

        choice = input(strings_dict[language]['choice']).strip()

        if choice == '7':
            print(strings_dict[language]['exit'])
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print(strings_dict[language]['error_choice'])
            continue

        try:
            value = float(input(strings_dict[language]['temperature']))
        except ValueError:
            print(strings_dict[language]['error_number'])
            continue


        result_word = strings_dict[language]['result']

        print()

        if choice == '1':
            print(f'{result_word} {value}°C = {celsius_to_fahrenheit(value):.2f}°F')
        elif choice == '2':
            print(f'{result_word} {value}°F = {fahrenheit_to_celsius(value):.2f}°C')
        elif choice == '3':
            print(f'{result_word} {value}°C = {celsius_to_kelvin(value):.2f}K')
        elif choice == '4':
            print(f'{result_word} {value}K = {kelvin_to_celsius(value):.2f}°C')
        elif choice == '5':
            print(f'{result_word} {value}°F = {fahrenheit_to_kelvin(value):.2f}K')
        elif choice == '6':
            print(f'{result_word} {value}K = {kelvin_to_fahrenheit(value):.2f}°F')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExit / Выход')
        sys.exit(0)
