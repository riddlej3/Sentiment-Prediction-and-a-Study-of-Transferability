"""
Plotting module for main plots in notebook
"""

import matplotlib.pyplot as plt


class model_plots:
    """ 
    class used to create graphs for testing models
    """

    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 2, figsize=(20, 6))

    def model_to_actual_plot(self, df, series1, series2, label1, label2, title=None):
        """
        Overview: Graph that plots the distribution of predictions against the distribution of actuals
        Input: Input: pred series and actuals needing comparing. Label 1 and label 2 are axis labels for x and y.
        In this particular example errors = 'Score' and 'Error Count or Total Count'
        """

        self.ax[0].bar(
            series1.value_counts().index, series1.value_counts().values, label=label1
        )
        self.ax[0].bar(
            series2.value_counts().index,
            series2.value_counts().values,
            label=label2,
            width=0.5,
            alpha=0.5,
            color="red",
        )
        self.ax[0].legend()
        self.ax[0].set_title(title)
        self.ax[0].set_xlabel("Score")
        self.ax[0].set_ylabel("Total Count")

    def error_plot(
        self, df, series1, series2, label1, label2, title="Distribution of Score Error"
    ):
        """
        Overview: Shows the error distribution of the results against actuals
        Input: pred series and actuals needing comparing.
        """
        graph = (series1.sub(series2)).value_counts().sort_index()
        self.ax[1].bar(graph.index, graph.values)
        self.ax[1].set_xlabel('Error Score')
        self.ax[1].set_ylabel('Error Count')
        self.ax[1].set_title("Distribution of Score Error")
        self.ax[1].set_ylim(0, graph.values.max() * 1.2)
        self.ax[1].set_yticks([])
        for i, v in enumerate(graph):
            self.ax[1].text(
                i - 4, v + (graph.max() / 13), f"{v}", horizontalalignment="center"
            )
        for i, v in enumerate(graph):
            self.ax[1].text(
                i - 4,
                v + (graph.max() / 50),
                "{:.2f}".format(v / graph.sum()),
                horizontalalignment="center",
            )

