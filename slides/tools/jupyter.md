# <logos-jupyter /> Jupyter Notebooks

* Jupyter notebooks can illustrate the exploration and analysis process step by step and allows
  easy switching between
  - explanatory text in <mdi-markdown /> Markdown format
  - equations $\Theta = (X^TX)^{-1} \cdot (X^Ty)$
  - code
    ```py
    def normal_equation(X, y):
        return np.linalg.inv(X.T @ X) @ X.T @ y
        #             3x3           @ 3x47 @ 47 x 1
    ```
  - graphs / visualization
    <img alt="graph" src="/images/tita-graph.png" style="width: 250px; height: 170px" />
