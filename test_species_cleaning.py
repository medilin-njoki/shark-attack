import pandas as pd
import cleaning as cl

# Read the Excel file
df = pd.read_excel('GSAF5.xls')

# Apply existing cleaning functions
shark_attack_df = cl.drop_useless_columns(df)
shark_attack_df = cl.clean_date(shark_attack_df)
shark_attack_df = cl.clean_type(shark_attack_df)
shark_attack_df = cl.clean_sex(shark_attack_df)
shark_attack_df = cl.clean_age(shark_attack_df)
shark_attack_df = cl.clean_country(shark_attack_df, 60)
shark_attack_df = cl.clean_state(shark_attack_df, 60)

# Apply species cleaning
shark_attack_df = cl.clean_species(shark_attack_df)

# Show results
print("Species cleaning results:")
print(shark_attack_df['Species'].value_counts().head(20))
print(f"\nUnique species count: {shark_attack_df['Species'].nunique()}")