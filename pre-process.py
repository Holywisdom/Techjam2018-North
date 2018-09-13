import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import Dataset

advertisement_log_dataset = pd.read_csv('ad_log.csv')
credit_card_transaction_dataset = pd.read_csv('cc_txn.csv')
debit_card_dataset = pd.read_csv('dc_txn.csv')
customer_demographic_dataset = pd.read_csv('demo.csv')
action_history_dataset = pd.read_csv('events.csv')
purchase_history_dataset = pd.read_csv('purchase.csv')
saving_balance_dataset = pd.read_csv('sa_bal.csv')
customer_index_dataset = pd.read_csv('y_index.csv')
training_dataset = pd.read_csv('y_train.csv')


# Dataset Structure


# Rename columns