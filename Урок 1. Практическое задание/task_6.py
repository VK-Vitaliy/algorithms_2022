"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskBoard:
    def __init__(self):
        self.current_tasks = []
        self.solved_tasks = []
        self.revision = []

    def __str__(self):
        if not self.current_tasks:
            if not self.revision:
                return f'Все задания выполнены.\nСписок решенных задач: {self.solved_tasks}'
            return f'Список решенных задач: {self.solved_tasks}\nСписок задач отправленных на доработку: {self.revision}'
        else:
            return f'Базовый список задач: {self.current_tasks}.\nСписок задач отправленных на доработку: {self.revision}'

    def is_empty(self):
        return self.current_tasks == []

    def add_task(self, task):
        self.current_tasks.insert(0, task)
        print(f"Задача \"{task}\" добавлена в базовый список задач.")

    def del_task(self):
        if self.current_tasks:
            task = self.current_tasks.pop()
            print(f'Задание "{task}" выполнено.')
            self.solved_tasks.append(task)
        else:
            print('Список заданий пуст')

    def return_to_revision(self):
        if self.current_tasks:
            task = self.current_tasks.pop()
            print(f'Задание "{task}" отправлено на доработку.')
            self.revision.append(task)
        else:
            print('Список заданий пуст')


if __name__ == '__main__':
    to_do_list = TaskBoard()
    to_do_list.add_task('Позвонить клиенту')
    to_do_list.add_task('Назначить встречу')
    to_do_list.add_task('выставить счет')
    print(to_do_list)
    to_do_list.del_task()
    to_do_list.del_task()
    to_do_list.return_to_revision()
    print(to_do_list)
    to_do_list.add_task('прочитать книгу')
    print(to_do_list)


