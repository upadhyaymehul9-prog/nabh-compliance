Bug: oe_code matching is inconsistent depending on how the user types it.

Confirmed working: "AAC .1.a" (uppercase, with dots, stray space) → matches correctly.
Confirmed failing: "aac 1 a" (lowercase, no dots, spaces instead of dots) → no match found.

Real hospital users will type codes in many inconsistent ways: "aac1a",
"AAC 1 A", "aac.1.a", "Aac-1-A", etc. The matching logic needs to normalize
ALL of these to the same canonical format before querying.

Fix: in the retrieval function, before attempting the oe_code match:
1. Convert the question text segment to uppercase
2. Strip all whitespace
3. Replace any of these separator characters with a single consistent
   format matching the DB's actual oe_code pattern (CHAPTER.NUMBER.LETTER,
   e.g. "AAC.1.a") — handle separators: space, hyphen, no separator at all
4. Use a regex that captures: 2-4 letter chapter code, then digits, then
   a single letter, regardless of what (if any) separator appears between
   them in the user's input
5. Reconstruct the query string in the exact DB format before the ILIKE match

Test cases that must ALL resolve to the same OE (AAC.1.a):
- "AAC.1.a"
- "AAC .1.a" (stray space)
- "aac 1 a" (lowercase, space-separated)
- "aac1a" (no separators at all)
- "AAC-1-A" (hyphens)

After fixing, redeploy and test all 5 variants above against the live
endpoint. Confirm all 5 return the same grounded answer citing AAC.1.a.
