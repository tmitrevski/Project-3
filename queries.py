# %%
import requests
import json
import pandas as pd
# %%
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
df['token0_decimals'] = [d.get('decimals') for d in df.token0]
df['token0_name'] = [d.get('symbol') for d in df.token0]
df.drop('token0', inplace=True, axis = 1)
df['token1_decimals'] = [d.get('decimals') for d in df.token1]
df['token1_name'] = [d.get('symbol') for d in df.token1]
df.drop('token1', inplace=True, axis = 1)
df.head()
# %%
uni_df = df.loc[((df['token0_name'] == 'ETH') & (df['token1_name'] == 'UNI'))]
uni_df.head()
# %%
sqrtprice = ((914809224745660573156617212212)) / 2**(96)
price = sqrtprice ** 2
price
# %%
liq = float(uni_df['liquidity'][4]) * (10 ** (-1 * 18))
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
