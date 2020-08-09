import numpy as np
import matplotlib.pyplot as plt


class CalibrationCurve:
    def __init__(self, absorbance, concentration):
        self._absorbance = absorbance
        self._concentration = concentration
        self._coefficients = np.polyfit(self.absorbance, self.concentration, 1)

    @property
    def absorbance(self):
        return self._absorbance

    @property
    def concentration(self):
        return self._concentration

    @property
    def coefficients(self):
        return self._coefficients

    @property
    def a(self):
        return self._coefficients[0]

    @property
    def b(self):
        return self._coefficients[1]

    def __call__(self, x):
        return self.a * x + self.b

    def plot(self):
        absorbance = np.array(self.absorbance)
        concentration_lab = np.array(self.concentration)
        concentration_curve = self(absorbance)

        plt.plot(absorbance, concentration_curve)
        plt.plot(absorbance, concentration_lab, 'ro')
        plt.show()


c1 = CalibrationCurve([1.3, 2.1, 3.30, 4.15, 5.2], [3.1, 6.1, 9.1, 12.1, 15.1])
c1.plot()
