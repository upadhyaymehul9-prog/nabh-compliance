"""Verify the reconstructed hic2_draft.json against md5 hashes from the live row.

The hashes in DB_STEP_MD5 were read from shco_policy_masters with:

    select ord, md5(step), length(step)
    from public.shco_policy_masters,
         lateral unnest(procedure_steps) with ordinality as t(step, ord)
    where standard_code = 'HIC.2' order by ord;

A reconstruction is only usable if EVERY step matches. Partial matches mean the
inversion of the renderer is lossy somewhere and the output must not be trusted.
"""

import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent

# (md5, char_length) per step, in order, from the live HIC.2 row.
DB_STEP_MD5 = [
    ("a766f71aebb541483b68f802638eed09", 648),
    ("89a83d2297a658f9b85a21673160ea86", 1340),
    ("f2601bf682b3511ef2379d6cc08b9fbc", 1662),
    ("0711c367ee520320ee50ff16f68199f4", 844),
    ("5f7a2c19e6db331ee2b2b422f333b847", 1174),
    ("9a49861b86e927ea51f0fd857e546edc", 862),
    ("67129e883dcf4b3cd7cb52b8bdac4da9", 831),
    ("6f0bd913924c821c0114fb65210e2288", 1674),
    ("f9b28b96ca79f1b3c35fe7e5a0fb8eb1", 1444),
    ("4cf43285abd87103f1df1e9d2bc2e98c", 983),
    ("47a1a215c40ef4cea93cc7e89f13b2bb", 750),
    ("835b5713879fbcd9dfd32bdc9b6bf67a", 1484),
    ("54ba43f6af521f825fa2db9bf821a2e0", 748),
    ("4d7bb01f9dd1bc014d849e3b7e9f4e25", 803),
    ("5f3243e38469ae961e76cb4454086d48", 1229),
    ("6ff083871aa1458ce913194c8a90e133", 1149),
    ("bf63f9357fdcda0ab57734b5d97a9ddc", 767),
    ("99e444f24a66e28cdecca0a1775a1b0f", 1441),
    ("cf3ee55d5681367a3487f50decb5a5f9", 1066),
    ("e18cecfc051814f60c4e5869a41b24f0", 1263),
    ("45c573e57b50c6eb961bc5a91d181ed9", 1040),
    ("00aa6aee93ed69ea355b42e015888a88", 1135),
    ("1c56455a84867d90b64d7ff781626bd7", 2146),
    ("57406b118df3c34ba9bc3a13a1e2e017", 3154),
    ("7f4638e81accbd7b270a2bdacfa5ed2a", 3171),
    ("f62d4ee0c4212ecb0a6de19cb6af9c53", 2220),
    ("dbed9037678c219d7ce1c4408162f07a", 1732),
    ("6bdaf222c8a8f598d28e6ba7cb5a84eb", 1724),
    ("1f3c7e072f0cbf175e5bc858252e6d6f", 2487),
    ("87a24c503128597cffb95a23b351958b", 1751),
    ("fab9b55856397eedcd2232c5032f3adb", 1242),
    ("6cec70b75cbde2ef56d3e1ad5808ce1b", 1670),
    ("36ade62c8b767054c37c8a7ae9178a16", 656),
]


def main():
    draft = json.loads((REPO / "policies/drafts/hic2_draft.json").read_text(encoding="utf-8"))
    steps = draft["procedure_steps"]

    if len(steps) != len(DB_STEP_MD5):
        print(f"FAIL: step count {len(steps)} != live row {len(DB_STEP_MD5)}")
        raise SystemExit(1)

    bad = []
    for i, (step, (want_md5, want_len)) in enumerate(zip(steps, DB_STEP_MD5), 1):
        got = hashlib.md5(step.encode("utf-8")).hexdigest()
        if got != want_md5:
            bad.append((i, len(step), want_len, len(step) - want_len))

    if not bad:
        print(f"PASS: all {len(steps)} steps match the live HIC.2 row byte-for-byte.")
        return

    print(f"FAIL: {len(bad)} of {len(steps)} steps differ from the live row.")
    print(f"{'step':>5} {'got_len':>8} {'db_len':>8} {'delta':>7}")
    for i, got_len, want_len, delta in bad:
        print(f"{i:>5} {got_len:>8} {want_len:>8} {delta:>+7}")
    raise SystemExit(1)


if __name__ == "__main__":
    main()
