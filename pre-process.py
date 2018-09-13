import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import Dataset

Advertisement_log_dataset = pd.read_csv('ad_log.csv')
Credit_card_transaction_dataset = pd.read_csv('cc_txn.csv')
Debit_card_dataset = pd.read_csv('dc_txn.csv')
Customer_demographic_dataset = pd.read_csv('demo.csv')
Action_history_dataset = pd.read_csv('events.csv')
Purchase_history_dataset = pd.read_csv('purchase.csv')
Saving_balance_dataset = pd.read_csv('sa_bal.csv')
y_index_dataset = pd.read_csv('y_index.csv')
customer_index_dataset = pd.read_csv('y_train.csv')


# Rename columns