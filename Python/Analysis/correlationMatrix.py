import mysql.connector
from mysql.connector import Error
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a server connection function
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

# Create query execution function
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

# Create SQL query reading function
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# Attempt server connection
connection = create_db_connection('localhost', 'marcrng', 'Kaisersql0413$', 'er_database')

# Create dataframe from melee_data
from_db = []

melee_data_selectall = """
SELECT atkPhysical, crit, strReq, strScaling, weight
FROM melee_data;
"""

results = read_query(connection, melee_data_selectall)

for result in results:
  result = list(result)
  from_db.append(result)

columns = ['atkPhysical', 'crit', 'strReq', 'strScaling', 'weight']
melee_df = pd.DataFrame(from_db, columns=columns)

# Create a correlation matrix with Pandas
melee_matrix = melee_df.corr()

# Create visualization for correlation matrix with Seaborn

# Apply custom color palette to matrix
palette = sns.diverging_palette(20, 220, n=256)

sns.heatmap(melee_matrix, annot=True, cmap = palette)
plt.show()
