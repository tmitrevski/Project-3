# %%
import requests
import json
import pandas as pd
# %%
query = """query pools {
  pools(
    block: {number: 1312667}
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
      id
      symbol
      name
      decimals
      derivedETH
      __typename
    }
    token1 {
      id
      symbol
      name
      decimals
      derivedETH
      __typename
    }
    token0Price
    token1Price
    volumeUSD
    txCount
    totalValueLockedToken0
    totalValueLockedToken1
    totalValueLockedUSD
    __typename
  }
}
"""
# %%
url = 'https://api.thegraph.com/subgraphs/name/ianlapham/uniswap-optimism-dev'
r = requests.post(url, json={'query': query})
print(r.status_code)
print(r.text)
# %%