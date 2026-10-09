# Optional arithmetic helper

`total_points.py` uses only the Python standard library (Python 3.8+).
It is optional; a host calculator can perform the same arithmetic.

```sh
python3 scripts/total_points.py /path/to/factors.json
```

## Input

Use a UTF-8 JSON object with at most one integer point value per factor.
These are **mechanical baseline bands**, not confirmation of current law or
of the applicant's entitlement. Refresh and verify applicable law separately
before selecting values. The helper does not check facts, evidence, dates,
visa subclass compatibility, or eligibility.

| Factor | Accepted integer points |
| --- | --- |
| `age` | 0, 15, 25, 30 |
| `english` | 0, 10, 20 |
| `overseas_employment` | 0, 5, 10, 15 |
| `australian_employment` | 0, 5, 10, 15, 20 |
| `professional_year` | 0, 5 |
| `education` | 0, 10, 15, 20 |
| `specialist_education` | 0, 10 |
| `australian_study` | 0, 5 |
| `community_language` | 0, 5 |
| `regional_study` | 0, 5 |
| `partner` | 0, 5, 10 |
| `nomination` | 0, 5, 15 |

Every factor also accepts `null`. Missing or null factors are **unresolved**,
not confirmed zeroes. Explicit `0` is resolved for arithmetic only. Booleans,
negative numbers, floats (including `30.0`), strings, arrays, nested values,
unknown fields, duplicate keys, and invalid bands are rejected. Multiple
values cannot be stacked within a factor.

Synthetic input (not an entitlement example):

```json
{"age": 30, "english": null, "overseas_employment": 15, "australian_employment": 20}
```

## Output

The command writes one JSON object to stdout. Successful arithmetic exits `0`:

- `status`: always `"provisional"`.
- `notice`: explicitly says factual and legal entitlement is not verified;
  there is no eligibility judgment.
- `provisional_supported_subtotal`: sum of supplied, non-null values, with
  combined employment capped at 20. Here, “supported” refers only to the
  supplied numeric inputs, not verified evidence or legal entitlement.
- `unresolved`: missing/null factor names in the table's order.
- `employment_raw`: sum of supplied, non-null employment inputs.
- `employment_capped`: the raw sum capped at 20.

For the synthetic input above the subtotal is `50`, raw employment is `35`,
and capped employment is `20`. In a different input omitting both employment factors, those factors remain
unresolved even when the raw/capped employment numbers are `0`; the numbers
represent only supplied values, never assumed entitlement.

Input, file-reading, and argument errors produce `{"error": "..."}` on stdout
and exit `2`, without a traceback. There is no eligibility threshold, visa
recommendation, factual-entitlement validation, or date validation.

The source includes the full BSD-0-Clause license text, without an invented
copyright owner.
