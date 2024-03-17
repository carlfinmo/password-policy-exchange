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

password1 = "password"
password10 = "password!!"
passpharse = "horse-battery-staple-correct"
policy = parseTextPol(policyText)
print(polEval(policy, password1))  # False
print(polEval(policy, password10))  # True
print(polEval(policy, passpharse))  # True
```
