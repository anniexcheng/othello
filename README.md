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

## Experiment 10: 3 Moves Ahead Min Max Pruning vs Random

B = 3 Moves Ahead Min Max Pruning | W = Random

(100 trials per run)

| Run | Results      | Time        | Winner
| --- | ------------ | ----------- | -----------------------------
| 1   | B: 90, W: 10 | 371.3230456 | 3 Moves Ahead Min Max Pruning 
| 2   | B: 86, W: 14 | 365.3254486 | 3 Moves Ahead Min Max Pruning 
| 3   | B: 89, W: 11 | 356.6269122 | 3 Moves Ahead Min Max Pruning 

3 Moves Ahead Min Max Pruning AI has a 88.33% win rate.

Each game takes on average 3.644 seconds.

## Experiment 11: 4 Moves Ahead Min Max Pruning vs Random

B = 4 Moves Ahead Min Max Pruning | W = Random

(100 trials per run)

| Run | Results      | Time         | Winner
| --- | ------------ | ------------ | -----------------------------
| 1   | B: 90, W: 10 | 3519.2586111 | 4 Moves Ahead Min Max Pruning 
| 2   | B: 92, W: 8  | 3461.8270923 | 4 Moves Ahead Min Max Pruning 
| 3   | B: 91, W: 9  | 3466.9219156 | 4 Moves Ahead Min Max Pruning 

4 Moves Ahead Min Max Pruning AI has a 91% win rate.

Each game takes on average 34.827 seconds.

## Experiment 12: 5 Moves Ahead Min Max Pruning vs Random

B = 5 Moves Ahead Min Max Pruning | W = Random

(100 trials per run)

| Run | Results     | Time          | Winner
| --- | ----------- | ------------- | -----------------------------
| 1   | B: 94, W: 6 | 36452.1509229 | 5 Moves Ahead Min Max Pruning 
| 2   | B: 95, W: 5 | 36409.3769924 | 5 Moves Ahead Min Max Pruning 
| 3   | B: 98, W: 2 | 36285.4164915 | 5 Moves Ahead Min Max Pruning 

5 Moves Ahead Min Max Pruning AI has a 95.67% win rate.

Each game takes on average 363.823 seconds.

## Experiment 102: Monte Carlo vs 3 Moves Ahead MinMax

B = Monte Carlo | W = 3 Moves Ahead MinMax

(10 trials per run)

| Run | Results     | Time         | Winner
| --- | ----------- | ------------ | -----------
| 1   | B: 10, W: 0 | 4004.5383061 | Monte Carlo

Monte Carlo has a 100% win rate.

Each game takes on average 400.454 seconds.

## Experiment 103: Monte Carlo vs 4 Moves Ahead MinMax

B = Monte Carlo | W = 4 Moves Ahead MinMax

(10 trials per run)

| Run | Results    | Time         | Winner
| --- | ---------- | ------------ | -----------
| 1   | B: 9, W: 1 | 3708.4793977 | Monte Carlo

Monte Carlo has a 90% win rate.

Each game takes on average 370.848 seconds.

## Experiment 104: Monte Carlo vs 5 Moves Ahead MinMax

B = Monte Carlo | W = 5 Moves Ahead MinMax

(10 trials per run)

| Run | Results    | Time         | Winner
| --- | ---------- | ------------ | -----------
| 1   | B: 9, W: 1 | 6867.8314918 | Monte Carlo

Monte Carlo has a 90% win rate.

Each game takes on average 686.783 seconds.

## Experiment 1000: Simulated Annealing vs 3 Moves Min Max Pruned AI

B = Simulated Annealing | W = 3 Moves Min Max Pruned AI

(1000 trials per run)

| Run | Results        | Time     | Winner
| --- | -------------- | -------- | -------------------------
| 1   | B: 229, W: 771 | 739.5246 | 3 Moves Min Max Pruned AI

3 Moves Min Max Pruned AI has a 77.1% win rate.

Each game takes on average 0.74 seconds.

## Experiment 1001: Simulated Annealing vs 4 Moves Min Max Pruned AI

B = Simulated Annealing | W = 4 Moves Min Max Pruned AI

(100 trials per run)

| Run | Results     | Time     | Winner
| --- | ----------- | -------- | -------------------------
| 1   | B: 8, W: 92 | -------- | 4 Moves Min Max Pruned AI

4 Moves Min Max Pruned AI has a 92% win rate.

## Experiment 1003:  3 Moves Min Max Pruned AI vs Simulated Annealing

B = 3 Moves Min Max Pruned AI | W = Simulated Annealing 

(1000 trials per run)

| Run | Results        | Time        | Winner
| --- | -------------- | ----------- | -------------------------
| 1   | B: 805, W: 195 | 864.9745707 | 3 Moves Min Max Pruned AI

3 Moves Min Max Pruned AI has a 80.5% win rate.

Each game takes on average 0.867 seconds.

## Experiment 1004: 4 Moves Min Max Pruned AI vs Simulated Annealing

B = 4 Moves Min Max Pruned AI | W = Simulated Annealing

(100 trials per run)

| Run | Results     | Time        | Winner
| --- | ----------- | ----------- | -------------------------
| 1   | B: 93, W: 7 | 834.4100537 | 4 Moves Min Max Pruned AI

4 Moves Min Max Pruned AI has a 93% win rate.

Each game takes on average 8.344 seconds.

## Experiment 1006: Simulated Annealing vs Random

B = Simulated Annealing | W = Random

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------------
| 1   | B: 8393, W: 1607 | 193.9548190 | Simulated Annealing

Simulated Annealing has a 83.93% win rate.

Each game takes on average 0.019 seconds.

## Experiment 1007: Random vs Simulated Annealing

B = Random | W = Simulated Annealing

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------------
| 1   | B: 8799, W: 1201 | 179.9206823 | Simulated Annealing

Simulated Annealing has a 87.99% win rate.

Each game takes on average 0.018 seconds.

## Experiment 1008: Simulated Annealing vs Naive Eval

B = Simulated Annealing | W = Naive Eval

(10000 trials per run)

| Run | Results           | Time        | Winner
| --- | ---------------- | ----------- | -------------------
| 1   | B: 8041, W: 1959 | 257.7942597 | Simulated Annealing

Simulated Annealing has a 80.41% win rate.

Each game takes on average 0.026 seconds.

## Experiment 1009: Naive Eval vs Simulated Annealing

B = Naive Eval | W = Simulated Annealing 

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------------
| 1   | B: 1871, W: 8129 | 248.6963340 | Simulated Annealing

Simulated Annealing has a 81.29% win rate.

Each game takes on average 0.025 seconds.

## Experiment 1010: Simulated Annealing vs 1 Move MinMax (temperature = 0.1)

B = Simulated Annealing  | W = 1 Move MinMax

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------
| 1   | B: 4039, W: 5961 | 253.5756809 | 1 Move MinMax

1 Move MinMax has a 59.61% win rate.

Each game takes on average 0.025 seconds.


## Experiment 1010 v2: Simulated Annealing vs 1 Move MinMax (temperature = 0.5)

B = Simulated Annealing  | W = 1 Move MinMax

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------
| 1   | B: 3967, W: 6033 | 248.6963340 | 1 Move MinMax

1 Move MinMax has a 60.33% win rate.

Each game takes on average 0.03 seconds.

## Experiment 1010 v3: Simulated Annealing vs 1 Move MinMax (temperature = 0.75)

B = Simulated Annealing  | W = 1 Move MinMax

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------
| 1   | B: 3209, W: 6791 | ----------- | 1 Move MinMax

1 Move MinMax has a 67.91% win rate.

## Experiment 1011: 1 Move MinMax (0.1) vs Simulated Annealing

B = 1 Move Minimax  | W = Simulated Annealing

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------------
| 1   | B: 5298, W: 4702 | 261.6754794 | 1 Move MinMax

1 Move MinMax has a 52.98% win rate.

Each game takes on average 0.026 seconds.

## Experiment 1011 v2: 1 Move MinMax (0.5) vs Simulated Annealing

B = 1 Move Minimax  | W = Simulated Annealing

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------------
| 1   | B: 5969, W: 4031 | 248.6963340 | 1 Move MinMax

1 Move MinMax has a 59.69% win rate.

Each game takes on average 0.026 seconds.

## Experiment 1011 v3: 1 Move MinMax (0.75) vs Simulated Annealing

B = 1 Move Minimax  | W = Simulated Annealing

(10000 trials per run)

| Run | Results          | Time        | Winner
| --- | ---------------- | ----------- | -------------------
| 1   | B: 6415, W: 3585 | ----------- | 1 Move MinMax

1 Move MinMax has a 64.15% win rate.

## Minimax Experiments: Min Max Pruned AI Score Comparisons

| AIs    | Score | Winner
| -------| ----- | ------ 
| 3 vs 4 | 18:46 | 4
| 3 vs 5 | 8:51  | 5
| 3 vs 6 | 28:36 | 6
| 4 vs 3 | 38:26 | 4
| 4 vs 5 | 44:20 | 4
| 4 vs 6 | 16:48 | 6
| 5 vs 3 | 44:20 | 5
| 5 vs 4 | 8:51  | 4
| 5 vs 6 | 22:42 | 6
| 6 vs 3 | 30:34 | 3
| 6 vs 4 | 53:11 | 6
| 6 vs 5 | 43:21 | 6

## Minimax Baseline Experiments: Min Max Pruned AI vs Naive Eval Scores
| AIs             | Score | Winner
| --------------- | ----- | ------ 
| 3 vs Naive Eval | 55:9  | 3
| 4 vs Naive Eval | 28:36 | Naive Eval
| 5 vs Naive Eval | 48:16 | 5
| 6 vs Naive Eval | 53:11 | 6










