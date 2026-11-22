test_cases = [{"name":"Valid Login:", "expected":"PASS", "actual":"PASS"}, {"name":"Invalid Password:", "expected":"FAIL", "actual":"FAIL"}, {"name":"Empty Username:", "expected":"FAIL", "actual":"PASS"}, {"name":"Logout:", "expected":"PASS", "actual":"PASS"}]
for test in test_cases:
    if test["actual"] == test["expected"]:
        print(test["name"], "Test Result: PASS")
    else:
        print(test["name"], "Test Result: FAIL")


