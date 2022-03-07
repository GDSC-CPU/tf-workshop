---
layout: center
---

# Predicting House Prices: A great idea 💡

1. start with random values for $w_0$ and $w_1$
2. determine how wrong the guessed $w_0$ and $w_1$ are
   - predict the house price $\hat{y}$ with the equation containing guessed $w_0$ and $w_1$
   - $\hat{y} = w_1x_1 + w_0$, where $x_1$ is the house size
   - compare how far is the predicted value $\hat{y}$ with the **actual** house price $y$
   - keep doing this for all data in the training set `#1`, `#2`, `#3`, `#4`, etc...
     + $\hat{y}^{(1)} = w_1x_1^{(1)} + w_0$, then compare how far is $\hat{y}^{(1)}$ to $y^{(1)}$
     + $\hat{y}^{(2)} = w_1x_1^{(2)} + w_0$, then compare how far is $\hat{y}^{(2)}$ to $y^{(2)}$
     + $\hat{y}^{(3)} = w_1x_1^{(3)} + w_0$, then compare how far is $\hat{y}^{(3)}$ to $y^{(3)}$
     + $\hat{y}^{(4)} = w_1x_1^{(4)} + w_0$, then compare how far is $\hat{y}^{(4)}$ to $y^{(4)}$
   - average those error values
3. make another guess, repeat Step 2
   - 🙏 hopefully with some ~~magic 🌈✨~~ **math** the new $w_0$ and $w_1$ become better guesses
