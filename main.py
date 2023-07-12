from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainApp(App):

    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        main_layout = BoxLayout( orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="left", font_size=55
        )
        main_layout.add_widget(self.solution)

        buttons = [

            ["7", "8", "9", "/"],

            ["4", "5", "6", "*"],

            ["1", "2", "3", "-"],

            [".", "0", "C", "+"],

        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text= label,
                    pos_hint={"center_x": .5, "center_y": .5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(text="=", 
        pos_hint={'center_x':0.5, 'center_y':0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        equals_button.background_color = [1,0,1,1]

        main_layout.add_widget(equals_button)

        return main_layout
    
    def on_button_press(self, instance):
        
        current = instance.text
      
        if current == 'C':
            self.solution.text = ''
        else: 
            # clear the display and show the value of the key pressed if the last operator pressed is '='
            if self.last_was_operator == "=":
                self.solution.text = ""
                self.solution.text += instance.text
                # set last operatorto disable this feature
                self.last_was_operator = None
            # get the value of the button pressed, and a list of the values on the display 
            # insert values of button pressed into the list at the position of the cursur
            elif self.last_was_operator == None:
                button_value = instance.text 
                display = list(self.solution.text)
                display.insert(self.solution.cursor_col, button_value)
                self.solution.text = "".join(display)
                print()

    def on_solution(self, instance):

        expr = self.solution.text
        if expr:
            #catch and handle any mathematical error
            try:
                self.solution.text = str(eval(expr))
            except SyntaxError:
                self.solution.text = "invalid expression"
        #  get a reference of the equals sign if it was pressed
        self.last_was_operator = "="

if __name__ == "__main__":
    app = MainApp()
    app.run()