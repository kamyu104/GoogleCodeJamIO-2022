# [GoogleCodeJamIO 2022](https://codingcompetitions.withgoogle.com/codejamio/round/00000000009d9870) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-4%20%2F%204-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.googlecodejamio.2022)

* Python3 solutions of Google Kick Start 2022. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8` is not friendly for Python3 to solve in 5 ~ 15 seconds.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Speed Typing](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021)| [Python3](./Round%20A/speed_typing.py3)| _O(\|P\|)_ | _O(1)_ | Easy | | String |
|B| [Challenge Nine](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997)| [Python3](./Round%20A/challenge_nine.py3) | _O(logN)_ | _O(logN)_ | Easy | | Math, Greedy |
|C| [Palindrome Free Strings](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e762e)| [Python3](./Round%20A/palindrome_free_strings.py3) [Python3](./Round%20A/palindrome_free_strings2.py3) | _O(N)_ | _O(1)_ | Medium | | Backtracking, DP |
|D| [Interesting Integers](https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e73ea)| [Python3](./Round%20A/interesting_integers.py3) [Python3](./Round%20A/interesting_integers2.py3) | precompute: _O(2835 * log(MAX_B)^2)_<br>runtime: _O(9 * (logB)^2)_ | _O(2835 * log(MAX_B)^2)_ | Hard | | Counting, Memoization |
