Bug found in live testing: oe_code matching fails when the code is embedded
in a natural-language question, even though the bare code alone works fine.

Confirmed working: "MOM 3 F" (bare code, space-separated) → matches correctly,
returns grounded answer citing MOM.3.f.

Confirmed failing: "what is MOM.3.g" (natural language wrapping a valid,
real code) → "I couldn't find a matching SHCO Full requirement" — even
though MOM.3.g is a real, confirmed OE in the live database.

Real hospital users will almost always type natural-language questions
("what is X", "tell me about X", "how do I comply with X"), not bare codes.
The current regex likely only matches when the code is the ENTIRE input
(after whitespace normalization), not when it's a substring within a longer
sentence.

Fix: update the oe_code regex extraction in supabase/functions/ai-assistant/
index.ts to find a valid code PATTERN ANYWHERE within the question string,
not just when the whole (normalized) input equals the pattern. The regex
should scan the full question text for something matching
[A-Z]{2,4}\.?\d+\.?[a-z] (case-insensitive) regardless of surrounding words,
extract just that match, normalize it, then query against it — same
normalization logic already built (handles spaces, hyphens, case), just
needs to work when embedded in a sentence rather than requiring the whole
input to be only the code.

Test cases that must ALL resolve to MOM.3.g:
- "MOM.3.g"
- "MOM 3 G"
- "what is MOM.3.g"
- "what is MOM 3 G"
- "tell me about MOM.3.g"
- "how do I comply with MOM.3.g"

If no code pattern is found anywhere in the question, fall through to the
existing keyword search as before — that part of the logic is unchanged.

After fixing, redeploy and test all 6 variants above against the live
endpoint. Confirm all 6 return the same grounded answer citing MOM.3.g
(corrective/preventive action based on audit).
