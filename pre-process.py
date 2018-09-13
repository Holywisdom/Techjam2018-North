import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import Dataset

advertisement_log_dataset = pd.read_csv('ad_log.csv')
credit_card_transaction_dataset = pd.read_csv('cc_txn.csv')
debit_card_transaction_dataset = pd.read_csv('dc_txn.csv')
customer_demographic_dataset = pd.read_csv('demo.csv')
action_history_dataset = pd.read_csv('events.csv')
purchase_history_dataset = pd.read_csv('purchase.csv')
saving_balance_dataset = pd.read_csv('sa_bal.csv')
customer_index_dataset = pd.read_csv('y_index.csv')
training_dataset = pd.read_csv('y_train.csv')


# Dataset Structure

'''
    training_dataset
        user_id
        label
        
    customer_index_dataset
        user_id
        
    credit_card_transaction_dataset (dup-1)
        user_id
        category 
        dt (dup-2)
        txn_amt
        
    debit_card_dataset (dup-1)
        user_id
        category 
        dt (dup-2)
        txn_amt
        
    customer_demographic_dataset
        user_id
        account_start_date
        birth_year
        gender
        marital_status
        individual_income_segment_code
        family_income_segment_code
        
    purchase_history_dataset
        user_id
        dt (dup-2)
        product
    
    action_history_dataset
        user_id
        dt (dup-2)
        screen
        login_cnt
    
    advertisement_log_dataset
        user_id
        dt (dup-2)
    
    saving_balance_dataset
        user_id
        month
        balance
'''

# Rename columns

credit_card_transaction_dataset.rename(index=str, columns={"category": "credit_card_category", "dt": "credit_card_dt", "txn_amt": "credit_card_txn_amt"}, inplace=True)
debit_card_transaction_dataset.rename(index=str, columns={"category": "debit_card__category", "dt": "debit_card__dt", "txn_amt": "debit_card__txn_amt"}, inplace=True)
purchase_history_dataset.rename(index=str, columns={"dt": "purchase_history__dt"}, inplace=True)
action_history_dataset.rename(index=str, columns={"dt": "action_history__dt"}, inplace=True)
advertisement_log_dataset.rename(index=str, columns={"dt": "advertisement_log__dt"}, inplace=True)

# Merchant category code

def labelEncoder(Dataframe,CatType,Prefix,ColName) :
    Dataframe[Prefix+CatType] = np.where(Dataframe[ColName]==CatType,1,0)

for i in range(1, 16):
    labelEncoder(credit_card_transaction_dataset,'cat'+str(i),'cc_','credit_card_category')
    labelEncoder(debit_card_transaction_dataset,'cat'+str(i),'dc_','debit_card__category')

credit_card_transaction_dataset.drop(columns=['credit_card_category'], inplace=True)
debit_card_transaction_dataset.drop(columns=['debit_card__category'], inplace=True)