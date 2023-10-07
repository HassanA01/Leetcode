
## Max Profit from Stock Prices

The goal is to calculate the maximum profit one can achieve by buying and selling a stock given its daily prices. 

### Approach

1. **Initialization**:
    - `max_profit`: The maximum profit achieved so far. Initialized to 0 since we haven't processed any transactions yet.
    - `buyDay`: The index or day on which we consider buying the stock. Starts at 0, the first day.
    - `sellDay`: The index or day on which we consider selling the stock after buying it on `buyDay`. Starts at 1, the day after the `buyDay`.

2. **Traversal**:
    We continue examining potential sell days until we've examined all prices.

    - `current_profit`: Calculate the profit made if we bought the stock on `buyDay` and sold it on `sellDay`.

    - **Check if Current Pair is Profitable**:
        If the price on `buyDay` is less than the price on `sellDay`, it means there's a potential profit. We update the `max_profit` with the greater of the current `max_profit` or the `current_profit`.

    - **Adjust Buy Day if Needed**:
        If the price on `buyDay` is not less than the price on `sellDay`, it indicates that buying on `buyDay` and selling on `sellDay` will not yield a profit or might reduce the profit. Thus, we update `buyDay` to be `sellDay` to consider new buying opportunities.

    - **Move to the Next Day**:
        Increment `sellDay` to examine the next potential selling day.

### Output

At the end of the loop, `max_profit` will have the maximum profit that can be achieved given the daily stock prices.
