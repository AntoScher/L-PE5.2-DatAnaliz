import pandas as pd
payments = pd.read_csv('payments_result.csv')
#payments.query('is_trial == 1')
#payments.query('is_trial == 1').drop_duplicates()[['user_id', 'is_trial']]
#payments.query('is_trial == 1').drop_duplicates()[['user_id', 'is_trial']].reset_index(drop=True)
trial_users = payments.query('is_trial == 1').drop_duplicates()[['user_id', 'is_trial']]
#payments.query('amount>0')
#payments.query('amount>0').drop_duplicates()[['user_id', 'amount']]
payed_users = payments.query('amount>0').drop_duplicates()[['user_id', 'amount']]
print (trial_users.head())
print (payed_users.head())

joined_t = payed_users.merge(trial_users, how='left')
print (joined_t.head())
joined_t['is_trial'].sum()
joined_t['user_id'].count()
print ('Доля тех, кто имел пробный период, из тех, кто оплатил',round(joined_t['is_trial'].sum()/joined_t['user_id'].count()*100,1),'%')

