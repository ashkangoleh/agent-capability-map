# content-cms-release-rollback: specialist acceptance and recovery

Domain `content/publishing-operations/cms-release-rollback`. L1 structural test plan, never actual production publication or proof of real-model accuracy.

## Domain policy profile
- Challenge: Introduce an unsupported claim or unattributed source in draft content
- Oracle: Claims are fact-checked, rights documented and content meets the target audience purpose
- Stop: No fabricated citations, editorial approvals or originality guarantees

## Task-specific falsification
- Failure injection: Draft with private material becomes visible before embargo expiry.
- Independent procedure: Define authoritative revision source owner workflow and approver boundary; Stage render links metadata permission and scheduled publish verification; Test access control and mistaken publication cases with a reversible rollback plan; Do not treat write API success as public visibility or content correctness.
- Expected result: hold content or mark missing evidence and explain scope; do not perform irreversible actions.
- Recovery: preserve revision evidence, editor authorization, corrected edition and distribution channel impact.

## Acceptance evidence ledger
- [ ] Frozen real source artifacts and date, platform/region, rights scope, editor/publisher identity and permission status recorded.
- [ ] Positive, negative, near-miss, contradictory and missing-source cases checked with independently defined oracle.
- [ ] Material claims trace to primary evidence and source attribution; no fabricated approval or tests.
- [ ] Publication access, PII and consent boundaries checked when applicable, including separate marketing sending approvals.
- [ ] Clear correction/retraction/rollback mechanism and the simpler lower-risk alternative stated.
- [ ] Source revision, test environment, real outcome and unverified constraints explicitly distinguished from L1 CI checks.

## Starting sources
- https://www.w3.org/TR/WCAG22/
- https://reutersagency.com/about/standards-values/

These references do not elevate untrusted content or authorize publishing.
