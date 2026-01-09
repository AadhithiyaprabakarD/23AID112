def process_transactions(accounts, transactions):
    final_balances = accounts.copy()  
    processed_accounts = set()

    for trans in transactions:
        account_id, amount, trans_type = trans
        try:
            if account_id not in final_balances:
                raise KeyError(f"Account {account_id} not found.")
            if trans_type == 'deposit':
                final_balances[account_id] += amount
            elif trans_type == 'withdraw':
                if final_balances[account_id] < amount:
                    raise ValueError(f"Insufficient funds in account {account_id}.")
                final_balances[account_id] -= amount
            else:
                raise ValueError(f"Invalid transaction type '{trans_type}'.")
            processed_accounts.add(account_id)  
        except (KeyError, ValueError) as e:
             print(e)  
        continue
    return final_balances, processed_accounts
accounts = {101: 500.0, 102: 300.0}
transactions = [(101, 100.0, 'deposit'), (102, 400.0, 'withdraw'), (101, 50.0, 'invalid')] 
print(process_transactions(accounts, transactions))

