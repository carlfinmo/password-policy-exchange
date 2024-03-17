# What
A password policy specification language and evaluator

# Motivating idea
Allow a single source of truth for password policy specification
that can be synchronized/shared.

# Status
Exploratory

# Example
```
# Policy to allow conventional password with enough complexity OR a passphrase
# Each line is OR, Each expression within a line is AND, separated by ;
policyText = """
CheckLengthV1 10; CheckSpecialsV1 2
CheckLengthV1 20
"""
passPr = parseTextPol(policyText)
print("pol3 <passphrase len=20+>", polEval(pol3, passphrase)) # True
print("pol3 <passphrase len=20+>", polEval(pol3, passphrase)) # False
```
