#Task 1 A Person class

# Make a class called Person. Make the __init__() method take firstname, lastname, 
# and age as parameters and add them as attributes. 
# Make another method called talk() which makes prints a greeting from the person containing, 
# for example like this: "Hello, my name is Carl Johnson and I’m 26 years old".

class Person:
    def __init__(self, firstname, lastname,age ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
      
    def called_talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')
        
person1 = Person('Bill', 'Klinton', 79)
person1.called_talk()

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# Task 2 Doggy age
# Create a class Dog with class attribute 'age_factor' equals to 7. 
# Make __init__() which takes values for a dog’s age.
# Then create a method `human_age` which returns the dog’s age in human equivalent.

class Dog:
    age_factor = 7

    def __init__(self, dogs_name, dogs_age):
        self.dogs_name = dogs_name
        self.dogs_age = dogs_age

    def human_age_equivalent(self):
        return self.dogs_age * self.age_factor
      
    
dog1 = Dog('Tuzik', 5)
print(dog1.human_age_equivalent())

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 3  TV controller
# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# exists(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case

# The default channel turned on before all commands is №1.

# Your task is to create the TVController class and methods described above.


"""
Клас TVController для керування телевізором
Реалізує базові функції перемикання каналів та перевірки їх наявності
"""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    """
    Контролер для керування телевізором зі списком каналів
    """
    
    def __init__(self, channels):
        """
        Ініціалізація контролера зі списком каналів
        
        Args:
            channels (list): Список назв телеканалів
        """
        self.channels = channels
        self.current_channel_index = 0  # Поточний канал (індекс у списку, починається з 0)
        self.total_channels = len(channels)  # Загальна кількість каналів

    def first_channel(self):
        """Перемикає на перший канал у списку"""
        self.current_channel_index = 0
        return self._get_current_channel_name()

    def last_channel(self):
        """Перемикає на останній канал у списку"""
        self.current_channel_index = self.total_channels - 1
        return self._get_current_channel_name()

    def turn_channel(self, channel_number):
        """
        Перемикає на конкретний канал за номером
        
        Args:
            channel_number (int): Номер каналу (починається з 1)
            
        Returns:
            str: Назва каналу або "No" якщо канал не існує
        """
        if self._is_valid_channel_number(channel_number):
            self.current_channel_index = channel_number - 1
            return self._get_current_channel_name()
        return "No"

    def next_channel(self):
        """Перемикає на наступний канал (з циклічним переходом)"""
        self.current_channel_index = (self.current_channel_index + 1) % self.total_channels
        return self._get_current_channel_name()

    def previous_channel(self):
        """Перемикає на попередній канал (з циклічним переходом)"""
        self.current_channel_index = (self.current_channel_index - 1) % self.total_channels
        return self._get_current_channel_name()

    def current_channel(self):
        """Повертає назву поточного каналу"""
        return self._get_current_channel_name()

    def exists(self, channel):
        """
        Перевіряє, чи існує канал
        
        Args:
            channel (int/str): Номер каналу або назва каналу
            
        Returns:
            str: "Yes" якщо канал існує, "No" якщо не існує
        """
        if isinstance(channel, int):
            return "Yes" if self._is_valid_channel_number(channel) else "No"
        elif isinstance(channel, str):
            return "Yes" if channel in self.channels else "No"
        return "No"

    # Допоміжні (приватні) методи
    def _get_current_channel_name(self):
        """Повертає назву поточного каналу"""
        return self.channels[self.current_channel_index]

    def _is_valid_channel_number(self, channel_number):
        """
        Перевіряє, чи є номер каналу коректним
        
        Args:
            channel_number (int): Номер каналу для перевірки
            
        Returns:
            bool: True якщо номер коректний, False якщо ні
        """
        return 1 <= channel_number <= self.total_channels


# Приклад використання
if __name__ == "__main__":
    # Створюємо контролер телевізора
    controller = TVController(CHANNELS)
    
    print("📺 TV Controller Demo")
    print("Доступні канали:", CHANNELS)
    print()
    
    # Демонстрація роботи методів
    print("1. Перший канал:", controller.first_channel())
    print("2. Останній канал:", controller.last_channel())
    print("3. Перемикаємо на канал 1:", controller.turn_channel(1))
    print("4. Наступний канал:", controller.next_channel())
    print("5. Попередній канал:", controller.previous_channel())
    print("6. Поточний канал:", controller.current_channel())
    print("7. Чи існує канал 4?", controller.exists(4))
    print("8. Чи існує канал 'BBC'?", controller.exists("BBC"))


# ---------------------------------------------------------------------------------------------------------------------------




