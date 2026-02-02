from hamilton.function_modifiers import extract_columns, parameterize_values
from hamilton.function_modifiers import parameterize_extract_columns, ParameterizedExtract, source, value
import pandas as pd

def raw_dataset() -> pd.DataFrame:
  index = pd.date_range('20230101', '20230110')
  return pd.DataFrame(
      index=index,
      data={  
        "signups": [1, 10, 50, 100, 200, 400, 700, 800, 1000, 1300],
        "spend": [10, 10, 20, 40, 40, 50, 100, 80, 90, 120],
      })

def acquisition_cost_rolling_mean_7(raw_dataset: pd.DataFrame) -> pd.Series:
  """Rolling 7 day average spend."""
  return raw_dataset.spend.rolling(window=7, min_periods=1).mean()


@extract_columns(*["spend", "signups"])
def raw_dataset_cols() -> pd.DataFrame:
  index = pd.date_range('20230101', '20230109')
  return pd.DataFrame(
      index=index,
      data={  
        "signups": [1, 10, 50, 100, 200, 400, 700, 800, 1000],
        "spend": [10, 10, 20, 40, 40, 50, 100, 80, 90],
      })

def acquisition_cost_rolling_mean_cols(spend: pd.Series) -> pd.Series:
  """Rolling 7 day average spend."""
  return spend.rolling(window=7, min_periods=1).mean()

def stats() -> int:
  return 22


@parameterize_values(
    parameter="myparam",
    assigned_output={
      ("sales_table", "parameter1 sales amt"): "sales_amt",
      ("returns_table", "parameter2 returns amt"): "returns_amt"
    }
)
def parameter_func(myparam: str) -> str:
  return f"pre_{myparam}_tbl"


def concat_sales_returns(sales_table: str, returns_table: str) -> str:
  return f"{sales_table}_{returns_table}"

def inseries1a() -> pd.Series:
  return pd.Series([2])

def inseries2a() -> pd.Series:
  return pd.Series([3])

@parameterize_extract_columns(
    ParameterizedExtract(
        ("outseries1a", "outseries2a"),
        {"input1": source("inseries1a"), "input2": source("inseries1b"), "input3": value(10)},
    ),
    ParameterizedExtract(
        ("outseries1b", "outseries2b"),
        {"input1": source("inseries2a"), "input2": source("inseries2b"), "input3": value(100)},
    ),
)
def fn(input1: pd.Series, input2: pd.Series, input3: float) -> pd.DataFrame:
    return pd.concat([input1 * input2 * input3, input1 + input2 + input3], axis=1)