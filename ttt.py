import tkinter as tk  # Импорт библиотеки Tkinter для создания графического интерфейса
from tkinter import messagebox  # Импорт модуля messagebox для вывода диалоговых окон
import time  # Импорт модуля time для измерения времени выполнения операций

class SortApp:
    def __init__(self, master):
        self.master = master  # Сохранение ссылки на основное окно приложения
        master.title("Сортировка чисел")  # Установка заголовка для основного окна

        # Создание и размещение метки для поля ввода чисел
        self.input_label = tk.Label(master, text="Введите числа через запятую:")
        self.input_label.pack()

        # Создание и размещение поля ввода чисел
        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        # Создание и размещение метки для выбора метода сортировки
        self.sort_label = tk.Label(master, text="Выберите метод сортировки:")
        self.sort_label.pack()

        # Создание переменной для хранения выбранного метода сортировки и установка значения по умолчанию
        self.sort_option = tk.StringVar(master)
        self.sort_option.set("Сортировка пузырьком")

        # Создание выпадающего меню для выбора метода сортировки
        self.sort_menu = tk.OptionMenu(master, self.sort_option, "Сортировка пузырьком", "Сортировка подсчетом", "Сортировка слиянием", "Пирамидальная сортировка")
        self.sort_menu.pack()

        # Создание и размещение кнопки для запуска сортировки
        self.start_button = tk.Button(master, text="Start", command=self.sort_numbers)
        self.start_button.pack()

        # Создание и размещение метки для вывода результата
        self.output_label = tk.Label(master, text="Результат:")
        self.output_label.pack()

        # Создание и размещение текстового поля для вывода результата
        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.pack()

        self.clear_button = tk.Button(master, text="Clear", command=self.clear_output)
        self.clear_button.pack()

    def sort_numbers(self):
        # Получение введенного пользователем текста и выбранного метода сортировки
        input_text = self.input_entry.get()
        sort_method = self.sort_option.get()

        try:
            # Преобразование введенного текста в список чисел, разделенных запятыми
            numbers = [int(x.strip()) for x in input_text.split(",")]
        except ValueError:
            # Вывод сообщения об ошибке, если введены некорректные данные
            messagebox.showerror("Ошибка", "Введите корректную последовательность чисел")
            return

        start_time = time.time()  # Запись текущего времени начала выполнения сортировки

        # Выбор и выполнение соответствующего метода сортировки
        try:
            if sort_method == "Сортировка пузырьком":
                self.bubble_sort(numbers)
            elif sort_method == "Сортировка подсчетом":
                self.counting_sort(numbers)
            elif sort_method == "Сортировка слиянием":
                self.merge_sort(numbers)
            elif sort_method == "Пирамидальная сортировка":
                self.heap_sort(numbers)
        except OverflowError:
            messagebox.showerror("Ошибка", "Одно или более из введеных вами чисел слишком большое")
            return
        except MemoryError:
            messagebox.showerror("Ошибка", "Одно или более из введеных вами чисел слишком большое")
            return

        end_time = time.time()  # Запись текущего времени окончания выполнения сортировки

        # Очистка текстового поля вывода и вывод результата сортировки
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Отсортированная последовательность:\n")
        self.output_text.insert(tk.END, ", ".join(map(str, numbers)))
        self.output_text.insert(tk.END, f"\n\nВремя выполнения: {end_time - start_time:.5f} сек")

    def clear_output(self):
            self.output_text.delete(1.0, tk.END)
            
    def bubble_sort(self, arr):
        # Реализация алгоритма сортировки пузырьком
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def counting_sort(self, arr):
        # Реализация алгоритма сортировки подсчетом
        max_num = max(arr)
        count = [0] * (max_num + 1)
        sorted_arr = [0] * len(arr)

        for num in arr:
            count[num] += 1

        for i in range(1, max_num + 1):
            count[i] += count[i - 1]

        for num in reversed(arr):
            sorted_arr[count[num] - 1] = num
            count[num] -= 1

        for i in range(len(arr)):
            arr[i] = sorted_arr[i]

    def merge_sort(self, arr):
        # Реализация алгоритма сортировки слиянием
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def heapify(self, arr, n, i):
        # Вспомогательная функция для пирамидальной сортировки
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr, n, largest)

    def heap_sort(self, arr):
        # Реализация алгоритма пирамидальной сортировки
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)


root = tk.Tk()  # Создание основного окна приложения
app = SortApp(root)  # Создание экземпляра приложения, связанного с основным окном
root.mainloop()  # Запуск бесконечного цикла обработки событий для работы графического интерфейса
