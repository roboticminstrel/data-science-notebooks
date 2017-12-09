from sklearn.base import BaseEstimator, RegressorMixin
import pandas as pd


class Base_Predictor(BaseEstimator, RegressorMixin):

    def __init__(self, DAMPENING_TERM=25, dampening=False):
        self._dampening_term = 25
        self._dampening = dampening

    def fit(self, X, y):
        self._mean = y.mean()
        self._R = pd.concat([X, y], axis=1).pivot_table(
                        index='UserID', columns='gameID', values='rating')
        self._bu = self._R.apply(lambda row: self._user_base(row), axis=1)
        self._bi = self._R.apply(lambda column: self._item_base(column))

    def _user_base(self, row):
        """(1/M+d)*bu is with the dampening factor. Without it's 1/M * bu.
        To find the way to add the dampening factor as a scalar multiplication:
            k*1/M(bu) = 1/M+d(bu)
            k = M/M+d"""
        bu = row.mean() - self._mean
        if self._dampening:
            num_items_user_reviewed = row[row.notnull()].size
            damp_factor = num_items_user_reviewed/(num_items_user_reviewed+self._dampening_term)
            bu *= damp_factor
        return bu

    def _item_base(self, column):
        users_that_reviewed_this_item = column[column.notnull()]
        bu_for_users_that_reviewed_i = self._bu[users_that_reviewed_this_item.index].mean()
        bi = users_that_reviewed_this_item.mean()-bu_for_users_that_reviewed_i-self._mean
        if self._dampening:
            num_users_reviewed_item = column[column.notnull()].size
            damp_factor = num_users_reviewed_item/(num_users_reviewed_item+self._dampening_term)
            bi *= damp_factor
        return bi

    def predict(self, X):
        bu = self._bu[X.UserID].values
        bi = self._bi[X.gameID].values
        return self._mean + bu + bi
