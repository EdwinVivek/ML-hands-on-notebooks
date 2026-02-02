from hamilton import driver, base
from hamilton_sdk import adapters
import simple_pipeline

dr = (
  driver.Builder()
    .with_modules(simple_pipeline)
    .with_adapters(base.PandasDataFrameResult())
    .build()
)

# Display the whole grap
gr = dr.display_all_functions(
  "digits_pipeline.dot", # create image if running locally
  show_legend=True,
  orient="LR",
  deduplicate_inputs=True,
)

