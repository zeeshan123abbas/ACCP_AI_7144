-- Session 15: Linear regression with SQL Server Machine Learning Services (Python)
EXEC sp_configure 'external scripts enabled', 1; RECONFIGURE;
GO
USE CampusDB;
GO
DROP TABLE IF EXISTS dbo.MonthlySales;
CREATE TABLE dbo.MonthlySales (MonthNo INT, Sales FLOAT);
INSERT INTO dbo.MonthlySales VALUES (1,120),(2,135),(3,150),(4,149),(5,170),(6,182),(7,195),(8,210);
GO
EXEC sp_execute_external_script
  @language = N'Python',
  @script = N'
from sklearn.linear_model import LinearRegression
import pandas as pd
model = LinearRegression().fit(InputDataSet[["MonthNo"]], InputDataSet["Sales"])
future = pd.DataFrame({"MonthNo": [9, 10, 11, 12]})
future["PredictedSales"] = model.predict(future[["MonthNo"]]).round(1)
OutputDataSet = future',
  @input_data_1 = N'SELECT MonthNo, Sales FROM dbo.MonthlySales'
WITH RESULT SETS ((MonthNo INT, PredictedSales FLOAT));
GO
