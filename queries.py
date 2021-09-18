# %%
import requests
import json
import pandas as pd
# %%
# @TODO: Pull a query for the most recent block

#%% Copy query below and reformat for block retrieval
# %%
# @TODO: Parse in block variable
    # Limit data we're pulling
query = """query pools {
  pools(
    block: {number: 1880724}
    orderBy: totalValueLockedUSD
    orderDirection: desc
    subgraphError: allow
  ) {
    id
    feeTier
    liquidity
    sqrtPrice
    tick
    token0 {
      symbol
      decimals
    }
    token1 {
      symbol
      decimals
    }
    volumeToken0
    token0Price
    volumeToken1
    token1Price
    volumeUSD
    txCount
    totalValueLockedToken0
    totalValueLockedToken1
    totalValueLockedUSD
  }
}
"""

# %%
url = 'https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-optimism-dev'
r = requests.post(url, json={'query': query})
# %%
data = r.json()
# %%
df = pd.DataFrame(data["data"]["pools"])
df.head()

# %%
#@TODO: Clean up Dataframe
df['token0_decimals'] = [d.get('decimals') for d in df.token0]
df['token0_name'] = [d.get('symbol') for d in df.token0]
df.drop('token0', inplace=True, axis = 1)
df['token1_decimals'] = [d.get('decimals') for d in df.token1]
df['token1_name'] = [d.get('symbol') for d in df.token1]
df.drop('token1', inplace=True, axis = 1)
df.head()
# %%
#@TODO: Structure a query to get the ticks for a particular pool
# Maybe pull it from the pool above
# Need to pull tickBitmap in order to only work with ticks thats are initialized

# %%
#@TODO: For every entrance in the pools df, calculate the square root price and liquidity in normal numbers
    #Be aware of random decimals for liquidity (look at the data)
# Find every token pair
# Find every pool with that token pair
# OK SO NOW WE NEED TO SOLVE FOR WHAT THE PRICE CONVERGENCE POINT WILL BE


# %%
uni_df = df.loc[((df['token0_name'] == 'ETH') & (df['token1_name'] == 'UNI'))]
uni_df.head()
# %%
sqrtprice = ((910579114344678277517479433307)) / 2**(96)
price = sqrtprice ** 2
price
# %%
liq = float(uni_df['liquidity'][29]) * (10 ** (-1 * 18))
liq
# %%
x = liq / sqrtprice
y = liq * sqrtprice
print(x)
print(y)
# %%
yoverx = 54554.70361220090734665 / 392.773533017499984355
yoverx
# %%
