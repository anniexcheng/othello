## Experiment 1: Random vs Random

B = Random 1 | W = Random 2 

(10,000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | --------
| 1   | W: 5368, B: 4632 | 439.2866395 | Random 2
| 2   | W: 5524, B: 4476 | 439.2661288 | Random 2
| 3   | W: 5483, B: 4517 | 442.0089947 | Random 2

Random 2 AI has a 54.5% win rate.

Each game takes on average 0.044 seconds.

## Experiment 2: Naive Eval Function vs Random

B = Naive Eval Function | W = Random

(10,000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------------
| 1   | B: 5836, W: 4164 | 747.3224598 | Naive Eval Function
| 2   | B: 5720, W: 4280 | 749.3102613 | Naive Eval Function
| 3   | B: 5849, W: 4151 | 749.6389969 | Naive Eval Function

Naive Eval Function AI has a 58.02% win rate.

Each game takes on average 0.0749 seconds.

## Experiment 3: 3 Moves Ahead Min Max vs Random

B = 3 Moves Ahead Min Max | W = Random

(10,000 trials per run)

| Run | Results         | Time          | Winner
| --- | --------------- | ------------- | ---------------------
| 1   | B: 9060, W: 940 | 37763.5919878 | 3 Moves Ahead Min Max
| 2   | B: 9072, W: 928 | 38069.0639094 | 3 Moves Ahead Min Max
| 3   | B: 9113, W: 887 | 37606.2559796 | 3 Moves Ahead Min Max

3 Moves Ahead Min Max AI has a 90.82% win rate.

Each game takes on average 3.781 seconds.

## Experiment 4: 4 Moves Ahead Min Max vs Random

B = 4 Moves Ahead Min Max | W = Random

(100 trials per run)

| Run | Results     | Time         | Winner
| --- | ----------- | ------------ | ---------------------
| 1   | B: 95, W: 5 | 3645.0901571 | 4 Moves Ahead Min Max
| 2   | B: 97, W: 3 | 3626.1859856 | 4 Moves Ahead Min Max
| 3   | B: 95, W: 5 | 3595.4563586 | 4 Moves Ahead Min Max

4 Moves Ahead Min Max AI has a 95.67% win rate.

Each game takes on average 36.222 seconds.

## Experiment 5: 5 Moves Ahead Min Max vs Random

B = 5 Moves Ahead Min Max | W = Random

(100 trials per run)

| Run | Results     | Time          | Winner
| --- | ----------- | ------------- | ---------------------
| 1   | B: 99, W: 1 | 38043.4888369 | 5 Moves Ahead Min Max
| 2   | B: 92, W: 8 | 38314.4652632 | 5 Moves Ahead Min Max
| 3   | B: 92, W: 8 | 39029.5983387 | 5 Moves Ahead Min Max

5 Moves Ahead Min Max AI has a 94.33% win rate.

Each game takes on average 384.625 seconds.

## Experiment 8: 3 Moves Ahead Min Max Pruning vs Random

B = 3 Moves Ahead Min Max Pruning | W = Random

(100 trials per run)

| Run | Results      | Time        | Winner
| --- | ------------ | ----------- | -----------------------------
| 1   | B: 90, W: 10 | 371.3230456 | 3 Moves Ahead Min Max Pruning 
| 2   | B: 86, W: 14 | 365.3254486 | 3 Moves Ahead Min Max Pruning 
| 3   | B: 89, W: 11 | 356.6269122 | 3 Moves Ahead Min Max Pruning 

3 Moves Ahead Min Max Pruning AI has a 88.33% win rate.

Each game takes on average 3.644 seconds.

## Experiment 9: 4 Moves Ahead Min Max Pruning vs Random

B = 4 Moves Ahead Min Max Pruning | W = Random

(100 trials per run)

| Run | Results      | Time         | Winner
| --- | ------------ | ------------ | -----------------------------
| 1   | B: 90, W: 10 | 3519.2586111 | 4 Moves Ahead Min Max Pruning 
| 2   | B: 92, W: 8  | 3461.8270923 | 4 Moves Ahead Min Max Pruning 
| 3   | B: 91, W: 9  | 3466.9219156 | 4 Moves Ahead Min Max Pruning 

4 Moves Ahead Min Max Pruning AI has a 91% win rate.

Each game takes on average 34.827 seconds.

## Experiment 10: 5 Moves Ahead Min Max Pruning vs Random

B = 5 Moves Ahead Min Max Pruning | W = Random

(100 trials per run)

| Run | Results     | Time          | Winner
| --- | ----------- | ------------- | -----------------------------
| 1   | B: 94, W: 6 | 36452.1509229 | 5 Moves Ahead Min Max Pruning 
| 2   | B: 95, W: 5 | 36409.3769924 | 5 Moves Ahead Min Max Pruning 
| 3   | B: 98, W: 2 | 36285.4164915 | 5 Moves Ahead Min Max Pruning 

5 Moves Ahead Min Max Pruning AI has a 95.67% win rate.

Each game takes on average 363.823 seconds.










