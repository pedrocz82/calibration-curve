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

    @property
    def r_squared(self):
        correlation_matrix = np.corrcoef(self.absorbance, self.concentration)
        correlation_xy = correlation_matrix[0, 1]
        return correlation_xy ** 2

    def __call__(self, x):
        return self.a * x + self.b

    def __str__(self):
        return f'calibration_curve -> {self.a:.4f}*x + {self.b:.4f} (r²={self.r_squared:.4f}) '

    def plot(self):
        absorbance = np.array(self.absorbance)
        concentration_lab = np.array(self.concentration)
        concentration_curve = self(absorbance)

        plt.plot(absorbance, concentration_curve, label=f'{str(self)}')
        plt.plot(absorbance, concentration_lab, 'ro', label='lab data')
        plt.xlabel('absorbance (mg/L)')
        plt.ylabel('concentration')
        plt.title('concentration x absorbance (mg/L)')
        plt.legend()
        plt.show()


c1 = CalibrationCurve([0.1516, 0.3826, 0.4281, 0.6545, 0.7118, 0.9565], [0.20, 0.40, 0.60, 0.80, 1.00, 1.2])
c1.plot()
