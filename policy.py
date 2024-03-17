# Evaluation
def evalDict(policy: dict, password: str):
    ret = False
    for pt in policy.keys():
        if pt == "OR":
            pol = policy[pt]
            ret = polEval(pol, password)
            ret = max(ret)
            # print("or", ret, pol)
            if ret:
                break
        elif pt == "AND":
            pol = policy[pt]
            ret = polEval(pol, password)
            ret = min(ret)
            # print("and", ret, pol)
            if not ret:
                break
        else:
            print("function", pt, policy[pt])
    return ret


def polEval(policy, password):
    result = []
    if isinstance(policy, list):
        for pol in policy:
            result.append(polEval(pol, password))
    elif isinstance(policy, dict):
        return evalDict(policy, password)
    elif isinstance(policy, bool):
        return policy
    else:
        return policy(password)
    return result
