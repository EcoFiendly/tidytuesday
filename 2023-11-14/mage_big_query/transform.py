import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df = df.drop_duplicates().reset_index(drop=True)

    # Group by 'Product_ID' and find the mode for each group
    mode_per_product_id = df.groupby('Product_ID')['Product_Category'].agg(lambda x: x.mode().iloc[0]).reset_index()

    # Merge the mode_per_product_id DataFrame back to the original DataFrame
    df = pd.merge(df, mode_per_product_id, on='Product_ID', how='left', suffixes=('', '_mode'))

    # Backfill 'Product_Category' with the mode values
    df['Product_Category'] = df['Product_Category_mode'].combine_first(df['Product_Category'])

    # Drop the extra column
    df = df.drop(['Product_Category_mode'], axis=1)

    customer_dim = df[["User_ID", 
                   "Cust_name", 
                   "Gender", 
                   "Age", 
                   "Marital_Status", 
                   "Occupation"
                   ]].drop_duplicates().reset_index(drop=True)
    
    age_dim = df[["Age", "Age Group"]].drop_duplicates().reset_index(drop=True)

    location_dim = df[["State", "Zone"]].drop_duplicates().reset_index(drop=True)

    product_dim = df[["Product_ID", "Product_Category"]].drop_duplicates().reset_index(drop=True)

    fact_table = df[["User_ID", "Product_ID", "Amount", "Orders"]].drop_duplicates().reset_index(drop=True)

    fact_table["Sale_ID"] = fact_table.index

    return {
        "fact_table": fact_table.to_dict(orient="dict"),
        "customer_dim": customer_dim.to_dict(orient="dict"),
        "age_dim": age_dim.to_dict(orient="dict"),
        "location_dim": location_dim.to_dict(orient="dict"),
        "product_dim": product_dim.to_dict(orient="dict"),
    }

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'