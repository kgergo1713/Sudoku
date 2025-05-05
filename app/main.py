from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from sudoku_logic import SudokuGame
from kivy.uix.boxlayout import BoxLayout

class SudokuCell(BoxLayout):
    """Egy cella widget – később ide kötjük az érintés-kezelést."""

class SudokuApp(App):
    def build(self):
        return Builder.load_file("app/kv/sudoku.kv")

    def on_start(self):
        # game init and load to grid
        self.game = SudokuGame()
        grid = self.root
        for i, row in enumerate(self.game.board):
            for j, val in enumerate(row):
                cell = grid.children[::-1][i*9+j]
                if val != 0:
                    cell.ids.label.text = str(val)

if __name__ == "__main__":
    SudokuApp().run()
