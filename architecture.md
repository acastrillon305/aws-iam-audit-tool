# Architecture Overview

This project represents a simple IAM audit workflow.

## Flow

1. IAM user data is collected
2. Script checks MFA status
3. Script checks access key age
4. Findings are written as JSON output
5. Security or operations teams review findings

## Why This Matters

IAM audits help identify weak access controls, reduce cloud security risk, and support compliance reviews.

## Example Findings

- User without MFA enabled
- Access key older than 90 days
- Accounts requiring security review
