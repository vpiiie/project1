import time
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
class Pet:   # класс, представляющий питомца с его состояниями и действиями
    def __init__(self):     #инициализирует параметры питомца
        self.name = "Стеша"
        self.food = 10
        self.fun = 10
        self.hygiene = 10
        self.health = 10
        self.last_action_time = time.time()
    def feed(self, food_choice):    # кормим питомца выбранным типом еды (1,2,3)
        if food_choice == "1":  #корм
            self.food += 2
        elif food_choice == "2":     #лакомство
            self.food += 1
        elif food_choice == "3":    #вода
            self.food += 1
        self.food = max(0, min(10, self.food))
        self.update_status()
    def play(self, activity_choice):    #играть с питомцем
        if activity_choice == "1":      #грызть вещи
            self.fun += 3
        elif activity_choice == "2":     #лазер
            self.fun += 1
        elif activity_choice == "3":     #погладить
            self.fun += 2
        self.fun = max(0, min(10, self.fun))
        self.update_status()
    def hygiene_up(self, action_choice):    #гигиена(1,2)
        if action_choice == "1":    #вычесать
            self.hygiene += 1
        elif action_choice == "2":  #душ
            self.hygiene += 2
        self.hygiene = max(0, min(10, self.hygiene))
        self.update_status()
    def heal(self, medicine_choice): #лечим
        if medicine_choice == "1":  #таблетка
            self.health += 2
        elif medicine_choice == "2":    #чудо микстурка
            self.health += 6
        self.health = max(0, min(10, self.health))
        self.update_status()
    def update_status(self):    #обновляем статус
        current_time = time.time()
        time_elapsed = current_time - self.last_action_time
        if time_elapsed >= 30:
            intervals_elapsed = int(time_elapsed // 30)
            self.food -= 1 * intervals_elapsed
            self.fun -= 2 * intervals_elapsed
            self.hygiene -= 1 * intervals_elapsed
            self.health -= 1 * intervals_elapsed
            self.last_action_time = current_time
            self.food = max(0, min(10, self.food))
            self.fun = max(0, min(10, self.fun))
            self.hygiene = max(0, min(10, self.hygiene))
            self.health = max(0, min(10, self.health))
    def get_status(self):   #возвращает состояние
        return {
            "food": self.food,
            "fun": self.fun,
            "hygiene": self.hygiene,
            "health": self.health
        }
class PetGameApp:       #класс GUI-приложение для взаимодействия
    def __init__(self, root):   # инициализирует приложение и все его компоненты
        self.root = root
        self.pet = Pet()
        self.root.title("Тамагочи: Стеша")
        self.root.resizable(False, False)
        #сообщение перед запуском
        messagebox.showinfo("Приветствие", "Привет! Ухаживай за моей кошкой Стешей и следи, чтобы ее показатели не доходили до нуля.")
        self.canvas = tk.Canvas(self.root, width=600, height=400)
        self.canvas.pack()
        self.load_pet_images()
        self.current_image_index = 0
        self.pet_image_item = self.canvas.create_image(300, 200, image=self.pet_images[self.current_image_index])
        self.create_status_bar()
        self.create_main_buttons()
        self.update_status()
        self.animate_pet_images()
        #загружаем изображения
    def load_pet_images(self):
        self.pet_images = []
        image_paths = []
        for i in range(1, 7): # Список путей к изображениям, нужно поменять
            image_path = f"/Users/leralipnickaa/Desktop/стеша/{i}.png"
            image_paths.append(image_path)
        # загрузка и изменение размера изображений
        for path in image_paths:
            try:
                image = Image.open(path)
                image = image.resize((400, 400), Image.LANCZOS)
                image = ImageTk.PhotoImage(image)
                self.pet_images.append(image)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось загрузить изображение {path}: {e}")
    # анимирует изображения питомца, создавая эффект слайдшоу
    def animate_pet_images(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.pet_images)
        self.canvas.itemconfig(self.pet_image_item, image=self.pet_images[self.current_image_index])
        self.root.after(1000, self.animate_pet_images)
        #панель статусов
    def create_status_bar(self):
        self.status_frame = tk.Frame(self.root, bg="lightblue")
        self.status_frame.pack(fill=tk.X)
        self.food_label = tk.Label(self.status_frame, text="", bg="lightblue", font=("Arial", 12))
        self.food_label.pack(side="left", padx=10)
        self.fun_label = tk.Label(self.status_frame, text="", bg="lightblue", font=("Arial", 12))
        self.fun_label.pack(side="left", padx=10)
        self.hygiene_label = tk.Label(self.status_frame, text="", bg="lightblue", font=("Arial", 12))
        self.hygiene_label.pack(side="left", padx=10)
        self.health_label = tk.Label(self.status_frame, text="", bg="lightblue", font=("Arial", 12))
        self.health_label.pack(side="left", padx=10)
    #создает основные кнопки управления приложением
    def create_main_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)
        self.feed_button = tk.Button(self.button_frame, text="Кормить питомца", command=self.show_feed_options)
        self.feed_button.pack(side="left", padx=10)
        self.play_button = tk.Button(self.button_frame, text="Играть с питомцем", command=self.show_play_options)
        self.play_button.pack(side="left", padx=10)
        self.hygiene_button = tk.Button(self.button_frame, text="Ухаживать за питомцем", command=self.show_hygiene_options)
        self.hygiene_button.pack(side="left", padx=10)
        self.heal_button = tk.Button(self.button_frame, text="Лечить питомца", command=self.show_heal_options)
        self.heal_button.pack(side="left", padx=10)
        self.quit_button = tk.Button(self.button_frame, text="Выйти", command=self.quit_game)
        self.quit_button.pack(side="left", padx=10)
    # обновляет отображение статусов питомца
    def update_status(self):
        self.pet.update_status()
        status = self.pet.get_status()
        self.food_label.config(text=f"Еда: {status['food']}/10")
        self.fun_label.config(text=f"Досуг: {status['fun']}/10")
        self.hygiene_label.config(text=f"Гигиена: {status['hygiene']}/10")
        self.health_label.config(text=f"Здоровье: {status['health']}/10")
        if any(value <= 0 for value in status.values()):
            messagebox.showinfo("Игра окончена", "Ваш питомец нуждается в уходе!")
            self.quit_game()
        else:
            self.root.after(1000, self.update_status)
    #универсальный метод для отображения вариантов действий
    def show_feed_options(self):
        options = [("Корм", "1"), ("Лакомство", "2"), ("Вода", "3")]
        self.show_options("Кормление", options, self.pet.feed)
    def show_play_options(self):
        options = [("Грызть вещи", "1"), ("Лазер", "2"), ("Погладить", "3")]
        self.show_options("Игры", options, self.pet.play)
    def show_hygiene_options(self):
        options = [("Вычесать", "1"), ("Душ", "2")]
        self.show_options("Гигиена", options, self.pet.hygiene_up)
    def show_heal_options(self):
        options = [("Таблетка", "1"), ("Чудо микстура", "2")]
        self.show_options("Лечение", options, self.pet.heal)
    def show_options(self, title, options, action):
        self.disable_main_buttons()
        self.option_window = tk.Toplevel(self.root)
        self.option_window.title(title)
        self.option_window.resizable(False, False)
        for text, value in options:
            btn = tk.Button(self.option_window, text=text, width=20, command=lambda v=value: self.select_option(v, action))
            btn.pack(pady=5)
        self.option_window.protocol("WM_DELETE_WINDOW", self.on_option_window_close)
    #Обрабатывает выбор
    def select_option(self, choice, action):
        action(choice)
        self.option_window.destroy()
        self.enable_main_buttons()
    # обрабатывает закрытие окна
    def on_option_window_close(self):
        self.option_window.destroy()
        self.enable_main_buttons()
    #отключает основные кнопки
    def disable_main_buttons(self):
        for btn in self.button_frame.winfo_children():
            btn.config(state=tk.DISABLED)
    #включает основные кнопки
    def enable_main_buttons(self):
        for btn in self.button_frame.winfo_children():
            btn.config(state=tk.NORMAL)
    # завершает работу приложения
    def quit_game(self):
        self.root.quit()
def main():
    root = tk.Tk()
    app = PetGameApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()
