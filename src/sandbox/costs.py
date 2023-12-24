# Handle conditional imports
def configure_imports(cuda):
    global np
    np = __import__('cupy' if cuda else 'numpy')

'''
Every cost class includes three methods:
    - forward: Compute cost
    - backward: Compute derivative of cost
'''

# Binary Cross Entropy - Binary classification
class BinaryCrossentropy:

    # (-1 / m * sum(Yln(A) + (1 - Y)ln(1 - A)))
    def forward(self, AL, Y):
        return np.squeeze(-1 / Y.shape[1] * np.sum(np.dot(Y, np.log(AL).T) + np.dot(1 - Y, np.log(1 - AL).T)))
    
    # (-Y/A + (1 - Y)/(1 - A))
    def backward(self, AL, Y):
        return -(np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))

# Categorical Cross Entropy - Multiclass classification
# TODO: Implement
class CategoricalCrossentropy:

    # TBA 
    def forward(self, AL, Y):
        pass

    # TBA
    def backward(self, AL, Y):
        pass

# Mean Squared Error - Regression
class MSE:

    # (1 / m * sum((Y - A)^2))
    def forward(self, AL, Y):
        return np.squeeze(1 / Y.shape[1] * np.sum(np.square((Y - AL))))
    
    # (-2 / m * (Y - A))
    def backward(self, AL, Y):
        return -2 * (Y - AL)

# Mean Absolute Error - Regression
class MAE:

    # (1 / m * sum(|Y - A|))
    def forward(self, AL, Y):
        return np.squeeze(1 / Y.shape[1] * np.sum(np.abs(Y - AL)))
    
    # -1 if AL < Y, 1 if AL > Y, 0 otherwise
    def backward(self, AL, Y):
        return np.where(AL < Y, -1, np.where(AL > Y, 1, 0))
