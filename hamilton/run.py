from hamilton import driver, base
from hamilton_sdk import adapters
import data_loading
#import simple_pipeline


#tracker = adapters.HamiltonTracker(
   #project_id=1,  # modify this as needed
   #username="admin",
   #dag_name="v3",
   #tags={"environment": "DEV", "team": "MY_TEAM", "version": "X"},
#)

dr = (
  driver.Builder()
    .with_modules(data_loading)
    .with_adapters(base.PandasDataFrameResult())
    .build()
)
result = dr.execute(
  [
    #"acquisition_cost_rolling_mean_7",
    #"acquisition_cost_rolling_mean_cols",
    #"stats",
    #"concat_sales_returns",
    "outseries1a"
    #"predicted_digits"
  ],
  #inputs={"input_digits": load_some_digits().sample(5)}
)
print(result.to_string())

# Display the whole grap
gr = dr.display_all_functions(
  "all_graph.dot", # create image if running locally
  show_legend=True,
  orient="LR",
  deduplicate_inputs=True,
)

dr.display_all_functions("graph.png")

# Display only what will be executed.
dr.visualize_execution(
    final_vars=["acquisition_cost_rolling_mean_7", "acquisition_cost_rolling_mean_cols"],
    output_file_path="graph.dot",
)

#in terminal run:
#dot -Tpng graph.dot -o graph.png

#gr.render()
#gr.render(filename='my_dag', format='png', cleanup=True)