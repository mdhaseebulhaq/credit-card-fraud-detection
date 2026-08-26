import pandas as pd

# Input files
transaction_path = "data/train_transaction.csv"
identity_path = "data/train_identity.csv"

# Output file
output_path = "data/train_merged.csv"

print("Loading transaction data...")

train_transaction = pd.read_csv(transaction_path)

print("Transaction data loaded:", train_transaction.shape)

print("Loading identity data...")

train_identity = pd.read_csv(identity_path)

print("Identity data loaded:", train_identity.shape)

print("Merging datasets...")

train_merged = train_transaction.merge(
    train_identity,
    on="TransactionID",
    how="left"
)

print("Merged dataset shape:", train_merged.shape)

print("Saving merged dataset...")

train_merged.to_csv(output_path, index=False)

print("SUCCESS!")
print("Saved to:", output_path)