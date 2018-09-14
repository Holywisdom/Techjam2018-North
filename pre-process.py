import numpy as np
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

# def labelEncoder(Dataframe,CatType,Prefix,ColName) :
#     Dataframe[Prefix+CatType] = np.where(Dataframe[ColName]==CatType,1,0)

# for i in range(1, 16):
#     labelEncoder(credit_card_transaction_dataset,'cat'+str(i),'cc_','credit_card_category')
#     labelEncoder(debit_card_transaction_dataset,'cat'+str(i),'dc_','debit_card__category')

# credit_card_transaction_dataset.drop(columns=['credit_card_category'], inplace=True)
# debit_card_transaction_dataset.drop(columns=['debit_card__category'], inplace=True)


#cleaning

customer_demographic_dataset['marital_status'] = pd.to_numeric(customer_demographic_dataset.marital_status, errors='coerce').fillna(0).astype(int)
customer_demographic_dataset['individual_income_segment_code'] = pd.to_numeric(customer_demographic_dataset.marital_status, errors='coerce').fillna(0).astype(int)
customer_demographic_dataset['family_income_segment_code'] = pd.to_numeric(customer_demographic_dataset.family_income_segment_code, errors='coerce').fillna(0).astype(int)

#Merge All User

customer_index_dataset.columns = ['user_id']

all_user_dataframe = pd.merge(customer_index_dataset, training_dataset, on=['user_id'], how='outer')

# Summary Dataset

all_tran_count_cc_df = pd.DataFrame(columns = ['user_id','cc_tran_count','cc_sum_amount'])
all_tran_count_dc_df = pd.DataFrame(columns = ['user_id','dc_tran_count','dc_sum_amount'])

all_tran_dataframe = pd.DataFrame(columns = ['user_id','cc_tran_count','cc_sum_amount','dc_tran_count','dc_sum_amount'])

all_purchase_history_dataframe = pd.DataFrame(columns = ['user_id','purchase_count','product_A_count','product_B_count'])

all_action_history_dataframe = pd.DataFrame(columns = ['user_id','number_action_history_screen1','dulation_action_history_screen1','number_action_history_screen2','dulation_action_history_screen2'])

all_saving_balance_dataframe = pd.DataFrame(columns = ['user_id','avg_saving_balance'])

all_advertisement_log_dataframe = pd.DataFrame(columns = ['user_id','number_advertisement_log'])

final_df = all_user_dataframe

for index_number, row in all_user_dataframe.iterrows():

    UserID = row['user_id']

    print UserID

    #Transaction cc

    target_user_cc = credit_card_transaction_dataset[credit_card_transaction_dataset['user_id']==int(row['user_id'])]

    Size_cc = len(target_user_cc.index)
    SumAmount_cc = target_user_cc['credit_card_txn_amt'].sum()

    target_user_cc_df = pd.DataFrame([[int(UserID),Size_cc,SumAmount_cc]],columns = ['user_id','cc_tran_count','cc_sum_amount'])

    all_tran_count_cc_df = pd.concat([all_tran_count_cc_df,target_user_cc_df])

    #Transaction cc

    target_user_dc = debit_card_transaction_dataset[debit_card_transaction_dataset['user_id']==int(row['user_id'])]

    Size_dc = len(target_user_dc.index)
    SumAmount_dc = target_user_dc['debit_card__txn_amt'].sum()

    target_user_dc_df = pd.DataFrame([[int(UserID),Size_dc,SumAmount_dc]],columns = ['user_id','dc_tran_count','dc_sum_amount'])

    all_tran_count_dc_df = pd.concat([all_tran_count_dc_df,target_user_dc_df])

    #merge cc - dc

    all_tran_dataframe = pd.merge(all_tran_count_cc_df, all_tran_count_dc_df, on=['user_id'], how='outer')

    #Purchase history

    purchase_history_target_user = purchase_history_dataset[purchase_history_dataset['user_id']==int(row['user_id'])]

    size_purchase_history = len(purchase_history_target_user.index)
    product_A_count = len(purchase_history_target_user[purchase_history_target_user['product'] == 'A'].index)
    product_B_count = len(purchase_history_target_user[purchase_history_target_user['product'] == 'B'].index)

    purchase_history_target_user_df = pd.DataFrame([[int(UserID),size_purchase_history,product_A_count,product_B_count]],columns = ['user_id','purchase_count','product_A_count','product_B_count'])

    all_purchase_history_dataframe = pd.concat([all_purchase_history_dataframe,purchase_history_target_user_df])

    #Action history

    action_history_target_user = action_history_dataset[action_history_dataset['user_id']==int(row['user_id'])]

    action_history_screen1 = action_history_target_user[action_history_target_user['screen']=='screen1']
    
    number_action_history_screen1 = len(action_history_screen1.index)

    dulation_action_history_screen1 = action_history_screen1['login_cnt'].sum()

    action_history_screen2 = action_history_target_user[action_history_target_user['screen']=='screen2']

    number_action_history_screen2 = len(action_history_screen2.index)

    dulation_action_history_screen2 = action_history_screen2['login_cnt'].sum()

    action_history_target_user_df = pd.DataFrame([[int(UserID),number_action_history_screen1,dulation_action_history_screen1,number_action_history_screen2,dulation_action_history_screen2]],columns = ['user_id','number_action_history_screen1','dulation_action_history_screen1','number_action_history_screen2','dulation_action_history_screen2'])

    all_action_history_dataframe = pd.concat([all_action_history_dataframe,action_history_target_user_df])

    # Saving balance

    saving_balance_target_user = saving_balance_dataset[saving_balance_dataset['user_id']==int(row['user_id'])]

    avg_saving_balance = saving_balance_target_user['balance'].mean()

    saving_balance_target_user_df = pd.DataFrame([[int(UserID),avg_saving_balance]],columns = ['user_id','avg_saving_balance'])

    all_saving_balance_dataframe = pd.concat([all_saving_balance_dataframe,saving_balance_target_user_df])

    # advertisement log

    advertisement_log_target_user = advertisement_log_dataset[advertisement_log_dataset['user_id']==int(row['user_id'])]

    number_advertisement_log_target_user = len(advertisement_log_target_user.index)

    # last_date_advertisement_target_user = 0

    # if pd.to_datetime(advertisement_log_target_user.iloc[1,-1]) :
    #     last_date_advertisement_target_user = pd.to_datetime('2018-07-06') - pd.to_datetime(advertisement_log_target_user.iloc[1,-1])

    # print last_date_advertisement_target_user

    advertisement_log_target_user_df = pd.DataFrame([[int(UserID),number_advertisement_log_target_user]],columns = ['user_id','number_advertisement_log'])

    all_advertisement_log_dataframe = pd.concat([all_advertisement_log_dataframe,advertisement_log_target_user_df])

    # print advertisement_log_target_user

    # pd.to_datetime('2018-07-06') - pd.to_datetime(advertisement_log_dataset['dt'])

    # print all_tran_dataframe

final_df = pd.merge(final_df, all_tran_dataframe, on=['user_id'], how='outer')
final_df = pd.merge(final_df, all_purchase_history_dataframe, on=['user_id'], how='outer')
final_df = pd.merge(final_df, all_action_history_dataframe, on=['user_id'], how='outer')
final_df = pd.merge(final_df, all_saving_balance_dataframe, on=['user_id'], how='outer')
final_df = pd.merge(final_df, customer_demographic_dataset, on=['user_id'], how='outer')
final_df = pd.merge(final_df, all_advertisement_log_dataframe, on=['user_id'], how='outer')

for columns in final_df.columns:
    final_df[columns].fillna(0, inplace=True)

final_df.to_csv("Techjam2018-dataset.csv")