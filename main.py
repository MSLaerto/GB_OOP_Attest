from calculator import Calculator, CalculatorView

import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    view = CalculatorView()
    view.run()            