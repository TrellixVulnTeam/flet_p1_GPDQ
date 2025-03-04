import flet
from flet import TextField, FloatingActionButton, Column, Row, UserControl, Checkbox, IconButton, icons, Page, colors

class Task(UserControl):
  def __init__(self, task_name, task_delete):
    self.task_name = task_name
    self.task_delete = task_delete
    super().__init__()
    

  def build(self):
    self.display_task = Checkbox(value=False, label=self.task_name)
    self.edit_task = TextField(expand=1)

    self.display_view = Row(
      visible=True,
      alignment='spaceBetween',
      vertical_alignment='center',
      controls=[
        self.display_task,
        Row(
          spacing=0,
          controls=[
            IconButton(
              icon=icons.CREATE_OUTLINED,
              tooltip='Edit To-Do',
              on_click=self.edit_clicked,
        ),
            IconButton(
              icon=icons.DELETE_OUTLINE,
              tooltip='Delete To_do',
              on_click=self.delete_clicked,
            ),
          ],
        ),
        
      ],
    )

    self.edit_view = Row(
      visible=False,
      alignment='spaceBetween',
      vertical_alignment='center',
      controls=[
        self.edit_task,
        IconButton(
          icon=icons.DONE_OUTLINE_OUTLINED,
          icon_color=colors.GREEN,
          tooltip='Update To-Do',
          on_click=self.save_clicked,
        ),
      ],
    )
    return Column(
      controls=[self.display_view, self.edit_view]
    )

  def edit_clicked(self, e):
    self.edit_task.value = self.display_task.label
    self.display_view.visible = False
    self.edit_view.visible = True
    self.update()

  def save_clicked(self, e):
    self.display_task.label = self.edit_task.value
    self.display_view.visible = True
    self.edit_view.visible = False
    self.update()

  def delete_clicked(self, e):
    self.task_delete(self)

class ToDoApp(UserControl):
  def build(self):
    self.new_task = TextField(hint_text='Whats needs to be done', expand=True)
    self.tasks = Column()

    return Column(
      width=600,
      controls=[
        Row(
          controls=[
            self.new_task,
            FloatingActionButton(icon=icons.ADD, on_click=self.add_clicked),
          ],
        ),
        self.tasks,
      ],
    )
  def add_clicked(self, e):
    task = Task(self.new_task.value, self.task_delete)
    self.tasks.controls.append(task)
    self.new_task.value = ''
    self.update()

  def task_delete(self, task):
    self.tasks.controls.remove(task)
    self.update()

def main(page: Page):
  page.title = 'ToDo App'
  page.horizontal_alignment = 'center'
  
  app1 = ToDoApp()
  page.add(app1)
  page.update()
flet.app(target=main)