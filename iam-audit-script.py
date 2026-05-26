import json

iam_users = [
    {"username": "admin-user", "mfa_enabled": False, "access_key_age_days": 120},
    {"username": "ops-user", "mfa_enabled": True, "access_key_age_days": 20},
    {"username": "dev-user", "mfa_enabled": False, "access_key_age_days": 95}
]

findings = []

for user in iam_users:
    if not user["mfa_enabled"]:
        findings.append({
            "user": user["username"],
            "issue": "MFA not enabled"
        })

    if user["access_key_age_days"] > 90:
        findings.append({
            "user": user["username"],
            "issue": "Stale access key"
        })

print(json.dumps(findings, indent=2))
