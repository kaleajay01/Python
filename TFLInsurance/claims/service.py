from claims.claim import Claim
from claims.repository import ( save_claim, get_all_claims )


def create_claim():

    claim_id = len(get_all_claims()) + 1

    policy_id = int(input("Enter policy ID: "))
    amount = float(input("Enter claim amount: "))
    reason = input("Enter claim reason: ")

    claim = Claim( claim_id, policy_id, amount, reason)

    save_claim(claim)

    print("Claim submitted successfully.")
    print(claim)


def process_claim():

    claim_id = int(input("Enter claim ID: "))
    claims = get_all_claims()
    claim =claims[claim_id]

    if claim is None:
        print("Claim not found.")
        return

    print("\nClaim Details")
    print(claim)

    print("\n1. Approve")
    print("2. Reject")

    choice = input("Enter choice: ")

    if choice == "1":
        claim.status = "Approved"
        print("Claim approved.")

    elif choice == "2":
        claim.status = "Rejected"
        print("Claim rejected.")

    else:
        print("Invalid choice.")


def get_claim_details():

    claim_id = int(input("Enter claim ID: "))
    claims = get_all_claims()
    claim =claims[claim_id]

    if claim:
        print(claim)
    else:
        print("Claim not found.")


def get_all_claim_details():

    claims = get_all_claims()

    if not claims:
        print("No claims available.")
        return

    for claim in claims:
        print(claim)