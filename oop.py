from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt
import numpy as np


class ErrorCalculator:

    def __init__(self, resid, stand_res, mse, rmse, y, y_pred):
        self.resid = resid
        self.stand_res = stand_res
        self.mse = mse
        self.rmse = rmse
        self.y_pred = np.array(y_pred)
        self.y = np.array(y)

    def get_residuals(self):
        self.resid = self.y - self.y_pred
        return self.resid

    def get_standardised_residuals(self):
        self.stand_res = (self.y - self.y_pred) / (self.y_pred)**0.5
        return self.stand_res

    def get_mse(self):
        self.mse = mse(self.y, self.y_pred)
        return self.mse

    def get_rmse(self):
        self.rmse = mse(self.y, self.y_pred, squared=False)
        return self.rmse

    def error_summary(self):
        stand_resid_min = min(self.stand_res)
        stand_resid_max = max(self.stand_res)
        rmse_min = min(self.rmse)
        rmse_max = max(self.rmse)
        mse_min = min(self.mse)
        mse_max = max(self.mse)
        print(f'standard residual: {stand_resid_min}')
        print(f'standard residual: {stand_resid_max}')
        print(f'min rmse: {rmse_min}')
        print(f'max rmse: {rmse_max}')
        print(f'min mse: {mse_min}')
        print(f'max mse: {mse_max}')


class Plotter(ErrorCalculator):

    def plot(self):
        plt.hist(self.resid)
        plt.title('Distribution of residuals')
        plt.xlabel('Residuals')
        plt.ylabel('Distribution')
        plt.show()
        return plt.show()


class HistogramPlotter(Plotter):

    Plotter.plot()
    super()


class ScatterPlotter(Plotter):
    def scatter(self):
        plt.scatter(self.y_pred, self.resid)
        plt.xlabel('Observed values')
        plt.ylabel('predicted values')
        plt.title('Observed values vs predicted values')
    super()